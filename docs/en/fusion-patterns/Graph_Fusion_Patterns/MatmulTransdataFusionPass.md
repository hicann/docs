# MatmulTransdataFusionPass

## Description

Reduces the number of Transdata operators in the graph from 2 to 1 through equivalent replacement.

![](../figures/MatmulTransdataFusionPass_1.png)

After:

![](../figures/MatmulTransdataFusionPass_2.png)

When the Cast operator is absent:

![](../figures/MatmulTransdataFusionPass_3.png)

After:

![](../figures/MatmulTransdataFusionPass_4.png)

## Constraints

None
