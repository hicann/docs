# RollV2

```c
REG_OP(RollV2)
    .INPUT(input, TensorType({DT_INT8,DT_UINT8,DT_INT16,DT_UINT16,DT_INT32,DT_INT64,DT_FLOAT16, \
                            DT_FLOAT,DT_DOUBLE}))
    .INPUT(shift, TensorType({DT_INT32,DT_INT64}))
    .INPUT(axes, TensorType({DT_INT32,DT_INT64}))
    .OUTPUT(output, TensorType({DT_INT8,DT_UINT8,DT_INT16,DT_UINT16,DT_INT32,DT_INT64,DT_FLOAT16, \
                            DT_FLOAT,DT_DOUBLE}))
    .OP_END_FACTORY_REG(RollV2)
```

## Brief

Roll the tensor along the given dimension(s).

## Inputs

One inputs, including:
- x: A tensor. Must be one of the following types: int8, uint8, int16, uint16, int32, int64, float16, float32, double.
- shift: The number of places by which the elements of the tensor are shifted. Must be one of the following types: int32, int64.
- axes: Axis along which to roll. Must be one of the following types:  int32, int64.

## Outputs

y: A Tensor with the same type and shape of x's. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 shift: int32,int64
- input2 axes: int32,int64
- output0 output: double,float16,float32,int8,int16,int32,int64,uint8,uint16

## Third-party framework compatibility

Compatible with the Pytorch operator Roll. 


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
