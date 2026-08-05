# SwiGluGrad

```c
REG_OP(SwiGluGrad)
        .INPUT(y_grad, "T")
        .INPUT(x, "T")
        .OUTPUT(x_grad, "T")
        .DATATYPE(T, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
        .ATTR(dim, Int, -1)
        .OP_END_FACTORY_REG(SwiGluGrad)
```

## Brief

Compute the SwiGluGrad,
where the activations function in GLU is SwishGrad.

## Inputs

two input, including:
- y_grad: A Tensor, which is the output gradient of forward operator and which
has the same shape as "x" except for the dimension specified by the "dim" parameter. 
The dimension size specified by "dim" is half of the corresponding dimension of x. 
Must be one of the following types: bfloat16, float16, float32.
- x: A Tensor. Must be one of the following types: bfloat16, float16, float32.

## Outputs

one Output, including:
x_grad: A Tensor, which is the gradient of x and has the same shape as "x". 
Must be one of the following types: bfloat16, float16, float32.

## Attributes

one attribute, including:
- dim: A optional int. The dimension to be split, default is -1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y_grad: bfloat16,float16,float32
- input1 x: bfloat16,float16,float32
- output0 x_grad: bfloat16,float16,float32

## Third-party framework compatibility

New operator SwiGluGrad.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
