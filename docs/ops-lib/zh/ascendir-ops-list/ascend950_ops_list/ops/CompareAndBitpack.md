# CompareAndBitpack

```c
REG_OP(CompareAndBitpack)
    .INPUT(x, TensorType({ DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_INT8, \
        DT_INT16, DT_INT32, DT_INT64, DT_BOOL }))
    .INPUT(threshold, TensorType({ DT_FLOAT, DT_FLOAT16, DT_DOUBLE, \
        DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_BOOL }))
    .OUTPUT(y, TensorType(DT_UINT8))
    .OP_END_FACTORY_REG(CompareAndBitpack)
```

## Brief

Compare values of input to threshold and pack resulting bits into
a uint8.

## Inputs

The input size must be a non-negative int32 scalar Tensor. Inputs include:
- input:Values to compare against threshold and bitpack.
- threshold:Threshold to compare against.

## Outputs

y:The bitpacked comparisons. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bool,double,float16,float32,int8,int16,int32,int64
- input1 threshold: bool,double,float16,float32,int8,int16,int32,int64
- output0 y: uint8

## Attention Constraints

Currently, the innermost dimension of the tensor must be divisible by 8. 

## Third-party framework compatibility

Compatible with tensorflow CompareAndBitpack operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
