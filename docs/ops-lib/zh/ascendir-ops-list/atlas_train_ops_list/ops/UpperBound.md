# UpperBound

```c
REG_OP(UpperBound)
    .INPUT(sorted_x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, \
      DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_DOUBLE}))
    .INPUT(values, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, \
      DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64}))
    .REQUIRED_ATTR(out_type, Type)
    .OP_END_FACTORY_REG(UpperBound)
```

## Brief

Applies upper_bound(sorted_search_values, values) along each row. 

## Inputs

Inputs "sorted_x" and "values" are 2D tensors.
- sorted_x: A 2D Tensor where each row is ordered.
- values: A 2D Tensor with the same numbers of rows as "sorted_x".

## Outputs

y: A Tensor with the same shape as "values". 

## Attributes

out_type: sets the optional out_type attribute to value. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 sorted_x: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 values: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- output0 y: int32,int64

## Attention Constraints

UpperBound runs on the Ascend AI CPU, which delivers poor performance. 

## Third-party framework compatibility

Compatible with the TensorFlow operator UpperBound.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
