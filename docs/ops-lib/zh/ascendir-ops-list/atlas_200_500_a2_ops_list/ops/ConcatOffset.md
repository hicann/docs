# ConcatOffset

```c
REG_OP(ConcatOffset)
    .INPUT(concat_dim, TensorType({DT_INT32}))
    .DYNAMIC_INPUT(x, TensorType({DT_INT32}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_INT32}))
    .REQUIRED_ATTR(N, Int)
    .OP_END_FACTORY_REG(ConcatOffset)
```

## Brief

Computes offsets of concat inputs within its output .

## Inputs

Two inputs, including:
- concat_dim: A Tensor of type int32.Supported format list ["ND"].
- x: A list of 1D tensor objects of type int32, each with same shape and type.
       It's a dynamic input.Supported format list ["ND"].
The number of tensors in the x must be at least 2.
The shape size of each tensor in x is in range [1, 8]. 

## Outputs

y: A Tensor list with same type as "x" . It's a dynamic output.Supported format list ["ND"]. 

## Attributes

N: A required int indicating the number of tensors in the input x. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 concat_dim: int32
- input1 x: int32
- output0 y: int32
### AI CPU
- input0 concat_dim: int32

## Third-party framework compatibility

@ Compatible with the TensorFlow operator ConcatOffset.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
