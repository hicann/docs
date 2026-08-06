# ForeachSqrt

```c
REG_OP(ForeachSqrt)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OP_END_FACTORY_REG(ForeachSqrt)
```

## Brief

Apply sqrt operation for each tensor in a tensor list in manner of element-wise

## Inputs

One inputs:
x: A tensor list containing multiple tensors. Format supports ND. The type support float16, float, bfloat16.
Maximum length of x is 50.

## Outputs

y: A tensor list which store the tensors whose value are the sqrt value of the x. Format supports ND.
The type support float16, float, bfloat16 and is consistent with x. Maximum length of y is 50.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
