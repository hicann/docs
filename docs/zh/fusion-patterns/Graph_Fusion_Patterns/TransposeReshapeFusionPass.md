# TransposeReshapeFusionPass

## 融合模式

该融合将符合图融合pattern的TransposeD+Reshape算子，融合成ConfusionTransposeD算子。

![](../figures/TransposeReshapeFusionPass_1.png)

## 使用约束

- 当TransposeD的输入shape为空或者Reshape的输出shape为空时，该融合规则不生效。
- 当TransposeD的输入为动态shape或者Reshape的输出为动态shape时，该融合规则不生效。
- 当Reshape的输出shape为1维，且不能整除16时，该融合规则不生效。
- 当Reshape的输出shape维度大于等于2，且shape的最后两维至少有一个不能整除16时，该融合规则不生效。
- 当TransposeD的输入shape为1维，且不能整除16时，该融合规则不生效。
- 当TransposeD的输入shape维度大于等于2，且shape的最后两维至少有一个不能整除16时，该融合规则不生效。
- 数据类型不在融合后算子的支持范围内，该融合规则不生效。

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->
