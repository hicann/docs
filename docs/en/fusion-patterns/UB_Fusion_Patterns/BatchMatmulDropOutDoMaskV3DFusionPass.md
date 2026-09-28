# BatchMatmulDropOutDoMaskV3DFusionPass

## Description

Performs UB fusion on BatchMatMul and DropOutDoMaskV3D/Add in a subgraph that meets the following pattern:

![](../figures/BatchMatmulDropOutDoMaskV3DFusionPass_1.png)

## Constraints

- Dynamic shapes are not supported.
- BatchMatMul and BatchMatMulV2 are supported.

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
