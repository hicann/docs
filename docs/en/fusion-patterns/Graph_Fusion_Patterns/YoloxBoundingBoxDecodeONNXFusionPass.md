# YoloxBoundingBoxDecodeONNXFusionPass

## Description

Fuses the StridedSliceD, Mul, Exp, GatherV2, Add, Muls, Sub, Unsqueeze, and ConcatD operators into YoloxBoundingBoxDecode, to improve the computing performance.

![](../figures/YoloxBoundingBoxDecodeONNXFusionPass_1.png)

After:

![](../figures/YoloxBoundingBoxDecodeONNXFusionPass_2.png)

## Constraints

None

## Applicable Products

<!-- npu="310p" id1 -->
Atlas inference products
<!-- end id1 -->
