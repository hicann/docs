# TransposeSigmoidMulAddPowConcatFusionPass

## Description

Fuses the sigmoid structures of yolov3, yolov5, and yolov7 models which have no NMS postprocessing operator into one operator.

**Pattern 1**

![](../figures/TransposeSigmoidMulAddPowConcatFusionPass_1.png)

After:

![](../figures/TransposeSigmoidMulAddPowConcatFusionPass_4.png)

**Pattern 2**

![](../figures/TransposeSigmoidMulAddPowConcatFusionPass_3.png)

After:

![](../figures/TransposeSigmoidMulAddPowConcatFusionPass_4.png)

## Constraints

None

## Applicable Products

<!-- npu="310p" id1 -->
Atlas inference products
<!-- end id1 -->
