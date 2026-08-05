# SwiGlu

```c
REG_OP(SwiGlu)
        .INPUT(x, "T")
        .OUTPUT(y, "T")
        .DATATYPE(T, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
        .ATTR(dim, Int, -1)
        .OP_END_FACTORY_REG(SwiGlu)
```

## Brief

Compute the SwiGlu,
where the activations function in GLU is Swish.

## Inputs

One input, including:
@x: A Tensor. Must be one of the following types: bfloat16, float16, float32.

## Outputs

one output, including:
@y: A Tensor. Must be one of the following types: bfloat16, float16, float32.

## Attributes

one attribute, including:
- dim: A optional int. The dimension to be split, default is -1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

New operator SwiGlu.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
