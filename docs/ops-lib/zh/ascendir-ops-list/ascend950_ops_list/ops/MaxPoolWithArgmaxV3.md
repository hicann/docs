# MaxPoolWithArgmaxV3

```c
REG_OP(MaxPoolWithArgmaxV3)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BF16}))
    .OUTPUT(argmax, TensorType({DT_INT32, DT_INT64}))
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dtype, Int, 3)
    .ATTR(dilation, ListInt, {1, 1})
    .ATTR(ceil_mode, Bool, false)
    .ATTR(data_format, String, "NCHW")
    .OP_END_FACTORY_REG(MaxPoolWithArgmaxV3)
```

## Brief

Performs max pooling on the input and outputs both max values and indices.

## Inputs

One input:
x: A tensor of type bfloat16, float16, float32, the shape is `[batch, channels, height_in, width_in]` or
`[batch, height_in, width_in, channels]`.

## Outputs

- y: A tensor has the same type and format as input "x", the shape is `[batch, channels, height_out, width_out]` or
`[batch, height_out, width_out, channels]`.
- argmax:  A tensor of type is int64 or int32, the shape is `[batch, channels, height_out, width_out]` or
`[batch, height_out, width_out, channels]`.

## Attributes

- ksize: A required list of int64 values,
specifying the size of the window for each dimension of the input tensor.
A list that has length 2.
- strides: A required list of int64 values,
specifying the stride of the sliding window for each dimension of the input tensor.
A list that has length 2.
- pads: A required list of int64 values,
specifying the pad of the input feature map. No default value.
A list that has length 2:
0 <= pads[0] <= (ksize[0]//2), 0 <= pads[1] <= (ksize[1]//2).
- dilation: A list that has length 2, default value is {1,1}.
- dtype: An optional int. default value is 3.  (3 is int32, 9 is int64)
- ceil_mode: When true, will use ceil instead of floor to compute the output shape, defaults to false.
- data_format: The value can be "NCHW" or "NHWC", defaults to "NCHW".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
- output1 argmax: int32,int64

## Third-party framework compatibility

Compatible with the PyTorch operator max_pool2d_with_indices.


---

[Back to Operator Specifications (Ascend950)](../README.md)
