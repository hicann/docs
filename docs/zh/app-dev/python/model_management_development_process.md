# 开发流程

**图 1**  开发流程
![](figures/model_management_development_process.png "开发流程-2")

1. 准备环境，包括开发环境和运行环境。
2. 创建代码目录。

    在开发应用前，您需要先创建目录，存放代码文件、测试图片数据、模型文件等。如下仅是示例，可参考：

    ```text
    ├App名称
    ├── caffe_model      # 该目录下存放模型转换相关的配置文件、模型文件。
    │   ├── xxx.cfg
    │   ├── xxx.prototxt
    ├── data
    │   ├── xxx.jpg     # 测试数据。
    │
    ├── model
    │   ├── xxx.om      # 转换后的模型文件。
    │
    ├── xxx.py           # python脚本。
    ├── xxx.py
    ```

3. 开发应用。
    1. 初始化，请参见[初始化与去初始化](initialization_and_deinitialization.md)。

        使用pyacl接口开发应用时，必须先调用`acl.init`接口进行初始化，否则可能会导致后续系统内部资源初始化出错，进而导致其它业务异常。

    2. 运行时资源申请，请参见[运行时资源申请与释放](runtime_resource_allocation_and_release.md)。
    3. 数据传输。
    4. 执行模型推理。请参见[模型管理](model_management.md)。

        模型推理结束后，需及时释放相关资源。

        若需要处理模型推理的结果，还需要进行数据后处理，例如对于图片分类应用，通过数据后处理从推理结果中查找最大置信度的类别标识。

    5. 所有数据处理结束后，需及时释放运行时资源，请参见[运行时资源申请与释放](runtime_resource_allocation_and_release.md)。
    6. 执行去初始化，请参见[初始化与去初始化](initialization_and_deinitialization.md)。

4. 运行应用，包括模型转换、运行应用脚本，请参见[应用调试](app_debug.md)。
