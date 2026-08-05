# AscendWeightQuant

```c
REG_OP(AscendWeightQuant)
    .INPUT(x, TensorType({DT_INT8}))
    .INPUT(offset, TensorType({DT_INT8}))
    .OUTPUT(y, TensorType({DT_INT8, DT_INT4}))
    .ATTR(dst_type, Int, DT_INT8)
    .OP_END_FACTORY_REG(AscendWeightQuant)
```

## Brief

Quantizes the input of int8.

## Inputs

- x: A tensor. Must be one of the following types: int8. The format support NZ.
- offset: A tensor. Must be one of the following types: int8. The format support NZ.

## Outputs

- y: A output Tensor. Must be one of the following types: int8, int4. The format support NZ.

## Attributes

- dst_type: Declare the output dtype. Support DT_INT8, DT_INT4. Defaults to DT_INT8.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: int8
- input1 offset: int8
- output0 y: int4,int8

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe, Onnx, Tensorflow or Pythorch.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
