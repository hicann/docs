# MaxPool3DWithArgmaxV2

```c
REG_OP(MaxPool3DWithArgmaxV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BF16}))
    .OUTPUT(argmax, TensorType({DT_INT32, DT_INT64}))
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dilation, ListInt, {1, 1, 1})
    .ATTR(ceil_mode, Bool, false)
    .ATTR(data_format, String, "NCDHW")
    .ATTR(dtype, Int, 3)
    .OP_END_FACTORY_REG(MaxPool3DWithArgmaxV2)
```

## Brief

Performs max pooling on the input and outputs both max values and indices.

## Inputs

One input:
x: A tensor of type bfloat16, float16, float32, the shape is [batch, channels, depth_in, height_in, width_in] or
[batch, depth_in, height_in, width_in, channels].

## Outputs

- y: A tensor has the same type and format as input "x", the shape is [batch, channels, depth_out, height_out, width_out] or
[batch, depth_out, height_out, width_out, channels].
- argmax:  A tensor of type is int64 or int32, the shape is [batch, channels, depth_out, height_out, width_out] or
[batch, depth_out, height_out, width_out, channels].

## Attributes

- ksize: A required list of int64 values,
specifying the size of the window for each dimension of the input tensor.
A list that has length 3.
- strides: A required list of int64 values,
specifying the stride of the sliding window for each dimension of the input tensor.
A list that has length 3.
- pads: A required list of int64 values,
specifying the pad of the input feature map.
A list that has length 3:
0 <= pads[0] <= (ksize[0]//2), 0 <= pads[1] <= (ksize[1]//2), 0 <= pads[2] <= (ksize[2]//2).
- dilation: A list that has length 3, default value is {1,1,1}.
- ceil_mode: When true, will use ceil instead of floor to compute the output shape, defaults to false.
- data_format: The value can be "NCDHW" or "NDHWC", defaults to "NCDHW".
- dtype: An optional int, default value is 3.  (3 is int32, 9 is int64)

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
- output1 argmax: int32

## Third-party framework compatibility

Compatible with the PyTorch operator max_pool3d_with_indices.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
