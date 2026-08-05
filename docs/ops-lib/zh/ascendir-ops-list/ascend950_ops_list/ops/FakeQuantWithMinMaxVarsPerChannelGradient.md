# FakeQuantWithMinMaxVarsPerChannelGradient

```c
REG_OP(FakeQuantWithMinMaxVarsPerChannelGradient)
    .INPUT(gradients, TensorType({DT_FLOAT}))
    .INPUT(x, TensorType({DT_FLOAT}))
    .INPUT(min, TensorType({DT_FLOAT}))
    .INPUT(max, TensorType({DT_FLOAT}))
    .OUTPUT(backprops_wrt_x, TensorType({DT_FLOAT}))
    .OUTPUT(backprops_wrt_min, TensorType({DT_FLOAT}))
    .OUTPUT(backprops_wrt_max, TensorType({DT_FLOAT}))
    .ATTR(num_bits, Int, 8)
    .ATTR(narrow_range, Bool, false)
    .OP_END_FACTORY_REG(FakeQuantWithMinMaxVarsPerChannelGradient)
```

## Brief

Computes gradients for a FakeQuantWithMinMaxVarsPerChannel operation.

## Inputs

Four inputs, including:
- gradients: A ND Tensor of type float32. Shape support 1D ~ 8D.
Has the same last dimension size as "x".
- x: A ND Tensor of type float32. Shape support 1D ~ 8D.
Has the same shape as "gradients".
- min: A ND Tensor of type float32. Shape must be 1D.
Has the same last dimension size as "x".
- max: A ND Tensor of type float32. Shape must be 1D.
Has the same last dimension size as "x". 

## Outputs

- backprops_wrt_x: A ND Tensor of type float32. Shape support 1D ~ 8D.
Has the same dtype and shape as input "x".
- backprops_wrt_min: A ND Tensor of type float32.
Shape must be 1D. Has the same dtype as input "min".
- backprops_wrt_max: A ND Tensor of type float32.
Shape must be 1D. Has the same dtype as input "max". 

## Attributes

- num_bits: An optional attribute specifying the quantization bit width.
Type is int. Defaults to "8".
- narrow_range: An optional attribute specifying whether to use a narrow range for quantization.
Type is bool. Defaults to "False". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 gradients: float32
- input1 x: float32
- input2 min: float32
- input3 max: float32
- output0 backprops_wrt_x: float32
- output1 backprops_wrt_min: float32
- output2 backprops_wrt_max: float32

## Attention Constraints

- "gradients" has the same shape as "x".
- "min" and "max" have one-dimensional shapes.
- "min" has the same last dimension size as "x". "max" has the same last dimension size as "x". "gradients" has the same last dimension size as "x".
- "num_bits" is between 2 and 16.
@see Region()

## Third-party framework compatibility

Compatible with the TensorFlow operator FakeQuantWithMinMaxVarsPerChannelGradient.


---

[Back to Operator Specifications (Ascend950)](../README.md)
