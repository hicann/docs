# AvgPool3DGradD

```c
REG_OP(AvgPool3DGradD)
    .INPUT(grads, TensorType({DT_FLOAT16}))
    .OPTIONAL_INPUT(filter, TensorType({DT_FLOAT16}))
    .OPTIONAL_INPUT(multiplier, TensorType({DT_FLOAT16}))
    .OUTPUT(output, TensorType({DT_FLOAT16}))
    .REQUIRED_ATTR(orig_input_shape, ListInt)
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(ceil_mode, Bool, false)
    .ATTR(count_include_pad, Bool, true)
    .ATTR(divisor_override, Int, 0)
    .ATTR(data_format, String, "NDHWC")
    .OP_END_FACTORY_REG(AvgPool3DGradD)
```

## Brief

Performs average pooling on the input.

## Inputs

- grads: An NDHWC tensor of type float16.
- filter: An optional tensor of type float16.
- multiplier: An optional tensor of type float16.

## Outputs

output: The average pooled output tensor with the same type as
input grads and same shape as orig_input_shape. 

## Attributes

- orig_input_shape: List of ints that has length 5.
The size of each dimension of the original input.
- ksize: List of ints that has length 5.
The size of the window for each dimension of the input tensor.
- strides:List of ints that has length 5.
The stride of the sliding window for each dimension of the input tensor.
- pads: List of ints, implicit zero paddings on both sides of the input.
- ceil_mode: An optional Boolean value. When true, will use ceil instead of floor
in the formula to compute the output shape. Defaults to false.
- count_include_pad:  An optional Boolean value. When true,
will include the zero-padding in the averaging calculation. Defaults to true.
- divisor_override:  An optional Boolean value. if specified, it will be used as divisor,
otherwise size of the pooling region will be used. Defaults to false.
- data_format: A string, format of input data. Defaults to "NDHWC"

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grads: float16
- input1 filter: float16
- input2 multiplier: float16
- output0 output: float16

## Attention Constraints

"ksize" is in the range [1, 255]. "strides" is in the range [1, 63]. 
The operator will not be enhanced in the future.

## Third-party framework compatibility

Compatible with the TensorFlow operator AvgPool3DGradD. 


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
