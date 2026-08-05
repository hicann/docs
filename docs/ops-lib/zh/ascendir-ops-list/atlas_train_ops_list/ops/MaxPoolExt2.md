# MaxPoolExt2

```c
REG_OP(MaxPoolExt2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT32, DT_DOUBLE, DT_INT8,
                          DT_INT16, DT_INT32, DT_INT64, DT_UINT8,
                          DT_UINT16, DT_QINT8}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT32, DT_DOUBLE, DT_INT8,
                           DT_INT16, DT_INT32, DT_INT64, DT_UINT8,
                           DT_UINT16, DT_QINT8}))
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(padding, String)
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(MaxPoolExt2)
```

## Brief

Performs max_pool_ext2 on the input .

## Inputs

One input:
x: A Tensor of type: float16, float32, float64, int8, int16, int32, int64, uint8, uint16, qint8.

## Outputs

y: A Tensor. Has the same type and format as input "x" . 

## Attributes

- ksize: A required list of int8, int16, int32, or int64 values,
specifying the size of the window for each dimension of the input tensor. No default value.
- strides: A required list of int8, int16, int32, or int64 values,
specifying the stride of the sliding window for each dimension of the input tensor. No default value.
- padding: A required string. No default value.
- data_format: An optional string .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- output0 y: float16

## Attention Constraints

- "ksize" is a list that has length 4: ksize[0] = 1 or ksize[3] = 1, ksize[1] * ksize[2] <= 255.
- "stride" is a list that has length 4: strides[0] = 1 or strides[3] = 1,
strides[1] <= 63, strides[0] >= 1, strides[2] <= 63, strides[2] >= 1.
- "padding" is either "SAME" or "VALID" .

## Third-party framework compatibility

Compatible with the TensorFlow operator MaxPoolV2.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
