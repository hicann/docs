# HistogramV2

```c
REG_OP(HistogramV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT64, DT_INT32, DT_INT16, DT_INT8, DT_UINT8}))
    .INPUT(min, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT64, DT_INT32, DT_INT16, DT_INT8, DT_UINT8}))
    .INPUT(max, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT64, DT_INT32, DT_INT16, DT_INT8, DT_UINT8}))
    .OUTPUT(y, TensorType({DT_INT32, DT_FLOAT}))
    .ATTR(bins, Int, 100)
    .ATTR(y_dtype, Type, DT_INT32)
    .OP_END_FACTORY_REG(HistogramV2)
```

## Brief

Computes the histogram of a tensor.

## Inputs

- x: A tensor of type float16, float32, int64, int32, int16, int8, uint8.
- min: A tensor of type float16, float32, int64, int32, int16, int8, uint8, with only one element.
- max: A tensor of type float16, float32, int64, int32, int16, int8, uint8, with only one element.

## Outputs

y: A tensor of type int32 .

## Attributes

bins: Optional. Type Must be int64. Value must be greater than 0, Defaults to 100.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int8,int16,int32,int64,uint8
- input1 min: float16,float32,int8,int16,int32,int64,uint8
- input2 max: float16,float32,int8,int16,int32,int64,uint8
- output0 y: int32

## Third-party framework compatibility

Compatible with the Pytorch operator Histc.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
