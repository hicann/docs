# SoftmaxGradFusionPass

## 融合模式

该融合将符合图融合pattern的小算子融合成SoftmaxGrad算子。

- 场景一：

![](../figures/SoftmaxGradFusionPass_1.png)

- 场景二：

![](../figures/SoftmaxGradFusionPass_2.png)

## 使用约束

- Mul0和Mul1的第一个输入相同。
- ReduceSumD的输出节点只能有一个。
- 在reduce轴为1且AReduceSumFusionPass融合规则开启时，当前融合规则不生效。
- 在场景一子图中，
  - Mul0的第二个输入和Sub的第一个输入相同。
  - Mul0的输出节点只能有一个。
  - Sub的输出节点只能有一个。

- 在场景二子图中
  - Sub的第一个输入必须是Mul0的输出。
  - Mul0的输出节点只能有2个。
  - Mul1的输出节点只能有一个。

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->
