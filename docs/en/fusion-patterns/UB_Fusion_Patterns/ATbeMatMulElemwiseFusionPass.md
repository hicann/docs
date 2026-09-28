# ATbeMatMulElemwiseFusionPass

## Description

Performs UB fusion on MatMul/GEMM and Elemwise in the subgraphs that meet the following patterns.

![](../figures/ATbeMatMulElemwiseFusionPass_1.png)

Or

![](../figures/ATbeMatMulElemwiseFusionPass_2.png)

## Constraints

Dynamic shapes are not supported.

## Applicable Products

<!-- npu="310b" id1 -->
Atlas 200I/500 A2 inference products
<!-- end id1 -->

<!-- npu="310p" id2 -->
Atlas inference products
<!-- end id2 -->

<!-- npu="910" id3 -->
Atlas training products
<!-- end id3 -->
