# Flatten

```c
REG_OP(Flatten)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType::ALL())
    .ATTR(axis, Int, 1)
    .OP_END_FACTORY_REG(Flatten)
```

## Brief

Flattens the inputs tensor into a 2D matrix. If input tensor has shape (d_0, d_1,..., d_n),
       then the output will have shape (d_0 X d_1 ... d_(axis-1), d_axis X d_(axis + 1)...X d_n)

## Inputs

One input:
x: A multi-dimensional tensor. All data types are supported.

## Outputs

y: A 2D flattened tensor with the contents of the input tensor, with input dimensions up to axis flattened
to the outer dimension of the output and remaining input dimensions flattened into the inner dimension of the
output.
Has the same type as "x".

## Attributes

axis: A optional int32, default value is 1. Indicate up to which input dimensions (exclusive) should be flattened
to the outer dimension of the output. The value for axis must be in the range [-r, r], where r is the rank of
the input tensor. Negative value means counting dimensions from the back. When axis = 0, the shape of
the output tensor is (1, (d_0 X d_1 ... d_n), where the shape of the input tensor is (d_0, d_1, ... d_n).

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bool,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: bool,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with TensorFlow / ONNX operator Flatten.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
