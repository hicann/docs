# MaxPoolGradWithArgmaxV1

```c
REG_OP(MaxPoolGradWithArgmaxV1)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(grad, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(argmax, TensorType({DT_UINT16, DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dtype, Int, 3)
    .ATTR(dilation, ListInt, {1, 1, 1, 1})
    .ATTR(ceil_mode, Bool, false)
    .OP_END_FACTORY_REG(MaxPoolGradWithArgmaxV1)
```

## Brief

Performs the backpropagation of MaxPoolWithArgmaxV1.

## Inputs

Three inputs, including:
- x: A tensor of type float16,float32, support format: [NC1HWC0, NCHW].
- grad: A tensor of type float16,float32, support format: [NC1HWC0, NCHW].
- argmax: A tensor of type uint16,int32, support format: [NC1HWC0, NCHW].
For Ascend 950 AI Processor: The uint16 data type is not supported.

## Outputs

y: A Tensor. Has the same type and format as input "x". 

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
- ceil_mode: An attr which type is bool, default value is false. when True,
will use ceil instead of floor to compute the output shape.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- input1 grad: float16
- input2 argmax: uint16
- output0 y: float16

## Attention Constraints

- The MaxPoolGradWithArgmaxV2 operator has the same function, and it is recommended to use the V2 operator.
When call the MaxPoolGradWithArgmaxV2 operator, the constraints are updated to those of V2.
- ksize: A list that has length 4:
ksize[0] = 1, ksize[3] = 1, ksize[1] * ksize[2] <= (ub_size-8)*1024//7//2//16.
- strides: A list that has length 4:
strides[0] = 1, strides[3] = 1, 1 <= strides[1] <= 2048, 1 <= strides[2] <= 2048.
- pads: A list that has length 4:
pads[0] = 1, pads[3] = 1, 0 <= pads[1] <= (ksize[1]//2), 0 <= pads[2] <= (ksize[2]//2).
- x: Format NCHW can only support float.
- argmax: format NCHW can only support int32, format NC1HWC0 can only support uint16,
specifying when the dtype of argmax is int32, argmax must be index; when the dtype of argmax is uint16, argmax must be mask.
- dilation: A list that has length 4:
dilation[0] = 1, dilation[1] = 1, dilation[2] = 1, dilation[3] = 1.

## Third-party framework compatibility

Compatible with the PyTorch backward operator of max_pool2d_with_indices.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
