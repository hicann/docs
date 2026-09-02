# TbeConv2DReluv2Pass

## 融合模式

该融合将Conv2D+ReluV2算子融合成1个Conv2D融合算子。

![](../figures/TbeConv2DReluv2Pass_1.png)

## 使用约束

- Conv2D的第一个输出output1的数据类型需要为float16。
- ReluV2的输出边要有两条。

## 支持的型号

<!-- npu="910" id1 -->
Atlas 训练系列产品
<!-- end id1 -->
