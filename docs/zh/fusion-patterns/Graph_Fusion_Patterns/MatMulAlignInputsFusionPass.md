# MatMulAlignInputsFusionPass

## 融合模式

当matmul算子输入shape内轴非512B对齐时，MTE效率较低，性能表现较差。该图融合就是将matmul的输入shape进行对齐，解决性能问题。

![](../figures/MatMulAlignInputsFusionPass_1.png)

## 使用约束

仅适用于静态场景，且输入DType为Float32，输入不带bias。

非普通融合，仅对个别情况做此融合

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->

<!-- npu="A3" id2 -->
Atlas A3 训练系列产品/Atlas A3 推理系列产品
<!-- end id2 -->
