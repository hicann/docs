# PRelu

```c
REG_OP(PRelu)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(weight, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OP_END_FACTORY_REG(PRelu)
```

## Brief

Performs parametric ReLU .

## Inputs

Two inputs, including:
- x: A multi-dimensional Tensor of type bfloat16, float16 or float32.
- weight: A Scalar or 1D Tensor of type bfloat16, float16 or float32, specifying the weight,
initial value of "a". The number of dimensions must be the same as the number of channels . 

## Outputs

y: An activated Tensor. Has the same dimensions with "x" . 

## Third-party framework compatibility

Compatible with PyTorch and Caffe operator PReLU.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
