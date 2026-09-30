# 接口调用流程

开发应用时，如果涉及执行单个算子，则应用程序中必须包含执行单个算子的代码逻辑。关于执行单个算子的接口调用流程，请先参见[接口调用流程](interface_calling_process.md)了解整体流程，再查看本节中的流程说明。

系统支持的算子请参见《算子库》。

对于系统不支持的算子，用户需先参见[《Ascend C算子开发指南》](https://hiascend.com/document/redirect/CannCommunityOpdevAscendC)完成自定义算子开发。

**图 1**  算子调用流程
![](figures/operator_invoke_process.png "算子调用流程")

关键接口的说明如下：

1. 加载算子模型文件。

    支持以下2种方式中的一种加载单算子模型文件：

    - 调用`acl.op.set_model_dir`接口，设置加载模型文件的目录，目录下存放单算子模型文件（\*.om文件）。
    - 调用`acl.op.load`接口，从内存中加载单算子模型数据，由用户管理内存。单算子模型数据是指“单算子编译成\*.om文件后，再将om文件读取到内存中”的数据。

2. 调用`acl.rt.malloc`接口申请Device上的内存，存放执行算子的输入、输出数据。

    如果需要将Host上数据传输到Device，则需要调用`acl.rt.memcpy`接口（同步接口）或`acl.rt.memcpy_async`接口（异步接口）通过内存复制的方式实现数据传输。

3. 动态Shape场景，如果无法明确算子的输出Shape时，在执行算子前，还需推导或预估算子的输出Shape。

    需用户调用`acl.op.infer_shape`接口、`acl.get_tensor_desc_num_dims`接口、`acl.get_tensor_desc_dim_v2`接口、`acl.get_tensor_desc_dim_range`等接口，推导或预估算子的输出Shape，作为算子执行接口`acl.op.execute_v2`的输入。

4. 执行算子。

    - 对于被封装成pyacl接口的算子（参见[调用CBLAS接口](calling_cblas_interface.md)），包括GEMM算子、Cast算子，目前支持以下两种执行方式：
        - 不以handle方式执行算子，接口名称中不包含“Handle”关键字，例如，调用`acl.blas.gemm_ex`接口（封装GEMM算子）、`acl.op.cast`接口（封装Cast算子）等执行算子。
        - 以handle方式执行算子，接口名称中包含“Handle”关键字，例如，调用`acl.blas.create_handle_for_gemm_ex`接口、`acl.op.create_handle_for_cast`接口等创建handle后，还需要调用`acl.op.execute_with_handle`接口执行算子。

    - 对于未被封装成pyacl接口的算子，目前执行以下两种执行方式：
        - 不以handle方式执行算子，调用`acl.op.execute_v2`接口执行算子。
        - 以handle方式执行算子，调用`acl.op.create_handle`接口创建handle，再调用`acl.op.execute_with_handle`接口执行算子。

    >[!NOTE]
    >- 不以handle方式执行算子时，每次执行算子时，系统内部都会根据算子描述信息匹配内存中的模型。
    >- 以handle方式执行算子时，系统内部将算子描述信息匹配到内存中的模型，并缓存在Handle中，每次执行算子时，无需重复匹配算子与模型，因此在涉及多次执行同一个算子时，效率更高。但Handle使用结束后，需调用`acl.op.destroy_handle`接口释放。

5. 调用`acl.rt.synchronize_stream`接口阻塞应用运行，直到指定Stream中的所有任务都完成。
6. 调用`acl.rt.free`接口释放内存。

    如果需要将Device上的算子执行结果数据传输到Host，则需要调用`acl.rt.memcpy`接口（同步接口）或`acl.rt.memcpy_async`接口（异步接口）通过内存复制的方式实现数据传输，然后再释放内存。
