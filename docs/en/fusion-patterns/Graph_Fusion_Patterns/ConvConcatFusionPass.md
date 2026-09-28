# ConvConcatFusionPass

## Description

Inserts a StridedWrite operator before a Concat operator. The inserted StridedWrite, instead of the Concat operator, will concatenate Conv2D memory to reduce the performance consumption caused by Concat computation.

Concat operators include ConcatD and ConcatV2D, and Conv2D operators include Conv2D and Conv2D_Compress.

<!-- npu="A3,910b,310b" id1 -->
The following models do not support StridedWrite, but the hardware can emulate equivalent StridedWrite behavior. ConvConcatFusionPass will still match these models.<br>
<!-- npu="910b" id2 -->
- Atlas A2 training products/Atlas A2 inference products<br>
<!-- end id2 -->
<!-- npu="A3" id3 -->
- Atlas A3 training products/Atlas A3 inference products<br>
<!-- end id3 -->
<!-- npu="310b" id4 -->
- Atlas 200I/500 A2 inference products
<!-- end id4 -->
<!-- end id1 -->

**When the subgraph does not contain Dequant or Quant, the following scenarios are involved:**

Scenario 1:

![](../figures/ConvConcatFusionPass_1.png)

Scenario 2:

![](../figures/ConvConcatFusionPass_2.png)

Scenario 3:

![](../figures/ConvConcatFusionPass_3.png)

Scenario 4:

![](../figures/ConvConcatFusionPass_4.png)

Scenario 5:

![](../figures/ConvConcatFusionPass_5.png)

Scenario 6: When cube and vector operations are not separated on AI Core, Mish fusion is not required.

![](../figures/ConvConcatFusionPass_6.png)

Scenario 7: When cube and vector operations are separated on AI Core, Mish fusion is required.

![](../figures/ConvConcatFusionPass_7.png)

**When the subgraph does not contain Dequant but contains Quant, the following scenarios are involved:**

Scenario 1:

![](../figures/ConvConcatFusionPass_8.png)

Scenario 2:

![](../figures/ConvConcatFusionPass_9.png)

Scenario 3:

![](../figures/ConvConcatFusionPass_10.png)

Scenario 4:

![](../figures/ConvConcatFusionPass_11.png)

Scenario 5:

![](../figures/ConvConcatFusionPass_12.png)

Scenario 6: When cube and vector operations are not separated on AI Core, the following scenarios are also involved:

![](../figures/ConvConcatFusionPass_13.png)

**When the subgraph contains Dequant but does not contain Quant, the following scenarios are involved:**

Scenario 1: When cube and vector operations are not separated on AI Core, Mish fusion is not required.

![](../figures/ConvConcatFusionPass_14.png)

Scenario 2: When cube and vector operations are separated on AI Core and at least one branch has a Mish operator, Mish fusion is required.

![](../figures/ConvConcatFusionPass_15.png)

**When the subgraph contains both Dequant and Quant, the following scenarios are involved regardless of whether cube and vector operations on AI Core are executed separately or not:**

![](../figures/ConvConcatFusionPass_16.png)

**When the subgraph contains both Dequant and Quant and cube and vector operations are not separated on AI Core, the following scenarios are involved:**

![](../figures/ConvConcatFusionPass_17.png)

## Constraints

- For quantization, the fusion pattern must be enabled. Otherwise, the output dtype of TransData is invalid.
- Dynamic shapes are not supported.
- This pass applies when all Concat inputs except the final one satisfy C axis alignment.
- Fusion of Quant and Mish operators is allowed when the Concat inputs have their C axis aligned with the data type. That is, the fusion takes effect when the Concat inputs meet any of the following conditions:
    - If the original dtype is fp16 or float, the value of dim C must be a multiple of 16.
    - If the original dtype is int8, the value of dim C must be a multiple of 32.
    - If the original dtype is int4, the value of dim C must be a multiple of 64.

- If the concat input branch contains the Pooling and mish operators, the quant and mish operators are not fused.
- For details about the conditions for Requant to take effect, see [V100RequantFusionPass](V100RequantFusionPass.md) or [V200RequantFusionPass](V200RequantFusionPass.md).

## Applicable Products

<!-- npu="310b" id5 -->
Atlas 200I/500 A2 inference products
<!-- end id5 -->

<!-- npu="310p" id6 -->
Atlas inference products
<!-- end id6 -->

<!-- npu="910" id7 -->
Atlas training products
<!-- end id7 -->

<!-- npu="910b" id8 -->
Atlas A2 training products/Atlas A2 inference products
<!-- end id8 -->

<!-- npu="A3" id9 -->
Atlas A3 training products/Atlas A3 inference products
<!-- end id9 -->
