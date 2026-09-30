# 检查数据处理或配置

1. 检查om模型与标杆网络推理的输入数据以及输入数据的处理是否一致，如果不一致，需调整成一致。
2. 检查AIPP配置。

    AIPP（Artificial Intelligence Pre-Processing），用于在AI Core上完成图像预处理，包括改变图像尺寸、色域转换（转换图像格式）、减均值/乘系数（改变图像像素），数据处理之后再进行真正的模型推理。

    如果AIPP配置错误可能导致模型推理的输入数据不准确，需要参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)中的“高级功能 \> 开启AIPP”章节检查AIPP配置，如有不正确的AIPP配置，修改正确后，重新转换模型，再重新推理。

3. 检查om模型与标杆网络推理结果的后处理方式是否一致，如果不一致，需调整成一致。
