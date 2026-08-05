# AvgPool

```c
REG_OP(AvgPool)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BF16, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BF16, DT_DOUBLE}))
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(padding, String)
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(AvgPool)
```

```c
when "padding_mode" is "SAME":
out_height = (in_height + stride_h - 1) / stride_h
out_width = (in_width + stride_w - 1) / stride_w
when "padding_mode" is "VALID":
out_height = (in_height + stride_h - ksize_h) / stride_h
out_width = (in_width + stride_w - ksize_w) / stride_w
It not support out_height < 0 or out_width < 0.
```

## Brief

Performs average pooling on the input.

## Inputs

x: A tensor of shape [N, C, H, W] or [N, H, W, C] which supports data type float16, float32, bfloat16, double. 

## Outputs

y: The average pooled output tensor. Has the same type and format
as input "x". 

## Attributes

- ksize: A required list of 4 ints, specifying the size of the sliding window,
The ksize of the N and C dimensions are 1.
- strides: A required list of 4 ints, specifying the stride of the
sliding window. The strides of the N and C dimensions are 1.
- padding: A required string, specifying the padding algorithm,
either "VALID" or "SAME". With "SAME" means that the outputs will have the
same spatial dimensions as its inputs. With "VALID" means no padding.
- data_format: An optional string, specifying the data format of "ksize"
and "strides", either "NCHW", or "NHWC" (default). 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,int8
- output0 y: float16,int32
### AI CPU
- input0 x: double,float16,float32
- output0 y: double,float16,float32

## Attention Constraints

- This operator applies only to a TensorFlow network.
- Only single input and single output are supported.
- For Atlas Training Series Product, Atlas A2 Training Series Product/Atlas 800I A2 Inference Product,
Atlas A3 Training Series Product: "ksize_H" and "ksize_W" are positive integers within the range [1, 255].
ksize_H * ksize_W < 256. 
For Ascend 950 AI Processor: The ksize of the H and W dimensions should be greater than 0.
- For Atlas Training Series Product, Atlas A2 Training Series Product/Atlas 800I A2 Inference Product,
Atlas A3 Training Series Product: the values of "strides_h" and "strides_w" are positive integers within
the range [1, 63]. 
For Ascend 950 AI Processor: The stride of the H and W dimensions should be greater than 0.
- When the C axis is greater than 1, if points with the same H and W dimensions in x contain one INF input
on the C axis, the output of the INF input covered by the sliding window on this C axis is INF, and the
outputs of other C axis without INF input covered by the sliding window are Nan. If points with the same
H and W dimensions in x contain more than one INF input on the C axis, the outputs of all INF input data
covered by the sliding window on the C axis are Nan. this constraints not for Ascend 950 AI Processor.
- The ouput "y" shape at the N and C dimensions should be equal with input "x" shape at same dimensions. The output
shape at the H and W dimensions is calculated by below formula: 

## Third-party framework compatibility

Compatible with the TensorFlow operator AvgPool.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
