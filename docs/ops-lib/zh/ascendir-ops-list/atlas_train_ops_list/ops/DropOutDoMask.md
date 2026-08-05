# DropOutDoMask

```c
REG_OP(DropOutDoMask)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(mask, TensorType({DT_UINT8, DT_UINT1}))
    .INPUT(keep_prob, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OP_END_FACTORY_REG(DropOutDoMask)
```

## Brief

Return "output" according to the algorithm of dropout_do_mask:  
 scale_x = x *(1 / keep_prob)  
 output = select(mask == 1, scale_x, 0)

## Inputs

Three inputs, including:
- x: A mutable Tensor. A ND tensor. Support 1D ~ 8D. Must be one of the following types:
    float16, float32, bfloat16 (bfloat16 only supported on Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component
and Atlas A3 Training Series Product/Atlas A3 Inference Series Product).
- mask: A mutable Tensor. A ND tensor. Must met all of the following rules:
    dtype of mask should be uint8 or uint1.
    if data type of mask is uint8, shape of mask should be 1D. value of shape should met the following algorithm:
    value = (size(x) + 128 - 1) // 128 * 128 // 8
    if data type of mask is uint1, shape of mask should be same to x.
- keep_prob: A mutable Tensor. A ND tensor. Must met all of the following rules:
    0 <= keep_prob <= 1
    shape of "keep_prob" should be (1,) or [1,].
    Has the same type as "x" . 

## Outputs

y: A mutable Tensor. A ND tensor. Support 1D ~ 8D. Has the same type, shape and format as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 mask: uint8
- input2 keep_prob: float16,float32
- output0 y: float16,float32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
