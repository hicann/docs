# AdaCast

```c
REG_OP(AdaCast)
    .INPUT(x, "T1")
    .OUTPUT(y, "T2")
    .ATTR(pixel, Int, 65535)
    .DATATYPE(T1, TensorType({DT_UINT16}))
    .DATATYPE(T2, TensorType({DT_FLOAT16}))
    .OP_END_FACTORY_REG(AdaCast)
```

## Brief

data conversion operator
Convert uint16 to uint32, convert to int32, convert to float32,
multiply by the reciprocal of pixel, convert to float16 . 

## Inputs

one inputs, including:
- x: A Tensor. Must be one of the following types: uint16.

## Outputs

y: A Tensor. Must be one of the following types: float16. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: uint16
- output0 y: float16

## Third-party framework compatibility

only for use by corresponding operators in HDRnet networks


---

[Back to Operator Specifications (Ascend950)](../README.md)
