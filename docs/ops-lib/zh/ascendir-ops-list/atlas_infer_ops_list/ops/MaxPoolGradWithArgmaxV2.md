# MaxPoolGradWithArgmaxV2

```c
REG_OP(MaxPoolGradWithArgmaxV2)
    .INPUT(x, TensorType({DT_FLOAT16}))
    .INPUT(grad, TensorType({DT_FLOAT16}))
    .INPUT(argmax, TensorType({DT_UINT16}))
    .OUTPUT(y, TensorType({DT_FLOAT16}))
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dtype, Int, 3)
    .ATTR(dilation, ListInt, {1,1,1,1})
    .ATTR(ceil_mode, Bool, false)
    .OP_END_FACTORY_REG(MaxPoolGradWithArgmaxV2)
```

## Brief

Performs the backpropagation of MaxPoolWithArgmaxV2.

## Inputs

Three inputs, including:
- x: An 5hd tensor of type float16.
Must set the format, supported format list ["NC1HWC0"]
- grad: An 5hd tensor of type float16.
Must set the format, supported format list ["NC1HWC0"]
- argmax: An 5hd tensor of type uint16 or int64.
Must set the format, supported format list ["NC1HWC0"] 
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
- dtype: A optional int. default value is 3.
- dilation: A optional list of int8, int16, int32, or int64 values.
- ceil_mode: A optional bool. default value is false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- input1 grad: float16
- input2 argmax: uint16
- output0 y: float16

## Attention Constraints

- ksize: a list that has length 4:
ksize[0] = 1, ksize[1] = 1, ksize[2] * ksize[3] <= (ub_size-8)*1024//7//2//16.
- strides: a list that has length 4:
strides[0] = 1, strides[1] = 1, 1 <= strides[2] <= 2048, 1 <= strides[3] <= 2048.
- pads: a list that has length 4:
pads[0] = 1, pads[1] = 1, 1 <= pads[2] <= (ksize[2]//2), 1 <= pads[3] <= (ksize[3]//2).
- dilation: a list that has length 4.
- ceil_mode: is a bool, default is false.
@see max_pool_grad_with_argmaxv2

## Third-party framework compatibility

Compatible with the PyTorch backward operator of max_pool2d_with_indices.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
