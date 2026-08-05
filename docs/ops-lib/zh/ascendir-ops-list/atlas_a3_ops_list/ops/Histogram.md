# Histogram

```c
REG_OP(Histogram)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT64, DT_INT32, DT_INT16, DT_INT8, DT_UINT8}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_INT64, DT_INT32, DT_INT16, DT_INT8, DT_UINT8}))
    .ATTR(bins, Int, 100)
    .ATTR(min, Float, 0.0)
    .ATTR(max, Float, 0.0)
    .OP_END_FACTORY_REG(Histogram)
```

## Brief

Computes the histogram of a tensor.

## Inputs

x: A Tensor of type float16,float32,int64,int32,int16,int8,uint8. 

## Outputs

y: A Tensor. A Tensor of type float32,int64,int32,int16,int8,uint8 . 

## Attributes

- bins: Optional. Must be one of the following types: int32. Defaults to 100.
- min: Optional. Must be one of the following types: float32. Defaults to 0.0.
- max: Optional. Must be one of the following types: float32. Defaults to 0.0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: float16,float32,int32
- output0 y: float32,int32

## Attention Constraints

The operator will use the interface set_atomic_add(), therefore weights and output should be float32 only. 

## Third-party framework compatibility

Compatible with the Pytorch operator Histc.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
