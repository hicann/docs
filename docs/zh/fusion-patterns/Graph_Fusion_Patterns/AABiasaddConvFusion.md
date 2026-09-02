# AABiasaddConvFusion

## 融合模式

该融合规则将不包含Bias的Conv卷积算子和BiasAdd算子进行融合，融合为一个包含Bias输入的Conv卷积算子。

![](../figures/AABiasaddConvFusion_1.png)

## 使用约束

- 当卷积算子已经有Bias的时候，不支持融合。
- 不支持动态场景。
- 该融合规则不可关闭。

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

<!-- npu="950" id5 -->
Ascend 950PR/Ascend 950DT
<!-- end id5 -->
