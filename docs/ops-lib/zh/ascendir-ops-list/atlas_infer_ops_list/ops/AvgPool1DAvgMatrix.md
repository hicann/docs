# AvgPool1DAvgMatrix

```c
REG_OP(AvgPool1DAvgMatrix)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, DT_UINT8,
                          DT_INT32, DT_INT64, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, DT_UINT8,
                           DT_INT32, DT_INT64, DT_DOUBLE}))
    .REQUIRED_ATTR(ksize, Int)
    .REQUIRED_ATTR(strides, Int)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(ceil_mode, Bool, false)
    .ATTR(count_include_pad, Bool, false)
    .OP_END_FACTORY_REG(AvgPool1DAvgMatrix)
```

## Brief

Generate an auxiliary matrix .  

## Inputs

- x: A tensor. Must be one of the following types:uint8, int8,int16, int32,
int64, float16, float, double.The format must be NHWC/NCHW.

## Outputs

y_tensor: A  tensor with the same types as "x" .  

## Attributes

- ksize: Kernel size. Input type is int.
- strides: Input type is int.
- pads: Input type is listInt .
- ceil_mode: Bool, default value is false.
- count_include_pad: Bool, default value is false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8

## Third-party framework compatibility

Compatible with the TensorFlow operator Unbatch.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
