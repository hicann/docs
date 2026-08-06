# AvgPool3D

```c
REG_OP(AvgPool3D)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(ceil_mode, Bool, false)
    .ATTR(count_include_pad, Bool, true)
    .ATTR(divisor_override, Int, 0)
    .ATTR(data_format, String, "NDHWC")
    .OP_END_FACTORY_REG(AvgPool3D)
```

```c
if "ceil_mode" is False:
out_depth = (in_depth + pad_front + pad_backend - ksize_d) / stride_d + 1
out_height = (in_height + pad_top + pad_bottom - ksize_h) / stride_h + 1
out_width = (in_width + pad_left + pad_right - ksize_w) / stride_w + 1
else :
out_depth = (in_depth + pad_front + pad_backend - ksize_d + stride_d - 1) / stride_d + 1
out_height = (in_height + pad_top + pad_bottom - ksize_h + stride_h - 1) / stride_h + 1
out_width = (in_width + in_width + pad_right - ksize_w + stride_w - 1) / stride_w + 1
if  (out_depth - 1) * stride_d >= in_depth + pad_front :
out_depth = out_depth - 1
if  (out_height - 1) * stride_h >= in_height + pad_top :
out_height = out_height - 1
if  (out_width - 1) * stride_w >= in_width + in_width :
out_width = out_width - 1
It not support out_depth < 0, out_height < 0 or out_width < 0.
```

## Brief

Performs average pooling on the input.

## Inputs

x: A 5D tensor. Supported type:float16. Additional support for float32, bfloat16 in Ascend 950 AI Processor.
Support format: NDHWC. Additional support for NCDHW in Ascend 950 AI Processor. 

## Outputs

y: The average pooled output tensor. 

## Attributes

- ksize: List of ints that has length 1, 3 or 5. The size of the window
for each dimension of the input tensor.
- strides: List of ints that has length 1, 3 or 5. The stride of the sliding
window for each dimension of the input tensor.
- pads: List of ints that has length 1, 3 or 6, implicit zero paddings on both sides of each dimension
of the input tensor.
- ceil_mode: When true, will use ceil instead of floor in the formula to
compute the output shape. Default value is false.
- count_include_pad: When true, will include the zero-padding in the
averaging calculation. Default value is true.
- divisor_override: if specified, it will be used as divisor, otherwise
size of the pooling region will be used. Default value is 0.
- data_format: An optional string, format of input data. It supports "NDHWC"(default).
Additional support for "NCDHW" in Ascend 950 AI Processor. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- output0 y: float16

## Attention Constraints

- The ksize of the D, H and W dimensions should be greater than 0.
For Atlas Training Series Product, Atlas A2 Training Series Product/Atlas 800I A2 Inference Product,
Atlas A3 Training Series Product: The produce of the ksize in D, H and W dimensions
should be greater than 0 and less than or equal to 255.  
- For Atlas Training Series Product, Atlas A2 Training Series Product/Atlas 800I A2 Inference Product,
Atlas A3 Training Series Product: The stride of the D, H and W dimensions should be greater than 0 and
smaller than 64.  
For Ascend 950 AI Processor: The stride of the D, H and W dimensions should be greater than 0.
- The ouput "y" shape at the N and C dimensions should be equal with input "x" shape at same dimensions. The output
shape at the D, H and W dimensions is calculated by below formula: 

## Third-party framework compatibility

Compatible with the TensorFlow/Pytorch operator AvgPool3D.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
