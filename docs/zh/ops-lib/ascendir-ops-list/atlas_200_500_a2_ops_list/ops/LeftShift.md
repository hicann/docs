# LeftShift

```c
REG_OP(LeftShift)
    .INPUT(x, TensorType({DT_INT8, DT_INT16, DT_INT32, DT_INT64, \
           DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64}))
    .INPUT(y, TensorType({DT_INT8, DT_INT16, DT_INT32, DT_INT64, \
           DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64}))
    .OUTPUT(z, TensorType({DT_INT8, DT_INT16, DT_INT32, DT_INT64, \
            DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64}))
    .OP_END_FACTORY_REG(LeftShift)
```

## Brief

Element-wise computes the bitwise left-shift of x and y . 

## Inputs

Input "x" is a k-dimensional tensor. Inputs "num_lower" and "num_upper"
are 0D scalars.
- x: A Tensor. Must be one of the following types: int8, int16, int32,
int64, uint8, uint16, uint32, uint64.
- y: A Tensor. Has the same type as "x".

## Outputs

z: A Tensor. Has the same type as "x".  

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 y: int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 z: int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

Unique runs on the Ascend AI CPU, which delivers poor performance.  

## Third-party framework compatibility

Compatible with the TensorFlow operator LeftShift.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
