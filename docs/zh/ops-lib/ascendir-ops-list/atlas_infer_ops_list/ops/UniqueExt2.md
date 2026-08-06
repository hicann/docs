# UniqueExt2

```c
REG_OP(UniqueExt2)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, \
           DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_DOUBLE}))
    .INPUT(axis, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, \
           DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_DOUBLE}))
    .OUTPUT(idx, TensorType({DT_INT32, DT_INT64}))
    .ATTR(out_idx, Type, DT_INT32)
    .OP_END_FACTORY_REG(UniqueExt2)
```

## Brief

Finds unique elements in a 1D tensor. 

## Inputs

Input "x" is a k-dimensional tensor. Inputs "num_lower" and "num_upper"
are 0D scalars.
Including:
- x: 1D tensor.
- axis: A Tensor of type int32. Defaults to "None".

## Outputs

- y: "x" in the unique output "y".
- idx: A tensor the same size as "x". The index of each value of "x".

## Attributes

out_idx: An optional DType from: "int32, int64".
Defaults to "int32". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 axis: int32,int64
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- output1 idx: int32,int64

## Attention Constraints

UniqueExt2 runs on the Ascend AI CPU, which delivers poor performance. 

## Third-party framework compatibility

Compatible with the TensorFlow operator UniqueExt2.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
