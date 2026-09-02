# SoftmaxCrossEntropyWithLogitsPass

## 融合模式

该融合将符合图融合pattern的reshape+SoftmaxCrossEntropyWithLogits算子，融合后消除Reshape算子，仅保留SoftmaxCrossEntropyWithLogits算子。

![](../figures/SoftmaxCrossEntropyWithLogitsPass_1.png)

## 使用约束

- 输入、输出参数的shape约束：

    input0、input2、input4的shape必须是4D。

- 输入、输出参数的format约束：

    input0、input2的format必须是NHWC，C<131072。

- 输入参数的顺序约束：
  - input0、input2必须是Reshape的第一个输入。
  - SoftmaxCrossEntropyWithLogits的第一个输出必须是Reshape的第一个输入。

- 性能说明：

    融合规则在C=1的场景时，性能有提升。

    如果有性能劣化，考虑关闭该融合规则。

- 输入参数的数据类型约束：

    input0、input2的数据类型保持一致。

  <!-- npu="910b" id2 -->
  - Atlas A2 训练系列产品/Atlas A2 推理系列产品：数据类型支持FLOAT32、BFLOAT16。
  <!-- end id2 -->

## 支持的型号

<!-- npu="910b" id1 -->
Atlas A2 训练系列产品/Atlas A2 推理系列产品
<!-- end id1 -->
