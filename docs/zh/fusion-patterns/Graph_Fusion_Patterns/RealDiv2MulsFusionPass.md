# RealDiv2MulsFusionPass

## 融合模式

在RealDiv算子的第二个输入的数据类型为scalar时，该融合规则会将其转换为调用Muls算子，且第二个输入变为原输入的倒数。

![](../figures/RealDiv2MulsFusionPass_1.png)

## 使用约束

- x2输入的数据类型须为scalar或float32类型，且不能为tensor。
- x2的值需大于1e-6。

## 支持的型号

<!-- npu="310p" id1 -->
Atlas 推理系列产品
<!-- end id1 -->

<!-- npu="310b" id2 -->
Atlas 200I/500 A2 推理产品
<!-- end id2 -->

<!-- npu="910" id3 -->
Atlas 训练系列产品
<!-- end id3 -->

<!-- npu="910b" id4 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id4 -->
