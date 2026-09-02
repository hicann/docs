# ZConfusionSoftmaxGradFusionPass

## 融合模式

该融合将符合图融合pattern的Mul + ReduceSumD/ReduceSum（仅Ascend 950PR/Ascend 950DT支持） + Sub这几个小算子融合成ConfusionSoftmaxGrad算子。

![](../figures/ZConfusionSoftmaxGradFusionPass_1.png)

## 使用约束

- 动态shape场景，该融合规则不生效。
- 当Mul算子的两个输入shape不相同时，该融合规则不生效。
- 当Mul算子的input0输入与Sub算子的input0输入不是同一个节点时，该融合规则不生效。
- 当input0不是Sub的第一个输入参数时，该融合规则不生效。
- 当ReduceSumD/ReduceSum的属性axis不是其输入shape的尾轴索引时，该融合规则不生效。
- 当ReduceSumD/ReduceSum输入shape的尾轴大于30000时，该融合规则不生效。
- 数据类型不在融合后算子的支持范围内，该融合规则不生效。
- input0、input1的输入数据类型和数据格式保持一致。
- 在reduce轴为1且AReduceSumFusionPass融合规则开启时，当前融合规则不生效。
- Ascend 950PR/Ascend 950DT场景下，ReduceSum的属性keep\_dims为False时，当前融合规则不生效。
- Ascend 950PR/Ascend 950DT场景下，ReduceSum的输入axis不是const节点时，当前融合规则不生效。

## 支持的型号

<!-- npu="910b" id3 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id3 -->

<!-- npu="950" id2 -->
Ascend 950PR/Ascend 950DT
<!-- end id2 -->
