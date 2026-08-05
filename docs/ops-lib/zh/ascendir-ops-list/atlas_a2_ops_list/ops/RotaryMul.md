# RotaryMul

```c
REG_OP(RotaryMul)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .INPUT(r1, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .INPUT(r2, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BFLOAT16}))
    .OP_END_FACTORY_REG(RotaryMul)
```

## Brief

Apply rotary position embedding.

## Inputs

- x: A 4-dimensions tensor with layout BNSD, BSND or SBND, where B, N < 1000 and D is multiples of 64.
Must be one of the following types: float16, float32, bfloat16.
- r1: A 4-dimensions tensor with layout 11SD/B1SD/BNSD, 1S1D/BS1D/BSND or S11D/SB1D/SBND. When r1 broadcasts to x,
the product of the broadcast axes needs to be less than 1024. The dtype must be same as "x".
- r2: A 4-dimensions tensor. Has the same shpae and dtype as "r1".

## Outputs

y: A Tensor. Has the same shape and dtype as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 r1: bfloat16,float16,float32
- input2 r2: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
