# AvgPoolV2Grad

```c
REG_OP(AvgPoolV2Grad)
    .INPUT(orig_input_shape, TensorType({DT_INT32}))
    .INPUT(input_grad, TensorType({DT_FLOAT16, DT_FLOAT32, DT_DOUBLE, DT_BF16}))
    .OUTPUT(out_grad, TensorType({DT_FLOAT16, DT_FLOAT32, DT_DOUBLE, DT_BF16}))
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .ATTR(padding_mode, String, "CALCULATED")
    .ATTR(pads, ListInt, {0,0,0,0})
    .ATTR(data_format, String, "NCHW")
    .ATTR(global_pooling, Bool, false)
    .ATTR(ceil_mode, Bool, false)
    .ATTR(exclusive, Bool, true)
    .ATTR(divisor_override, Int, 0)
    .OP_END_FACTORY_REG(AvgPoolV2Grad)
```

## Brief

Computes avgpoolv2grad function.

## Inputs

- orig_input_shape: An NHWC tensor of type int32.
- input_grad: An NHWC tensor of type float16, float32 or double.

## Outputs

- out_grad: A mutable tensor with the same shape and type as "orig_input_shape".
    input_grad_height = (out_grad_height + pads_top + pads_bottom - ksize_height)
                          / strides_h + 1
    input_grad_width = (out_grad_width + pads_left + pads_right - ksize_width)
                         / strides_w + 1

## Attributes

- ksize: A required tuple or list of ints,
specifying the size of the window for each dimension of the input tensor.
- strides: A required tuple or list of ints,
specifying the stride of the sliding window for each dimension of the input tensor.
- padding_mode: An optional string, specifying the type of the padding algorithm to use,
either "VALID", "SAME" or "CALCULATED". Default "CALCULATED".
With "SAME" means that the outputs will have the same spatial dimensions as its inputs.
With "VALID" means no padding.
- pads: An optional list of ints, specifying the pad of the input feature map.
Default value {0,0,0,0}.
- global_pooling: An optional bool, whether to use the global pooling. If global_pooling =
true, ksize and pads will be ignored. Default False.
- ceil_mode: An optional bool, whether to use the ceil function to calculate output height
and width. Default False.
- exclusive: An optional bool, whether to exclude padding points. Default is true.
- data_format: An optional string. Defaults to "NCHW".
- divisor_override: An optional int, the default value is zero.
if specified, it will be used as divisor, otherwise size of the pooling region will be used.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_grad: float16
- input3 orig_input_shape: int64
- output0 out_grad: float16

## Third-party framework compatibility

- Compatible with the TensorFlow operator AvgPoolGrad.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
