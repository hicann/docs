# 开发流程

**图 1**  开发流程
![](figures/single_operator_development_process.png "开发流程")

1. 准备环境。

    请参见[环境准备](environment_preparation.md)。

2. 创建代码目录。

    在开发应用前，您需要先创建目录，存放代码文件、脚本、测试图片数据、模型文件等。

3. 准备算子。

    使用ATC工具编译算子生成om模型文件。

    该种方式，需要先构造\*.json格式单算子描述文件（描述算子的输入、输出及属性等信息），借助ATC工具，将单算子描述文件编译成om模型文件，再分别调用pyacl接口加载om模型文件、执行算子。

    关于ATC工具的使用说明，请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)。

4. 开发应用。

    单算子调用的流程请参见[接口调用流程](single_operator_interface_calling_process.md)及相关的示例代码。

5. 运行应用，请参见[应用调试](app_debug.md)。
