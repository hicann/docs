# ZZConfusionTransposeNdFusionPass

## 融合模式

将静态场景下ND格式的ConfusionTransposeD替换为Transpose算子。

![](../figures/ZZConfusionTransposeNdFusionPass_1.png)

## 使用约束

- 输入输出的Format必须为ND格式。
- 只支持静态shape。
- 属性perm的值必须在\[0, 输入的rank\)之间。

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->
