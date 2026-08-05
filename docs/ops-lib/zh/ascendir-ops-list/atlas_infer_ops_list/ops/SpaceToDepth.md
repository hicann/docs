# SpaceToDepth

```c
REG_OP(SpaceToDepth)
    .INPUT(x, TensorType::BasicType())
    .OUTPUT(y, TensorType::BasicType())
    .REQUIRED_ATTR(block_size, Int)
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(SpaceToDepth)
```

## Brief

Outputs a copy of the input tensor where values from the "height" and
"width" dimensions are moved to the "depth" dimension . 

## Inputs

x: A Tensor. The data type must be one of BasicType.
The data format must be NCHW or NHWC and must be same as the attribute value data_format.

## Outputs

y: A Tensor. Has the same type as input "x".

## Attributes

- block_size: A required int, specifying the input block size.
- data_format: An optional string, specifying the data format. Must be
    NCHW or NHWC, and be same as the data format of x. Defaults to "NHWC".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator SpaceToDepth.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
