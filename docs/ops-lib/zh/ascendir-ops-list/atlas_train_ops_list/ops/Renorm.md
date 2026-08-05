# Renorm

```c
REG_OP(Renorm)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR(p, Float)
    .REQUIRED_ATTR(dim, Int)
    .REQUIRED_ATTR(maxnorm, Float)
    .OP_END_FACTORY_REG(Renorm)
```

## Brief

Returns a tensor where each sub-tensor of input along dimension
      dim is normalized such that the p-norm of the sub-tensor is lower than the value maxnorm.

## Inputs

One input, including:
x: A tensor. Support one of the following types: float32, float16, bfloat16. The dimension range is [2, 8]. 

## Outputs

One output, including:
y: shape and dtype of output, should be same shape and type as input.

## Attributes

- p: Specify L_p norm, the type is float32, the range is greater than or equal to 0.
- dim: The processed dim, the type is int64, the range is within [-x dimension, x dimension - 1].
- maxnorm: Threshold for comparison, the type is float32, the range is greater than or equal to 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
