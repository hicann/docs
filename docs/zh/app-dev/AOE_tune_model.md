# 使用AOE工具调优模型

本节介绍**推理**场景下使用**aoe命令**进行子图调优、算子调优的基本方法。**在调优前**，您需要先参见[《AOE调优工具》](https://hiascend.com/document/redirect/CannCommunityToolAoe)准备好环境、了解使用约束以及基本的参数使用方法。

使用aoe命令调优时，会生成：适配AI处理器的om模型文件、基于AI处理器的调优知识库、调优效果文件（通过效果文件可查阅模型中各算子的性能提升率）。由于生成om模型文件，所以aoe命令是包含模型转换的功能，因此aoe命令的参数，一般来说，是在atc命令参数的基础上增加了**--job\_type**参数，增加**子图调优**、**算子调优**的功能。**一般建议先进行子图调优，再进行算子调优**，原因是：先进行子图调优会生成图的切分方式，子图调优后算子已经被切分成最终的shape了，再进行算子调优，会基于这个最终shape去做算子调优。如果优先算子调优，这时调优的算子shape不是最终切分后的算子shape，可能会影响最终的调优效果。

## 操作步骤

<a id="li621122115138"></a>

1. **使用aoe命令依次执行子图调优、算子调优**。
    - **子图调优命令示例如下所示**：

        ```bash
        aoe --model=${HOME}/module/resnet50_pytorch_1.4.onnx --framework=5 --job_type=1
        ```

    - **算子调优命令示例如下所示**：

        ```bash
        aoe --model=${HOME}/module/resnet50_pytorch_1.4.onnx --framework=5 --job_type=2
        ```

2. **查看调优结果**。

    执行调优结果如下所示，代表调优完成并且性能有提升。调优后，同时生成自定义知识库、om模型文件以及调优效果文件。

    ```bash
    <xxxx> process finished. Performance improved by xx%    //xxxx：调优任务名称,xx%：性能提升的比例。
    ```

    **调优结果文件如下：**

    - **基于AI处理器的调优知识库**
        - 针对子图调优，默认存储到$\{HOME\}/Ascend/latest/data/aoe/custom/graph/$\{soc\_version\}目录下。
        - 针对算子调优，默认存储到$\{HOME\}/Ascend/latest/data/aoe/custom/op/$\{soc\_version\}路径下。

    - **适配AI处理器的om模型文件**

        调优后的om模型默认存放在执行aoe命令的当前目录下，具体路径如下：$\{model\_name\}\_$\{timestamp\}/tunespace/result/$\{model\_name\}\_$\{timestamp\}\_tune.om（或者$\{model\_name\}\_$\{timestamp\}\_tune_\__$\{os\}\_$\{arch\}.om）。

    - **调优效果文件**

        执行aoe命令的当前目录下生成命名为“aoe\_result\_opat\_\{timestamp\}\_\{pid_xxx_\}.json”的文件，记录调优过程中被调优的算子信息。

        json文件中的内容片段示例如下：

        ```json
        {
                  "op_name": "Conv_125",
                  "op_type": "Conv2D",
                  "tune_performance": {
                    "Schedule": {
                      "performance_after_tune(us)": 72.046,
                      "performance_before_tune(us)": 72.055,
                      "performance_improvement": "0.01%",
                      "update_mode": "add"
                    }
                  }
        }
        ```

3. **指定调优知识库，再执行模型推理**。
    1. 设置TUNE\_BANK\_PATH环境变量，指定为AOE调优后的自定义知识库存放路径，该路径下的graph目录下为子图调优知识库、op目录下为算子调优知识库。示例如下：

        ```bash
        export TUNE_BANK_PATH=/home/HwHiAiUser/custom
        ```

    2. 模型推理。

        使用[1](#li621122115138)中执行算子调优命令生成的om模型文件，执行模型推理。

        >**说明：** 
        >**支持“一次AOE调优+多次ATC模型转换”的场景**，使用AOE工具调优模型后，若由于其它业务需求需要重新转换模型，可通过环境变量指定AOE调优知识库的路径，再使用ATC工具重新转换模型，这样就可以基于知识库中的调优策略编译模型、转换出调优后的模型。
