# BatchToSpace

```c
REG_OP(BatchToSpace)
    .INPUT(x, TensorType::BasicType())
    .INPUT(crops, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::BasicType())
    .REQUIRED_ATTR(block_size, Int)
    .OP_END_FACTORY_REG(BatchToSpace)
```

## Brief

BatchToSpace rearranges data from the batch dimension into spatial blocks.

## Inputs

Two inputs, including:
- x: A 4D tensor, Format support ND, Must be one of the following types:
float16, float32, double, int64, int32, uint8, uint16, uint32, uint64, int8,
int16, complex64, complex128, qint8, quint8, qint16, quint16, qint32, bfloat16.
- crops: A 2D Tensor of shape [2, 2] = [[crop_top, crop_bottom], [crop_left, crop_right]].
    Values are non-negative integers. Support int32 or int64.

## Outputs

y: A 4D Tensor of shape [N, H_out, W_out, C] where
   H_out = H_in * block_size - crop_top - crop_bottom
   W_out = W_in * block_size - crop_left - crop_right

## Attributes

- block_size: An int >= 1, specifying the size of the spatial block.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 crops: int32,int64
- output0 y: float16,float32
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- input1 crops: int32,int64
- output0 y: double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator BatchToSpace.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
