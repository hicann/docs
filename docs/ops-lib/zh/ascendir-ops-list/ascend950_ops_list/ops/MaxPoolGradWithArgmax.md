# MaxPoolGradWithArgmax

```c
REG_OP(MaxPoolGradWithArgmax)
    .INPUT(x, TensorType::RealNumberType())
    .INPUT(grad, TensorType::RealNumberType())
    .INPUT(argmax, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::RealNumberType())
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(padding, String)
    .ATTR(include_batch_in_index, Bool, false)
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(MaxPoolGradWithArgmax)
```

## Brief

Performs the backpropagation of MaxPoolWithArgmax.

## Inputs

Three inputs, including:
- x: A 4d tensor. Supported type: float16, bfloat16, float32.
Must set the format, supported format list ["NCHW, NHWC"]
- grad: A 4d tensor. Supported type: float16, bfloat16, float32.
Must set the format, supported format list ["NCHW, NHWC"]
- argmax: A tensor of type int32 or int64.
For Ascend 950 AI Processor: The uint16 data type is not supported.

## Outputs

y: A Tensor. Has the same type and format as input "x".

## Attributes

- ksize: A required list of int8, int16, int32, or int64 values,
specifying the size of the window for each dimension of the input tensor.
No default value.
- strides: A required list of int8, int16, int32, or int64 values,
specifying the stride of the sliding window for each dimension of
the input tensor. No default value.
- padding: A string specifying the padding algorithm for the input feature map. No default value.
- include_batch_in_index: A boolean attribute indicating whether the batch dimension is included when computing argmax indices.
    If false (default), the argmax index is computed within each batch independently, and the index only reflects the spatial and channel position.
    if true, the batch dimension is included in the flattened index computation, so the argmax index spans across the batch dimension.
    Default value: false.
- data_format: A string specifying the data layout of the input and output tensors.
    - "NHWC": Data is stored in the order [batch, height, width, channels].
    - "NCHW": Data is stored in the order [batch, channels, height, width].
    Default value: "NHWC".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 grad: bfloat16,float16,float32
- input2 argmax: int32,int64
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 grad: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input2 argmax: int32,int64
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

- "ksize" is a list that has length 4:
If data_format is "NCHW", the ksize[0] = 1 or ksize[1] = 1,
If data_format is "NHWC", the ksize[0] = 1 or ksize[3] = 1.
- "strides" is a list that has length 4:
If data_format is "NCHW", the strides[0] = 1 or strides[1] = 1,
If data_format is "NHWC", the strides[0] = 1 or strides[3] = 1.
- "padding" is either "SAME" or "VALID".
- "include_batch_in_index": This operator currently only supports include_batch_in_index = false.
@see max_pool_with_argmax

## Third-party framework compatibility

Compatible with the TensorFlow operator MaxPoolGradWithArgmax.


---

[Back to Operator Specifications (Ascend950)](../README.md)
