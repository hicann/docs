# GeluMul

```c
REG_OP(GeluMul)
        .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
        .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
        .ATTR(approximate, String, "none")
        .OP_END_FACTORY_REG(GeluMul)
```

## Brief

GeluMul divides the input tensor into left and right tensors x1 and x2 based on the last dimension,
performs GELU calculation on x1 on the left, and multiplies the calculation result by x2. 

## Inputs

x: A tensor of type float, float16 or bfloat16. Shape support 2D ~ 8D.
The format must be ND.

## Outputs

y: A tensor has the same type and format as "x".
Other dimensions of its shape are the same as those of "x".
The value of the last dimension is half the value of the last dimension of "x". 

## Attributes

approximate: A optional string. The GELU approximation algorithm to use: 'none' or 'tanh', default is 'none'.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
