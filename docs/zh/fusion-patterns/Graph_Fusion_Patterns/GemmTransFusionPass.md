# GemmTransFusionPass

## 融合模式

该融合规则将Transpose+Gemm算子融合为GemmTrans算子。

![](../figures/GemmTransFusionPass_1.png)

融合成

![](../figures/GemmTransFusionPass_2.png)

## 使用约束

Transpose输入format需为ND且不能为非对齐场景。

## 支持的型号

<!-- npu="310b" id1 -->
Atlas 200I/500 A2 推理产品
<!-- end id1 -->
