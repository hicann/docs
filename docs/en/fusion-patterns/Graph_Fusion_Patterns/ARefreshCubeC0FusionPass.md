# ARefreshCubeC0FusionPass

## Description

Corrects the c0 value of cube operators when their inputs and outputs use heavy (private) formats.

## Constraints

- Cube operators include AvgPool, AvgPoolV2, BatchMatMulV2, Conv2D, Conv2DTransposeD, Conv3D, Deconvolution, DepthwiseConv2D, FullyConnection, MatMulV2, MaxPool, Pooling, and QuantBatchMatmulV3.
- The input and output data types are float before conversion.
- This fusion pattern cannot be disabled.

## Applicable Products

<!-- npu="910b" id1 -->
Atlas A2 training products/Atlas A2 inference products
<!-- end id1 -->
