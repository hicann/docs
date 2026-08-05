# LowerBound

```c
REG_OP(LowerBound)
    .INPUT(sorted_x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, \
        DT_INT16, DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_DOUBLE}))
    .INPUT(values, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, \
        DT_INT16, DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64}))
    .ATTR(out_type, Type, DT_INT32)
    .OP_END_FACTORY_REG(LowerBound)
```

## Brief

Applies lower_bound(sorted_search_values, values) along each row. 

## Inputs

The input sorted_x and values can be one-dimensional vector. Inputs include:
- sorted_x:A `Tensor`. 2-D Tensor where each row is ordered.
Must be one of the following types: float32, float16, int8, int16, uint16, uint8, int32, int64, double.
- values:A `Tensor`. Must have the same type as `sorted_x`.

## Outputs

y: A `Tensor` of type `out_type`. 

## Attributes

out_type:An optional `DType` from: `int32, int64`.
Defaults to `int32`. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 sorted_x: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 values: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- output0 y: int32,int64

## Attention Constraints

The implementation for LowerBound on Ascend uses AI CPU, with bad performance. 

## Third-party framework compatibility

Compatible with tensorflow Operator LowerBound.

## Quantization supported or not.

Not supported

## Quantized inference supported or not.

Supported


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
