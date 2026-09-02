# AddRmsNormFusionGraphPass

## 融合模式

该融合将符合图融合pattern的Add算子和RmsNorm算子融合成融合算子AddRmsNorm，其中Add算子的输出作为RmsNorm算子的第一个输入。

![](../figures/AddRmsNormFusionGraphPass_1.png)

## 使用约束

- Add算子的输入X1和X2的shape/dtype要一致。
- format只支持ND。

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->

<!-- npu="A3" id2 -->
Atlas A3 训练系列产品/Atlas A3 推理系列产品
<!-- end id2 -->

<!-- npu="950" id3 -->
Ascend 950PR/Ascend 950DT
<!-- end id3 -->
