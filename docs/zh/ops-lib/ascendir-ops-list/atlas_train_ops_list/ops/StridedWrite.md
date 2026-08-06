# StridedWrite

```c
REG_OP(StridedWrite)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType::ALL())
    .ATTR(axis, Int, 1)
    .ATTR(stride, Int, 1)
    .OP_END_FACTORY_REG(StridedWrite)
```

## Brief

Write data by stride.

## Inputs

x: A Tensor. All data types are supported. Support format: NC1HWC0 . 

## Outputs

y: A Tensor. Has the same type and format as "x".

## Attributes

- axis: A required int32, specifying the index of axis to write by stride.
- stride: A required int32, specifying the value of writing stride.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,int8
- output0 y: float16,int8


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
