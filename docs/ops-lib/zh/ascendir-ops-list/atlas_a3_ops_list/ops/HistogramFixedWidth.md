# HistogramFixedWidth

```c
REG_OP(HistogramFixedWidth)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT64}))
    .INPUT(range, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT64}))
    .INPUT(nbins, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_INT32}))
    .ATTR(dtype, Int, 3)
    .OP_END_FACTORY_REG(HistogramFixedWidth)
```

## Brief

This operation returns a rank 1 histogram counting the number of entries in `x`
 that fell into every bin.The bins are equal width and determined by the arguments
 'range' and 'nbins' .

## Inputs

Three inputs, including:
- x: A Tensor of type float32, int32, int64, float16.
- range: A Tensor of type float32, int32, int64, float16.
- nbins: A Tensor of type int32 .

## Outputs

y: A Tensor. A Tensor of type int32. 

## Attributes

dtype: An optional int. Defaults to 3 . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int32
- input1 range: float16,float32,int32
- input2 nbins: int32
- output0 y: int32
### AI CPU
- input0 x: double,float16,float32,int32,int64
- input1 range: double,float16,float32,int32,int64
- input2 nbins: int32
- output0 y: int32,int64

## Third-party framework compatibility

Compatible with TensorFlow operator HistogramFixedWidth.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
