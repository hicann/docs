# MaxPoolWithArgmaxV1

```c
REG_OP(MaxPoolWithArgmaxV1)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT32}))
    .OUTPUT(argmax, TensorType({DT_UINT16, DT_INT32}))
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dtype, Int, 3)
    .ATTR(dilation, ListInt, {1, 1, 1, 1})
    .ATTR(ceil_mode, Bool, false)
    .OP_END_FACTORY_REG(MaxPoolWithArgmaxV1)
```

## Brief

Performs max pooling on the input and outputs both max values and indices.

## Inputs

One input:
- x: A tensor of type float16,float32, support format: [NC1HWC0, NCHW],
format NCHW can only support float32. 

## Outputs

- y: A tensor. Has the same type and format as input "x".
- argmax:  A tensor. type:uint16, int32.
Format NCHW can only support int32, format NC1HWC0 can only support uint16,
specifying when the dtype of argmax is int32, argmax must be index; when the dtype of argmax is uint16, argmax must be mask. 

## Attributes

- ksize: A required list of int8, int16, int32, or int64 values,
specifying the size of the window for each dimension of the input tensor. No default value.
- strides: A required list of int8, int16, int32, or int64 values,
specifying the stride of the sliding window for each dimension of the input tensor. No default value.
- pads: A required list of int8, int16, int32, or int64 values,
specifying the pad of the input feature map. No default value. 
- dtype: An Attr which type is int8, int16, int32, or int64. Default value is 3.
- dilation:A required list of int8, int16, int32, or int64 values, specifying the stride in each kernel.
Default value is: [1,1,1,1].
- ceil_mode: An attr which type is bool, default value is false. When True,
will use ceil instead of floor to compute the output shape.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- output0 y: float16
- output1 argmax: uint16

## Attention Constraints

- The MaxPoolWithArgmaxV2 operator has the same function, and it is recommended to use the V2 operator.
- ksize: a list that has length 4:
ksize[0] = 1, ksize[3] = 1, ksize[1] * ksize[2] < 1033.
- strides: a list that has length 4:
strides[0] = 1, strides[3] = 1, 1 <= strides[1] <= 127, 1 <= strides[2] <= 127, strides[1] * strides[2] < 7932.
- pads: a list that has length 4:
pads[0] = 1, pads[3] = 1, 0 <= pads[1] <= (ksize[1]//2), 0 <= pads[2] <= (ksize[2]//2).

## Third-party framework compatibility

Compatible with the PyTorch operator max_pool2d_with_indices.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
