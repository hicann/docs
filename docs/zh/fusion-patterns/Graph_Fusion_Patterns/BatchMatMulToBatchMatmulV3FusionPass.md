# BatchMatMulToBatchMatmulV3FusionPass

## 融合模式

该融合将符合图融合pattern的BatchMatMulV2/BatchMatMul的算子转换为BatchMatMulV3算子。

![](../figures/BatchMatMulToBatchMatmulV3FusionPass_1.png)

## 支持的型号

<!-- npu="950" id1 -->
Ascend 950PR/Ascend 950DT
<!-- end id1 -->
