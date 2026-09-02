# ConvFormatRefreshFusionPass

## 融合模式

针对如下图中的结构时，将卷积算子Input1的shape和format配置为输出的shape和format。

![](../figures/ConvFormatRefreshFusionPas_1.png)

## 使用约束

满足以下条件时，融合规则生效：

- Input1原始format和输出原始format一致，或者Input1原始shape维度和输出原始shape维度一致。
- 如果输出格式为5HD且存在C0值，需要卷积的Input1的C0值与输出的保持一致。
- 当Input1和输出格式不相等时，输出格式仅支持NCHW、NHWC、HWCN、CHWN、NC1HWC0。

## 支持的型号

<!-- npu="310b" id1 -->
Atlas 200I/500 A2 推理产品
<!-- end id1 -->

<!-- npu="310p" id2 -->
Atlas 推理系列产品
<!-- end id2 -->

<!-- npu="910" id3 -->
Atlas 训练系列产品
<!-- end id3 -->

<!-- npu="910b" id4 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id4 -->

<!-- npu="A3" id5 -->
Atlas A3 训练系列产品/Atlas A3 推理系列产品
<!-- end id5 -->

<!-- npu="950" id6 -->
Ascend 950PR/Ascend 950DT
<!-- end id6 -->
