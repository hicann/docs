# MatMulGelugradUbFusion

## Description

Performs UB fusion on MatMul/GEMM and Elemwise in a subgraph that meets the following pattern.

![](../figures/MatMulGelugradUbFusion_1.png)

## Constraints

- Dynamic scenarios are not supported.
- Elemwise does not support TanhGrad.

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
