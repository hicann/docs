# TbeEltwiseCastFusionPass

## Description

Fuses the Elemwise and Cast operators in the following four scenarios:

Scenario 1:

![](../figures/TbeEltwiseCastFusionPass_1.png)

Scenario 2:

![](../figures/TbeEltwiseCastFusionPass_2.png)

Scenario 3

![](../figures/TbeEltwiseCastFusionPass_3.png)

Scenario 4:

![](../figures/TbeEltwiseCastFusionPass_4.png)

## Constraints

- The Cast operator must be float16-to-float32 or float32-to-float16.
- The Elemwise operator type can be "Relu", "Add", "Mul", or "Sqrt".
- The `other` operator can be matched only. It cannot be involved in the fusion.
- Dynamic shapes are not supported.
