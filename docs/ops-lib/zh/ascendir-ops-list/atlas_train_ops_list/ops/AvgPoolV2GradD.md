# AvgPoolV2GradD

```c
REG_OP(AvgPoolV2GradD)
    .INPUT(input_grad, TensorType({DT_FLOAT16}))
    .OPTIONAL_INPUT(mean_matrix, TensorType({DT_FLOAT16}))
    .OPTIONAL_INPUT(kernel_matrix, TensorType({DT_FLOAT16}))
    .OUTPUT(out_grad, TensorType({DT_FLOAT16}))
    .REQUIRED_ATTR(orig_input_shape, ListInt)
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .ATTR(padding_mode, String, "CALCULATED")
    .ATTR(pads, ListInt, {0,0,0,0})
    .ATTR(data_format, String, "NCHW")
    .ATTR(global_pooling, Bool, false)
    .ATTR(ceil_mode, Bool, false)
    .ATTR(exclusive, Bool, true)
    .OP_END_FACTORY_REG(AvgPoolV2GradD)
```

## Brief

Computes gradients of averagev2 pooling function.

## Inputs

- input_grad: An NHWC tensor of type float16.
- mean_matrix: Assist matrix, an NHWC tensor of type float16.
- kernel_matrix: Assist matrix, an NHWC tensor of type float16.

## Outputs

out_grad: A mutable tensor with the same shape and type as "orig_input_shape".
    input_grad_height = (out_grad_height + pads_top + pads_bottom - ksize_height)
                          / strides_h + 1
    input_grad_width = (out_grad_width + pads_left + pads_right - ksize_width)
                         / strides_w + 1

## Attributes

- orig_input_shape: A required tuple or list of type int32.
- ksize: A required tuple or list, specifying the size of the window for
each dimension of the input tensor.
- strides: A required tuple or list, specifying the stride of the sliding
window for each dimension of the input tensor.
- padding_mode: An optional string, specifying the type of the padding algorithm to use,
either "VALID", "SAME" or "CALCULATED". Default "CALCULATED".
With "SAME" means that the outputs will have the same spatial dimensions as its inputs.
With "VALID" means no padding.
- pads: An optional list of ints, specifying the pad of the input feature map.
Default value {0,0,0,0}.
- global_pooling: Whether to use the global pooling. If global_pooling=true,
ksize and pads will be ignored. Default False.
- ceil_mode: Whether to use the ceil function to calculate output height and
width. Default False.
- exclusive: Whether to exclude padding points. default is true.
- data_format: An optional string. Defaults to "NCHW".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_grad: float16
- input1 mean_matrix: float16
- input2 kernel_matrix: float16
- output0 out_grad: float16

## Attention Constraints

The operator will not be enhanced in the future.

## Third-party framework compatibility

Compatible with the TensorFlow operator AvgPoolGrad.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
