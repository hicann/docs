# SpaceToBatch

```c
REG_OP(SpaceToBatch)
    .INPUT(x, TensorType::BasicType())
    .INPUT(paddings, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::BasicType())
    .REQUIRED_ATTR(block_size, Int)
    .OP_END_FACTORY_REG(SpaceToBatch)
```

## Brief

SpaceToBatch divides spatial data into blocks and moves them to the batch dimension.
This is the inverse of BatchToSpaceND.

## Inputs

- x: A 4D NHWC tensor [N, H_in, W_in, C], types: float16, float32, double, int64, int32,
int8, uint8, int16, uint16.
- paddings: A 2D int tensor with shape [2, 2] = [[pad_top, pad_bottom], [pad_left, pad_right]].

## Outputs

y: A 4D NHWC tensor [N*block_size*block_size, H_out, W_out, C] where
H_out = (H_in + pad_top + pad_bottom) / block_size,
W_out = (W_in + pad_left + pad_right) / block_size.

## Attributes

- block_size: A required int. The spatial block size.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 paddings: int32,int64
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- input1 paddings: int32,int64
- output0 y: double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator space_to_batch.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
