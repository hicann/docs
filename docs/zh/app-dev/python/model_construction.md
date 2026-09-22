# 模型构建

对于开源框架的网络模型（如Caffe、TensorFlow等），不能直接在AI处理器上做推理，需要先使用ATC（Ascend Tensor Compiler）工具将开源框架的网络模型转换为适配AI处理器的离线模型（\*.om文件）。

此处以ONNX框架的ResNet-50网络为例，说明如何使用ATC工具进行模型转换，详细说明请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)。

1. 以运行用户登录开发环境。
2. 执行模型转换。

    执行以下命令，将原始模型转换为AI处理器能识别的\*.om模型文件。请注意，执行命令的用户需具有命令中相关路径的可读、可写权限。以下命令中的“_**<SAMPLE\_DIR\>**_”请根据实际样例包的存放目录替换。_**“<soc\_version\>”**_请根据实际AI处理器的版本进行替换。

    ```bash
    cd <SAMPLE_DIR>/MyFirstApp_ONNX/model
    wget https://obs-9be7.obs.cn-east-2.myhuaweicloud.com/003_Atc_Models/resnet50/resnet50.onnx
    atc --model=resnet50.onnx --framework=5 --output=resnet50 --input_shape="actual_input_1:1,3,224,224"  --soc_version=<soc_version>
    ```

    各参数的解释如下，详细约束说明请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)。

    - --model：ResNet-50网络的模型文件的路径。
    - --framework：原始框架类型。5表示ONNX。
    - --output：resnet50.om模型文件的路径。请注意，记录保存该om模型文件的路径，后续开发应用时需要使用。
    - --input\_shape：模型输入数据的shape。
    - --soc\_version：AI处理器的版本。

        >[!NOTE]
        >如果无法确定当前设备的soc\_version，可按如下方法查询：
        >- 针对如下产品：在安装AI处理器的服务器执行**npu-smi info**命令进行查询，获取**Name**信息。实际配置值为AscendName，例如**Name**取值为_xxxyy_，实际配置值为Ascend_xxxyy_。
        > Atlas A2系列产品
        > Atlas 200I/500 A2推理产品
        > Atlas 推理系列产品
        > Atlas 训练系列产品
        >- 针对Atlas A3系列产品，在安装AI处理器的服务器执行**npu-smi info -t board -i** _id_ **-c** _chip\_id_命令进行查询，获取**Chip Name**和**NPU Name**信息，实际配置值为Chip Name\_NPU Name。例如**Chip Name**取值为Ascend_xxx_，**NPU Name**取值为1234，实际配置值为Ascend_xxx__\__1234。其中：
            >- id：设备id，通过**npu-smi info -l**命令查出的NPU ID即为设备id。
            >- chip\_id：芯片id，通过**npu-smi info -m**命令查出的Chip ID即为芯片id。
            >- 针对Ascend 950PR&950DT系列产品，在安装AI处理器的服务器执行**npu-smi info -t board -i** _id_命令进行查询，获取**Chip Name**和**NPU Name**信息，实际配置值为Chip Name\_NPU Name。例如**Chip Name**取值为Ascend_xxx_，**NPU Name**取值为1234，实际配置值为Ascend_xxx__\__1234。
            > 其中，id为设备id，通过**npu-smi info -l**命令查出的NPU ID即为设备id。

>[!NOTE]
> 
>- 如果模型转换时，提示有不支持的算子，请先参见[《Ascend C算子开发指南》](https://hiascend.com/document/redirect/CannCommunityOpdevAscendC)s先完成自定义算子，再重新转换模型。
>- 如果模型转换时，提示有算子编译相关问题，但根据报错信息无法定位问题、需要联系技术支持时（您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。），则需设置DUMP\_GE\_GRAPH、DUMP\_GRAPH\_LEVEL环境变量，再重新模型转换，收集模型转换过程中各个阶段的图描述信息。关于环境变量以及图描述信息的说明，请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)中的““参考 \> dump图详细信息””。
>- 如果模型的输入Shape是动态，关于模型构建、模型推理的说明请参见[模型动态Shape输入推理](dynamic_shape_model_inference.md)。
>- 如果现有网络不满足您的需求，您可以使用AI处理器支持的算子、调用构图接口自行构建自己的网络，再编译成om离线模型文件。详细说明请参见《图开发》。
