# TbeEltwiseQuantFusionPass

## Description

Performs UB fusion on the ElemWise/Broadcast and quant nodes in the subgraphs that meet the following patterns.

![](../figures/TbeEltwiseQuantFusionPass_01.png)

Or

![](../figures/TbeEltwiseQuantFusionPass_02.png)

Or

![](../figures/TbeEltwiseQuantFusionPass_03.png)

## Constraints

- In an ElemWise/Broadcast+ElemWise/Broadcast+Quant use case, a maximum of five ElemWise/Broadcast nodes are supported.
- Dynamic shapes are not supported.
