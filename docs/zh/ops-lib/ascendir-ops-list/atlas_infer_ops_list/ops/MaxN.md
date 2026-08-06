# MaxN

```c
REG_OP(MaxN)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_FLOAT64, DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_FLOAT64, DT_INT32, DT_INT64}))
    .OP_END_FACTORY_REG(MaxN)
```

## Brief

Element-wise min of each of the input tensors (with Numpy-style broadcasting support).
All inputs and outputs must have the same data type. This operator supports multidirectional
(i.e., Numpy-style) broadcasting

## Inputs

One input including:
x: dynamic input with ND Tensor. Must be one of the following types: float32, float16, double, int32, int64.
 The shape and dtype of all inputs must be equal.

## Outputs

one output including:
y:A ND Tensor with the same shape and dtype as x


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
