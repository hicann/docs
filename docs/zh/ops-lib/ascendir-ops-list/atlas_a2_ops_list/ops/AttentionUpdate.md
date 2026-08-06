# AttentionUpdate

```c
REG_OP(AttentionUpdate)
    .DYNAMIC_INPUT(lse, TensorType({DT_FLOAT}))
    .DYNAMIC_INPUT(go, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(output, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(lse_m, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(update_type, Int)
    .REQUIRED_ATTR(sp, Int)
    .OP_END_FACTORY_REG(AttentionUpdate)
```

## Brief

Function AttentionUpdate.

## Inputs

Two inputs, including:
- lse: Tensor list. Type is float32. The input of lse.
- go: Tensor list. Type is float32, float16, bfloat16. The input of attentionout.

## Outputs

Two outputs, including:
- output: A tensor. Type is float32, float16, bfloat16.
- lse_m: A tensor. Type is float32.

## Attributes

Two attributes, including:
- update_type: An int. The update type, value is 0 or 1. 0 means the output of lse_m is invalid, 1 means valid.
- sp: An int. The sp num, value is [1..16].

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 lse: float32
- input1 go: bfloat16,float16,float32
- output0 output: bfloat16,float16,float32
- output1 lse_m: float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
