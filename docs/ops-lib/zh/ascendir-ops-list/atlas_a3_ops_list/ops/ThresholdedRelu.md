# ThresholdedRelu

```c
REG_OP(ThresholdedRelu)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(alpha, Float, 1.0)
    .OP_END_FACTORY_REG(ThresholdedRelu)
```

## Brief

ThresholdedRelu takes one input data (Tensor) and produces one output data (Tensor)
 where the rectified linear function, y = x for x > alpha, y = 0 otherwise, is applied to the tensor elementwise.

## Inputs

one input including:
x: input A Tensor. Must be one of the following types: float32, float16

## Outputs

one output including:
y:A Tensor of the same type as x

## Attributes

alpha: An optional float. Defaults to 1.0. 


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
