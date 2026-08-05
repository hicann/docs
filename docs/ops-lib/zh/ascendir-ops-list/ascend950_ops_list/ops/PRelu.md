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

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 weight: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with PyTorch and Caffe operator PReLU.


---

[Back to Operator Specifications (Ascend950)](../README.md)
