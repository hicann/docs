# Conv2DbpInputBiasAddFusionPass

## Description

Fuses the Conv2DBackpropInput and BiasAdd operators into the Conv2DTransposeD operator.

![](../figures/Conv2DbpInputBiasAddFusionPass_1.png)

After:

![](../figures/Conv2DbpInputBiasAddFusionPass_2.png)

## Constraints

None
