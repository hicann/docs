# TbeMultiOutputFusionPass

## Description

Performs UB fusion on the ElemWise nodes in the subgraphs that meet the following patterns.

The number in the parentheses indicates the value range of the number of ElemWise nodes. `head` indicates that the current node is the first node for matching.

![](../figures/TbeMultiOutputFusionPass_1.png)

Or

![](../figures/TbeMultiOutputFusionPass_2.png)

## Constraints

None
