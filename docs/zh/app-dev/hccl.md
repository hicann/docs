# 集合通信

集合通信库HCCL（Huawei Collective Communication Library）是基于昇腾硬件的高性能集合通信库，为计算集群提供高性能、高可靠的通信方案。

>**说明：** 
>本节仅针对HCCL做简要介绍，关于HCCL的详细使用方法可参见《HCCL集合通信库》。

## 核心功能

- 提供单机、多机环境中的高性能集合通信和点对点通信。
- 支持AllReduce、Broadcast、AllGather、ReduceScatter、AlltoAll、Send、Receive等集合通信原语。
- 支持Ring、Mesh、Recursive Halving-Doubling（RHD）等通信算法。
- 支持HCCS、RoCE、PCIe、UB（Unified Bus）等高速通信链路。
- 支持单算子和图模式两种执行模式。
- 支持通信算子的自定义开发。

## 软件架构

HCCL是CANN的核心组件，为NPU集群提供高性能、高可靠性的通信方案。HCCL向上支持多种AI框架，向下实现多款昇腾AI处理器之间的高效互联，其架构如下图所示。

**图 1**  集合通信库软件架构图  
![](figures/HCCL_arch.png "集合通信库软件架构图")

HCCL包含HCCL集合通信库与HCOMM（Huawei Communication）通信基础库：

- **HCCL集合通信库**：包含内置通信算子和扩展通信算子，提供对外的通信算子接口。
    - 内置通信算子：HCCL提供的基础通信算子，包含集合通信算子和点对点通信算子。
    - 扩展通信算子：用户可以使用HCOMM通信基础库提供的接口自定义扩展通信算子。

- **HCOMM通信基础库**：采用分层解耦的设计思路，将通信能力划分为控制面和数据面两部分。

    - 控制面：提供拓扑信息查询与通信资源管理功能。
    - 数据面：提供本地操作、算子间同步、通信操作等数据搬运和计算功能。

    控制面提供通信资源，数据面提供操作资源的方法，提供的相关接口可以让通信算子开发人员聚焦于业务创新，而无需关注芯片底层复杂的实现细节。

## 快速体验

下面以AllReduce算子为例，介绍其在单算子执行模式下的使用方式，帮助用户快速体验集合通信功能。

- AllReduce算子介绍

    AllReduce操作是将通信域内所有节点的输入数据进行归约操作后（支持sum、prod、max、min），再把结果发送到所有节点的输出buffer。

    ![](figures/allreduce.png)

    注意：每个rank只能有一个输入。

- 样例介绍

    用户可以点击[Link](https://gitcode.com/cann/hcomm/tree/9.2.0-beta.2/examples/01_communicators/03_one_device_per_pthread)获取完整样例代码，该样例基于root节点信息创建通信域，在一个进程中管理一个AI Server，其中每个NPU设备由一个线程进行管理，主要包含以下功能点：

    1. 设备检测，通过aclrtGetDeviceCount\( \)接口查询可用设备数量。
    2. 将rank0作为root节点，通过HcclGetRootInfo\( \)接口生成root节点的rootInfo标识信息。
    3. 基于rootInfo，在每个线程中通过HcclCommInitRootInfo\( \)接口初始化通信域。
    4. 调用HcclAllReduce\(\) 接口，将通信域内所有rank的输入数据进行相加后，再把结果发送到所有节点，并打印结果。

- 编译运行

    在本样例代码目录下执行如下命令：

    ```bash
    make
    make test
    ```

- 结果解析

    每个rank的数据初始化为0\~7，经过AllReduce操作后，每个rank的结果是所有rank对应位置数据的和（8个rank的数据相加）。

    ```bash
    Found 8 NPU device(s) available
    rankId: 0, output: [ 0 8 16 24 32 40 48 56 ]
    rankId: 1, output: [ 0 8 16 24 32 40 48 56 ]
    rankId: 2, output: [ 0 8 16 24 32 40 48 56 ]
    rankId: 3, output: [ 0 8 16 24 32 40 48 56 ]
    rankId: 4, output: [ 0 8 16 24 32 40 48 56 ]
    rankId: 5, output: [ 0 8 16 24 32 40 48 56 ]
    rankId: 6, output: [ 0 8 16 24 32 40 48 56 ]
    rankId: 7, output: [ 0 8 16 24 32 40 48 56 ]
    ```
