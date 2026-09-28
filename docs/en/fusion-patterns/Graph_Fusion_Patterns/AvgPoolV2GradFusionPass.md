# AvgPoolV2GradFusionPass

Changes the AvgPoolV2Grad operator into the AvgPoolV2GradD operator.

![](../figures/AvgPoolV2GradFusionPass_1.png)

## Constraints

The input `ori_input_shape` of AvgPoolV2Grad must be a const node or a data node with a value.
