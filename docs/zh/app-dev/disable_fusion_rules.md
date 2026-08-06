# 关闭融合规则

如果在模型转换时不指定关闭融合规则，当前默认开启融合规则，开启融合规则可提高计算效率、提升性能，但算子之间可能会融合，融合后的部分算子在实现上可能存在未考虑的场景，导致影响精度，因此在出现精度问题时可以尝试关闭融合规则。

如果关闭融合规则功能后，精度达标，则还是需要识别出问题算子，反馈给技术支持进一步分析、解决算子问题，解决算子问题后，建议保持开启融合规则功能。您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。

1. 使用ATC工具转换模型时，增加高级参数：--fusion\_switch\_file

    参数使用示例如下：

    ```bash
    --fusion_switch_file=$HOME/module/fusion_switch.cfg
    ```

    配置文件名举例为_fusion\_switch.cfg_，配置文件样例如下，将配置好的_fusion\_switch.cfg_文件上传到ATC工具所在服务器任意目录：

    ```json
    {
        "Switch":{
            "GraphFusion":{
                "ALL":"off"
            },
            "UBFusion":{
                "ALL":"off"
             }
        }
    }
    ```

    关于该参数的详细说明请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)中的“参数说明 \> 高级功能参数 \> 模型调优选项 \> --fusion\_switch\_file”。

2. 使用转换后的om模型重新推理。

>**说明：** 
>在联系技术支持前，设置DUMP\_GE\_GRAPH、DUMP\_GRAPH\_LEVEL环境变量，重新模型转换，打印模型转换过程中各个阶段的图描述信息。关于环境变量以及图描述信息的说明，请参见《ATC离线模型编译工具》中的“参考 \> dump图详细信息”。
