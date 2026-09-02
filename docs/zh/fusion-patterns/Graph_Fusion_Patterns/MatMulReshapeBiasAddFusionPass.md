# MatMulReshapeBiasAddFusionPass  

## 融合模式

该融合规则对MatMul算子的输出做了Reshape处理，并对Reshape输出进行BiasAdd/Add处理。

![](../figures/MatMulReshapeBiasAddFusionPass_1.png)

## 使用约束

- MatMul/MatMulV2仅支持两个输入。
- BiasAdd/Add的输入必须是一个Bias和一个Reshape的输出。
- Reshape节点无法拆分MatMul节点输出的尾轴。
- BiasAdd/Add的shape为MatMul节点输出的尾轴。
- 仅在静态图模式生效。

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
