# DropOutDoMaskV3

```c
REG_OP(DropOutDoMaskV3)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(mask, TensorType({DT_UINT8, DT_BOOL}))
    .INPUT(keep_prob, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OP_END_FACTORY_REG(DropOutDoMaskV3)
```

## Brief

Return "output" according to the algorithm of dropout_do_mask_v3:  
 scale_x = x *(1 / keep_prob)  
 output = select(mask == 1, scale_x, 0)  

## Inputs

Three inputs, including:
- x: A mutable Tensor. A ND tensor. Support 1D ~ 8D. Must be one of the following types:
    float16, float32, bfloat16.
- mask: A mutable Tensor. A ND tensor. Must met all of the following rules:
    shape of mask should be 1D.
    dtype of mask should be uint8 or bool.
    value of shape should met the following algorithm:
    value = value = ((size(x) + 127) / 128) * 128 / 8.
- keep_prob: A mutable Tensor.Must met all of the following rules:
    shape of "keep_prob" should be (1,).
    Has the same type as "x" . 

## Outputs

y: A mutable Tensor. Has the same type, shape and format as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 mask: uint8
- input2 keep_prob: float16,float32
- output0 y: float16,float32


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
