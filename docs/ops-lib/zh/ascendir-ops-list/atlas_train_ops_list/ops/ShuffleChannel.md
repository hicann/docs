# ShuffleChannel

```c
REG_OP(ShuffleChannel)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT,DT_INT8, DT_UINT8, DT_INT16,
                          DT_UINT16, DT_INT32, DT_UINT32,DT_INT64,DT_UINT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT,DT_INT8, DT_UINT8, DT_INT16,
                           DT_UINT16, DT_INT32, DT_UINT32,DT_INT64,DT_UINT64}))
    .ATTR(group, Int, 1)
    .OP_END_FACTORY_REG(ShuffleChannel)
```

## Brief

Permutes data in the channel dimension of the input

## Inputs

Inputs including:
x: A required Tensor. Must be one of the following types:
float16, float32, int8, uint8, int16, uint16, int32, uint32, int64, uint64 . 

## Outputs

y: A required Tensor. Has same type and shape as "x". Must be one of the following types:
float16, float32, int8, uint8, int16, uint16, int32, uint32, int64, uint64 . 

## Attributes

group: A required int32, specifying the number of groups to split the channel dimension into. Defaults to "1" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

- "group" must be greater than 0 and must evenly divide the channel dimension size.
- The format of input "x" must be NCHW.

## Third-party framework compatibility

Compatible with the Caffe operator ShuffleChannel.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
