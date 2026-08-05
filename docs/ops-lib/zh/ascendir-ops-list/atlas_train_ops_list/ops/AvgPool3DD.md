# AvgPool3DD

```c
REG_OP(AvgPool3DD)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OPTIONAL_INPUT(filter, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OPTIONAL_INPUT(multiplier, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(ceil_mode, Bool, false)
    .ATTR(count_include_pad, Bool, true)
    .ATTR(divisor_override, Int, 0)
    .ATTR(data_format, String, "NDHWC")
    .OP_END_FACTORY_REG(AvgPool3DD)
```

## Brief

Performs 3D average pooling on the input.

## Inputs

- x: A 5-D Tensor of shape [batch, depth, height, width, channels].
Support type float16, float32 and double.
- filter: An optional tensor of type float16, float32 or double, FRACTAL_Z_3D layout.
- multiplier: An optional tensor of float16, float32 or double.

## Outputs

y: The average pooled output tensor with the same type and format as input "x". 

## Attributes

- ksize: List of ints that has length 1, 3 or 5.
The size of the window for each dimension of the input x tensor.
- strides:List of ints that has length 1, 3 or 5.
The stride of the sliding window for each dimension of the input tensor.
- pads: List of ints, implicit zero paddings on both sides of the input.
- ceil_mode: An optional Boolean value. When true, will use ceil
instead of floor in the formula to compute the output shape. Defaults to false.
- count_include_pad: An optional Boolean value. When true,
will include the zero-padding in the averaging calculation. Defaults to false.
- divisor_override: An optional Boolean value. if specified, it will be used as divisor,
otherwise size of the pooling region will be used. Defaults to 0.
- data_format: A string, format of input data. Defaults to "NDHWC".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- input1 filter: float16
- input2 multiplier: float16
- output0 y: float16

## Attention Constraints

"ksize" is in the range [1, 255]. "strides" is in the range [1, 63] 
The operator will not be enhanced in the future. 

## Third-party framework compatibility

Compatible with the TensorFlow operator AvgPool3D. 


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
