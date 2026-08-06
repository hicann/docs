# 模型编译

以运行用户登录开发环境。使用ATC工具将开源框架的网络模型（如ONNX、TensorFlow等）编译成\*.om模型文件。

此处以转换ONNX模型为例给出命令示例，执行命令的用户需具有命令中相关路径的可读、可写权限。

```bash
atc --model=$HOME/module/resnet50*.onnx --framework=5 --output=$HOME/module/out/onnx_resnet50 --soc_version=<soc_version> 
```

各参数的解释如下，详细取值说明及约束说明请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)。

- --model：ResNet-50网络的模型文件的路径。
- --framework：原始框架类型。5表示ONNX。
- --output：resnet50.om模型文件的路径。请注意，记录保存该om模型文件的路径，后续开发应用时需要使用。
- --soc\_version：AI处理器的版本。_<soc\_version\>_请根据实际情况替换。

**注意事项：**

<!-- npu="950,A3,910b,910,310p,310b" id1 -->
- 如果模型转换时，提示有不支持的算子，请先参见[《Ascend C算子开发指南》](https://hiascend.com/document/redirect/CannCommunityOpdevAscendC)完成自定义算子开发，再重新编译模型。
<!-- end id1 -->
- 如果模型转换时，提示有算子编译相关问题，但根据报错信息无法定位问题、需要联系技术支持时（您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。），则需设置DUMP\_GE\_GRAPH、DUMP\_GRAPH\_LEVEL环境变量，再重新转换模型，收集模型转换过程中各个阶段的图描述信息。关于环境变量以及图描述信息的说明，请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)中的“参考 \> dump图详细信息”。
