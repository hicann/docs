# Logit

```c
REG_OP(Logit)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .ATTR(eps, Float, -1.0)
    .OP_END_FACTORY_REG(Logit)
```

## Brief

The logit function is a mathematical operation for converting probability to numeric variable. 

## Inputs

x: A tensor of type float, float16 or bfloat16. Input data for the probability to logit transformation.
Shape support 0D ~ 8D. The format must be ND.

## Outputs

y: A tensor with the same type, shape, format as "x". Output data from probability to logit transformation. 

## Attributes

eps: The epslion of "x", an optional attribute, the type is float. Defaults to -1.0. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core


---

[Back to Operator Specifications (Ascend950)](../README.md)
