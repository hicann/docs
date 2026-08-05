# MaxPoolGradWithArgmaxV3

```c
REG_OP(MaxPoolGradWithArgmaxV3)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BF16}))
    .INPUT(grad, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BF16}))
    .INPUT(argmax, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BF16}))
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dtype, Int, 3)
    .ATTR(dilation, ListInt, {1, 1})
    .ATTR(ceil_mode, Bool, false)
    .ATTR(data_format, String, "NCHW")
    .OP_END_FACTORY_REG(MaxPoolGradWithArgmaxV3)
```

## Brief

Performs the backpropagation of MaxPoolGradWithArgmaxV3.

## Inputs

Three inputs, including:
- x: A tensor of dtype bfloat16, float16, float32, the shape is `[batch, channels, height_in, width_in]` or
`[batch, height_in, width_in, channels]` , the format is `NCHW` or `NHWC`.
- grad: A tensor has the same dtype and format as input "x", the shape is `[batch, channels, height_out, width_out]` or
`[batch, height_out, width_out, channels]`.
- argmax: A tensor has the same shape and format as input "grad", the dtype is int32 or int64.

## Outputs

y: A Tensor. Has the same dtype , shape and format as input "x".

## Attributes

- ksize: A required list of int64 values,
specifying the size of the window for each dimension of the input tensor. No default value.
- strides: A required list of int64 values,
specifying the stride of the sliding window for each dimension of the input tensor. No default value.
- pads: A required list of int64 values,
specifying the pad of the input feature map. No default value.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 grad: bfloat16,float16,float32
- input2 argmax: int32,int64
- output0 y: bfloat16,float16,float32

## Attention Constraints

- The MaxPoolGradWithArgmaxV3 operator has the same function, and it is recommended to use the V3 operator.
- ksize: a list that has length 2:
- strides: a list that has length 2:
- pads: a list that has length 2:
1 <= pads[0] <= (ksize[0]//2), 1 <= pads[1] <= (ksize[1]//2).
- dilation: a list that has length 2. default value is {1,1}.
- dtype: A optional int. default value is 3.
- ceil_mode: defaults to False.
- data_format: defaults to "NCHW".

## Third-party framework compatibility

Compatible with the Pytorch backward operator of max_pool2d_with_indices.


---

[Back to Operator Specifications (Ascend950)](../README.md)
