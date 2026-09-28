# DepthwiseDfFusionPass

## Description

Adds the TransposeD operator before the DepthwiseConv2DbackpropInput convolution operator to improve computing performance.

Before: ![](../figures/DepthwiseDfFusionPass_1.png) After:

![](../figures/DepthwiseDfFusionPass_2.png)

## Constraints

This fusion takes effect only when the filter format is NCHW.
