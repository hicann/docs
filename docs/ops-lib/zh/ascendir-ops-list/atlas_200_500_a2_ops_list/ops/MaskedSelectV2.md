# MaskedSelectV2

```c
REG_OP(MaskedSelectV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(mask, TensorType({DT_BOOL}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OP_END_FACTORY_REG(MaskedSelectV2)
```

## Brief

Choose the value of X with value according to mask.

## Inputs

two inputs, including:
 @li x: A Tensor of dtype is float16 or float32.
 @li mask: A Tensor of dtype is bool. 

## Outputs

y: A tensor with the same type as x. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 mask: bool
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the Numpy operator select.
Replaces the pytorch operator masked_select in some scenarios.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
