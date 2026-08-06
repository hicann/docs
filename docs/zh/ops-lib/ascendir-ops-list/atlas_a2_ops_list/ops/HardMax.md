# HardMax

```c
REG_OP(HardMax)
    .INPUT(x, TensorType({ DT_FLOAT16, DT_FLOAT }))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(axis, Int, -1)
    .OP_END_FACTORY_REG(HardMax)
```

## Brief

Hardmax(element in input, axis) = 1 if the element is the first maximum value along the specified axis, 0
otherwise The input does not need to explicitly be a 2D vector.The "axis" attribute indicates the dimension along
which Hardmax will be performed.The output tensor has the same shape and contains the Hardmax values of the
corresponding input.

## Inputs

one input including:
x: input A ND Tensor.Must be one of the following types:float32,float16

## Outputs

one output including:
y:A ND Tensor of the same dtype as x

## Attributes

axis:A required int attribute that decides which dimension will be used to cal the hard_max


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
