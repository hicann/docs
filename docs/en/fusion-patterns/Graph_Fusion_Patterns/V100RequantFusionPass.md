# V100RequantFusionPass

## Description

Optimizes the quantization nodes in inference tasks.

Inserts the RequantHostCpuOpV2 operator into the input of AscendDequant based on the following structures.

- **Scenario 1**

  ![](../figures/V100RequantFusionPass_01.png)

- **Scenario 2**

  ![](../figures/V100RequantFusionPass_02.png)

- **Scenario 3**

  ![](../figures/V100RequantFusionPass_03.png)

## Constraints

If there are multiple AscendDequant operators, the scale values of all AscendDequant operators must be the same.

## Applicable Products

<!-- npu="310p" id1 -->
Atlas inference products
<!-- end id1 -->
