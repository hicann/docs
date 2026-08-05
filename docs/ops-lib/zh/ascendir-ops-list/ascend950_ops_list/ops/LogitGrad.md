# LogitGrad

```c
REG_OP(LogitGrad)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .INPUT(dy, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(dx, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .ATTR(eps, Float, -1.0)
    .OP_END_FACTORY_REG(LogitGrad)
```

## Brief

Backpropagation of Logit. 

## Inputs

- x: A input tensor of type float, float16 or bfloat16. Shape support 0D ~ 8D.
Input data for the backpropagation of the probability to logit transformation
The format must be ND.
- dy: Gradient of the positive output result. A Tensor with the same type, shape, format as "x".

## Outputs

dx: A output ensor with the same type, shape, format as "x". Probability to logit conversion backpropagates the output data. 

## Attributes

eps: The epslion of "x", an optional attribute, the type is float. Defaults to -1.0. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 dy: bfloat16,float16,float32
- output0 dx: bfloat16,float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
