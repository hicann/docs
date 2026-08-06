# MaxPool

```c
REG_OP(MaxPool)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT32, DT_DOUBLE, DT_INT8,
                          DT_INT16, DT_INT32, DT_INT64, DT_UINT8,
                          DT_UINT16, DT_QINT8}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT32, DT_DOUBLE, DT_INT8,
                           DT_INT16, DT_INT32, DT_INT64, DT_UINT8, DT_UINT16, DT_QINT8}))
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(padding, String)
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(MaxPool)
```

```c
when "padding" is "SAME":
out_height = (in_height + stride_h - 1) / stride_h
out_width = (in_width + stride_w - 1) / stride_w
when "padding" is "VALID":
out_height = (in_height + stride_h - ksize_h) / stride_h
out_width = (in_width + stride_w - ksize_w) / stride_w
It not support out_height < 0 or out_width < 0.
```

## Brief

Performs max pooling on the input .

## Inputs

One input:
x: A 4-D Tensor. Supported type:float16, float32, double, int8, int16,
int32, int64, uint8, uint16, qint8. Supported format: NHWC, NCHW.

## Outputs

y: A 4-D Tensor. Has the same type and format as input "x" . 

## Attributes

- ksize: A required list of int8, int16, int32, or int64 values,
specifying the size of the window for each dimension of the input tensor.
No default value.
- strides: A required list of int8, int16, int32, or int64 values,
specifying the stride of the sliding window for each dimension of
the input tensor. No default value.
- padding: A required string. Supported modes: SAME, VALID. No default value.
when padding is "SAME": pads 0 to ensure output shape equal to ceil(input shape / stride) ,
(output shape equal to input shape when stride=1). 
when padding is "VALID": no padding. The kernel slides only over valid regions, resulting in smaller output .
- data_format: An optional string. Supported format: NHWC, NCHW. Defaults to "NHWC" .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- output0 y: float16
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,qint8,uint8,uint16
- output0 y: double,float16,float32,int8,int16,int32,int64,qint8,uint8,uint16

## Attention Constraints

- "ksize" is a list that has length 4. The ksize of the H and W dimensions should be greater than 0.
The ksize of the N and C dimensions should be 1. e.g. For "data_format" is "NCHW", ksize[0] = 1 and ksize[1] = 1.
For "data_format" is "NHWC", ksize[0] = 1 and ksize[3] = 1. 
For Non-Ascend 950 AI Processor: The produce of the ksize in H and W dimensions
should be less than or equal to 255. e.g. For "data_format" is "NCHW", ksize[2] * ksize[3] <= 255. 
- "strides" is a list that has length 4. The stride of the N and C dimensions should be 1.
For Non-Ascend 950 AI Processor: The stride of the H and W dimensions should be greater than 0 and
smaller than 64. 
For Ascend 950 AI Processor: The stride of the H and W dimensions should be greater than 0.
- The ouput "y" shape at the N and C dimensions should be equal with input "x" shape at same dimensions. The output
shape at the H and W dimensions is calculated by below formula: 

## Third-party framework compatibility

Compatible with the TensorFlow operator MaxPool.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
