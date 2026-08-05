# FatreluMul

```c
REG_OP(FatreluMul)
        .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
        .INPUT(threshold, TensorType({DT_FLOAT, DT_FLOAT, DT_FLOAT}))
        .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
        .OP_END_FACTORY_REG(FatreluMul)
```

## Brief

FatreluMul divides the input tensor into left and right tensors x1 and x2 based on the last dimension,
performs Threshold calculation on x1 on the left, and multiplies the calculation result by x2. 

## Inputs

- x: A tensor of type float, float16 or bfloat16. Shape support 2D ~ 8D.
The format must be ND.
- threshold: A scalar, type is float, used to set the threshold of "x".

## Outputs

y: A tensor has the same type and format as "x".
Other dimensions of its shape are the same as those of "x".
The value of the last dimension is half the value of the last dimension of "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input1 threshold: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
