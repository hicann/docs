# 单边通信

HIXL（Huawei Xfer Library）是一个灵活、高效的昇腾单边通信库，面向集群场景提供简单、可靠、高效的点对点数据传输能力，并通过简易API开放给用户, 在多AI应用和多传输链路之间建立了桥梁。可用于构建大模型PD分离、RL后训练参数切换、模型参数缓存等多种业务场景。

本节仅针对HIXL做简要介绍，关于HIXL的详细使用方法可参见《HIXL单边通信库》。

## 核心优势

- 支持单边零拷贝（One-Sided Zero-Copy）通信机制：单边通信库提供简易、可靠的单边通信接口，可在本地内存数据准备就绪之后，通过单边操作完成向远端内存的直接数据传输。该机制无需远端节点执行任何操作，为用户构建通信与计算重叠掩盖的调度机制提供核心技术支撑。同时，零拷贝能力实现用户内存间的直接数据传输，避免冗余数据搬运，不仅可以降低内存带宽占用，还可以减少内存容量消耗。
- 屏蔽硬件差异，兼容多链路实现跨设备高速互联：单边通信库屏蔽了昇腾系列芯片的底层硬件差异，用户无需针对不同芯片架构进行代码适配。在通信链路层面，该技术原生支持RDMA，HCCS等多种高速互联协议，通信带宽最高可达119GB/s，可实现跨架构设备的无缝高速互联，满足低时延、 高吞吐的需求。
- 极简API设计，深度适配开源生态框架：单边通信库采用极简式API接口设计，接口数量精简至10余个核心调用，降低开发者集成门槛，同时提供完善的C++/Python语言接口支持。目前已实现与Mooncake、DeepLink等开源框架的深度集成，vLLM、SGLang等主流推理引擎也可以直接调用单边通信库API完成KV Cache的跨设备高效传输，将大模型推理过程中的内存访问延迟降低20%，提升推理吞吐。

## 软件架构

单边通信库如图1所示。

**图 1** 单边通信库软件架构图  
![](figures/单边通信库软件架构图.png "单边通信库软件架构图")

**核心组件**

- HIXL Engine：作为核心传输引擎，提供了基础传输接口，支持多种内存类型传输，比如D2D、D2H、H2D。同时兼容多种传输协议，包括HCCS、RDMA等。可实现高速、可靠的数据传输。原生支持多类型数据链路，可适用于同构集群和异构集群的复杂场景。面对集群节点动态扩缩容需求时，可高效完成链路适配与资源调度，为集群整体运行构建可靠通信基础。
- LLM-DataDist：基于HIXL Engine构建，提供了一套携带KV Cache语义的数据传输接口。可快速、灵活对接vLLM、SGLang等推理引擎。

## 快速体验

该样例场景为H2RD（指数据从Host设备往远端Device设备传输），描述了Client向Server单边发起数据读写。

1. 在Client侧和Server侧分别绑定本进程使用的昇腾设备，并初始化HIXL对象，同时申请内存并向HIXL注册。
    - Client侧：

        ```cpp
        // 绑定本进程使用的昇腾设备。
        CHECK_ACL(aclrtSetDevice(device));
        
        // 以local_engine为标识初始化HIXL引擎（Client侧一般为无端口IP字符串）。
        Hixl hixl_engine;
        std::map<AscendString, AscendString> options;
        CHECK_HIXL(hixl_engine.Initialize(local_engine, options));
        
        // 分配Host侧传输缓冲区，供MEM_HOST注册与单边读写的本地一端使用。
        int32_t *host_buf = nullptr;
        CHECK_ACL(aclrtMallocHost(reinterpret_cast<void **>(&host_buf), sizeof(int32_t)));
        
        // 将Host地址注册给HIXL，使对端可通过已建链的链路做单边访问。
        MemDesc reg_desc{};
        reg_desc.addr = reinterpret_cast<uintptr_t>(host_buf);
        reg_desc.len = sizeof(int32_t);
        MemHandle handle = nullptr;
        CHECK_HIXL(hixl_engine.RegisterMem(reg_desc, MEM_HOST, handle));
        ```

    - Server侧：

        ```cpp
        // 绑定本进程使用的昇腾设备。
        CHECK_ACL(aclrtSetDevice(device));
        
        // 在带端口的local_engine上初始化HIXL，作为被连接端。
        Hixl hixl_engine;
        std::map<AscendString, AscendString> options;
        CHECK_HIXL(hixl_engine.Initialize(local_engine, options));
        
        // 在Device上分配内存，并通过H2D写入初值1，供Client READ验证。
        constexpr int32_t kInit = 1;
        int32_t *dev_buf = nullptr;
        CHECK_ACL(aclrtMalloc(reinterpret_cast<void **>(&dev_buf), sizeof(int32_t), ACL_MEM_MALLOC_HUGE_ONLY));
        CHECK_ACL(aclrtMemcpy(dev_buf, sizeof(int32_t), &kInit, sizeof(int32_t), ACL_MEMCPY_HOST_TO_DEVICE));
        
        // 将Device地址注册给HIXL，使Client可单边读写该地址区间。
        MemDesc reg_desc{};
        reg_desc.addr = reinterpret_cast<uintptr_t>(dev_buf);
        reg_desc.len = sizeof(int32_t);
        MemHandle handle = nullptr;
        CHECK_HIXL(hixl_engine.RegisterMem(reg_desc, MEM_DEVICE, handle));
        ```

2. 在Client侧向Server侧发起建链。

    ```cpp
    // 与remote_engine（Server侦听地址）建立传输链路。
    CHECK_HIXL(hixl_engine.Connect(remote_engine));
    ```

3. 在Client侧向Server侧发起数据读写。并分别在Client侧和Server侧检查读写值是否正常。
    - Client侧：

        ```cpp
        // 单边读：从对端Server的MEM_DEVICE读取预写的1到本地Host内存。
        TransferOpDesc xfer{reinterpret_cast<uintptr_t>(&host_buf), dev_buf, sizeof(int32_t)};
        CHECK_HIXL(hixl_engine.TransferSync(remote_engine, READ, {xfer}));
        printf("after READ: %d\n", *host_buf);
        
        // 单边写：向对端Server的MEM_DEVICE写本地预设的Host内存2。
        *host_buf = 2;
        CHECK_HIXL(hixl_engine.TransferSync(remote_engine, WRITE, {xfer}));
        ```

    - Server侧：

        ```cpp
        // 在Client完成单边写之后，Server侧将Device上该值读回Host，校验Client WRITE后应为2。
        int32_t host_val = 0;
        CHECK_ACL(aclrtMemcpy(&host_val, sizeof(int32_t), dev_buf, sizeof(int32_t), ACL_MEMCPY_DEVICE_TO_HOST));
        printf("after transfer: %d\n", host_val);
        ```

4. 在Client侧释放链路。

    ```cpp
    CHECK_HIXL(hixl_engine.Disconnect(remote_engine));
    ```

5. 在Client侧和Server侧分别内存解注册、释放内存并销毁HIXL引擎，最后与设备解绑。
    - Client侧：

        ```cpp
        CHECK_HIXL(hixl_engine.DeregisterMem(handle));
        CHECK_ACL(aclrtFreeHost(host_buf));
        hixl_engine.Finalize();
        CHECK_ACL(aclrtResetDevice(device));
        ```

    - Server侧：

        ```cpp
        CHECK_HIXL(hixl_engine.DeregisterMem(handle));
        CHECK_ACL(aclrtFree(dev_buf));
        hixl_engine.Finalize();
        CHECK_ACL(aclrtResetDevice(device));
        ```
