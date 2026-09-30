# 配置精度模式

如果在模式转换时不指定网络模型或算子的精度模式，默认采用fp16（float16）数据类型进行计算。

配置模型高精度模式后推理，可提升精度，但可能会影响推理性能，如果在精度达标的同时，需要保持性能，则可以配置部分算子保持原始网络中的数据类型。

## 配置网络模型的高精度模式

1. 使用ATC工具转换模型时，增加高级参数--precision\_mode，用于指定精度模式。

    参数设置如下所示，表示如果网络模型中算子支持fp32（float32），则使用fp32；如果网络模型中算子不支持fp32，则使用fp16（float16）。

    ```bash
    --precision_mode=allow_fp32_to_fp16
    ```

    关于该参数的详细说明请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)中的“参数说明 \> 高级功能参数 \> 算子调优选项 \> --precision\_mode”。

2. 使用转换后的om模型重新推理。

## 配置部分算子保持原始网络中的数据类型

1. 使用ATC工具转换模型时，增加高级参数--keep\_dtype（指定部分算子计算时保持原始网络的数据类型）和--precision\_mode（指定网络模型的精度模式）。

    参数使用示例如下：

    ```bash
    --keep_dtype=$HOME/exceptionlist.cfg --precision_mode=force_fp16
    ```

    配置文件名举例为_exceptionlist.cfg_，配置文件样例如下，文件中每一行是一个算子的名称，将配置好的_exceptionlist.cfg_文件上传到ATC工具所在服务器任意目录：

    ```text
    Opname1 
    Opname2 
    …
    ```

    关于该参数的详细说明请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)中的“参数说明 \> 高级功能参数 \> 算子调优选项 \> --keep\_dtype”。

2. 使用转换后的om模型重新推理。
