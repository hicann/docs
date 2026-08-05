# MaxPoolV3

```c
REG_OP(MaxPoolV3)
    .INPUT(x,TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32, DT_DOUBLE, DT_INT32, DT_INT64, DT_UINT8, DT_INT16, DT_INT8, DT_UINT16, DT_QINT8}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32, DT_DOUBLE, DT_INT32, DT_INT64, DT_UINT8, DT_INT16, DT_INT8, DT_UINT16, DT_QINT8}))
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .ATTR(padding_mode, String, "CALCULATED")
    .ATTR(pads, ListInt, {0,0,0,0})
    .ATTR(data_format, String, "NCHW")
    .ATTR(global_pooling, Bool, false)
    .ATTR(ceil_mode, Bool, false)
    .OP_END_FACTORY_REG(MaxPoolV3)
```

```c
When "global_pooling" is True:
out_height = 1
out_width = 1
When "global_pooling" is False:
when "padding_mode" is "SAME":
out_height = (in_height + stride_h - 1) / stride_h
out_width = (in_width + stride_w - 1) / stride_w
when "padding_mode" is "VALID":
out_height = (in_height + stride_h - ksize_h) / stride_h
out_width = (in_width + stride_w - ksize_w) / stride_w
when "padding_mode" is "CALCULATED":
if "ceil_mode" is False:
out_height = (in_height + pad_top + pad_bottom - ksize_h) / stride_h + 1
out_width = (in_width + pad_left + pad_right - ksize_w) / stride_w + 1
else :
out_height = (in_height + pad_top + pad_bottom - ksize_h + stride_h - 1) / stride_h + 1
out_width = (in_width + in_width + pad_right - ksize_w + stride_w - 1) / stride_w + 1
if  (out_height - 1) * stride_h >= in_height + pad_top :
out_height = out_height - 1
if  (out_width - 1) * stride_w >= in_width + in_width :
out_width = out_width - 1
It not support out_height < 0 or out_width < 0.
```

## Brief

Performs max pooling on the input . 

## Inputs

One input:
x: A 4-D tensor. Supported type:float16, bfloat16, float32, double, int32, int64,
uint8, int16, int8, uint16, qint8. Supported format: NHWC, NCHW.

## Outputs

y: A 4-D tensor. Has the same type and format as input "x" . 

## Attributes

- ksize: A required list of int8, int16, int32, or int64 values,
specifying the size of the window for each dimension of the input tensor.
No default value.
- strides: A required list of int8, int16, int32, or int64 values,
specifying the stride of the sliding window for each dimension of
the input tensor. No default value.
- padding_mode: An optional string. Supported modes: SAME, VALID, CALCULATE. Defaults to "CALCULATED".
when padding_mode is "SAME": pads 0 to ensure output shape equal to ceil(input shape / stride) ,
(output shape equal to input shape when stride=1). 
when padding_mode is "VALID": no padding. The kernel slides only over valid regions, resulting in smaller output . 
when padding_mode is "CALCULATED": use pads to calculate output shape.
- pads: An optional list of int8, int16, int32, or int64 values.
It must have 4 elements, specifying the top, bottom, left, and right padding for input tensor.
The pads should be greater than or equal to 0 and smaller than the corresponding kernel size.
It only takes effect when padding_mode is "CALCULATED". Default value is {0,0,0,0}.
- data_format: An optional string, specify the data format of the input and
output data. Supported format: NHWC, NCHW. Defaults to "NCHW" .
- global_pooling bool, whether to use the global pooling.
If global_pooling = true, kernel size and paddings will be ignored.
Default False.
- ceil_mode: Whether to use the ceil function to calculate output
height and width. If it is set to False, the floor function will be used.
When the padding_mode is "SAME" and "VALID", it only support False.
Default False 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Attention Constraints

- "ksize" is a list that has length 4. The ksize of the H and W dimensions should be greater than 0.
The ksize of the N and C dimensions should be 1. e.g. For "data_format" is "NCHW", ksize[0] = 1 and ksize[1] = 1.
For "data_format" is "NHWC", ksize[0] = 1 and ksize[3] = 1.  
For Atlas Training Series Product, Atlas A2 Training Series Product/Atlas 800I A2 Inference Product,
Atlas A3 Training Series Product: The produce of the ksize in H and W dimensions
should be less than or equal to 255. e.g. For "data_format" is "NCHW", ksize[2] * ksize[3] <= 255. 
- "strides" is a list that has length 4. The stride of the N and C dimensions should be 1.
For Atlas Training Series Product, Atlas A2 Training Series Product/Atlas 800I A2 Inference Product,
Atlas A3 Training Series Product: The stride of the H and W dimensions should be greater than 0 and
smaller than 64.  
For Ascend 950 AI Processor: The stride of the H and W dimensions should be greater than 0.
- The ouput "y" shape at the N and C dimensions should be equal with input "x" shape at same dimensions. The output
shape at the H and W dimensions is calculated by below formula: 

## Third-party framework compatibility

Compatible with the TensorFlow operator MaxPool.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
