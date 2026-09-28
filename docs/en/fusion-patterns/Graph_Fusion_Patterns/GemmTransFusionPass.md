# GemmTransFusionPass

## Description

Fuses the Transpose+Gemm operators into the GemmTrans operator.

![](../figures/GemmTransFusionPass_1.png)

After:

![](../figures/GemmTransFusionPass_2.png)

## Constraints

The input format of Transpose must be ND, and non-alignment scenarios are not supported.

## Applicable Products

<!-- npu="310b" id1 -->
Atlas 200I/500 A2 inference products
<!-- end id1 -->
