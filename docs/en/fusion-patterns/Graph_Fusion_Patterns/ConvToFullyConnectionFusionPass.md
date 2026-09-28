# ConvToFullyConnectionFusionPass

## Description

Fuses the Conv operator into the FullyConnection operator to improve computing performance.
![](../figures/ConvToFullyConnectionFusionPass_1.png) After: ![](../figures/ConvToFullyConnectionFusionPass_2.png)

## Constraints

- Dynamic shapes are not supported.
- The int4 and int8 data types are not supported.
<!-- npu="910b" id1 -->
- For Atlas A2 training products/Atlas A2 inference products, Float32 does not support filters whose N axis is not aligned to 16.
<!-- end id1 -->
- The number of conv2d output nodes must be 1. The input size must be the same as the HWC axis of the filter size. The value of the group attribute must be 1. The value of the pad attribute must be `[0,0,0,0]`.
- The conv2d operator cannot be followed by the quant or requant operator.
- The conv2d operator cannot be cascaded with dequant+sigmoid.

## Applicable Products

<!-- npu="310b" id2 -->
Atlas 200I/500 A2 inference products
<!-- end id2 -->

<!-- npu="310p" id3 -->
Atlas inference products
<!-- end id3 -->

<!-- npu="910" id4 -->
Atlas training products
<!-- end id4 -->

<!-- npu="910b" id5 -->
Atlas A2 training products/Atlas A2 inference products
<!-- end id5 -->

<!-- npu="A3" id6 -->
Atlas A3 training products/Atlas A3 inference products
<!-- end id6 -->
