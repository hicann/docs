# ListDiff

```c
REG_OP(ListDiff)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_UINT8, DT_INT8,
        DT_INT16, DT_UINT16, DT_INT32, DT_INT64}))
    .INPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_UINT8, DT_INT8,
        DT_INT16, DT_UINT16, DT_INT32, DT_INT64}))
    .OUTPUT(out, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_UINT8, DT_INT8,
        DT_INT16, DT_UINT16, DT_INT32, DT_INT64}))
    .OUTPUT(idx, TensorType({DT_INT32, DT_INT64}))
    .ATTR(out_idx, Type, DT_INT32)
    .OP_END_FACTORY_REG(ListDiff)
```

## Brief

Calculates the difference between two numbers or a list of strings. 

## Inputs

Inputs "x" and "y" are 1D vectors.
- x: A Tensor. 1D. Values to keep.
- y: A Tensor. Must have the same type as x. 1D. Values to remove.

## Outputs

- out: A Tensor. Has the same type as "x".
- idx: A Tensor of type "out_idx".

## Attributes

out_idx: An optional DType from: "int32, int64". Defaults to "int32". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,string,uint8,uint16
- input1 y: double,float16,float32,int8,int16,int32,int64,string,uint8,uint16
- output0 out: double,float16,float32,int8,int16,int32,int64,string,uint8,uint16
- output1 idx: int32,int64

## Attention Constraints

ListDiff runs on the Ascend AI CPU, which delivers poor performance. 

## Third-party framework compatibility

Compatible with the TensorFlow operator ListDiff.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
