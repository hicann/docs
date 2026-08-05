# FakeQuantWithMinMaxVarsPerChannel

```c
REG_OP(FakeQuantWithMinMaxVarsPerChannel)
    .INPUT(x, TensorType({DT_FLOAT}))
    .INPUT(min, TensorType({DT_FLOAT}))
    .INPUT(max, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .ATTR(num_bits, Int, 8)
    .ATTR(narrow_range, Bool, false)
    .OP_END_FACTORY_REG(FakeQuantWithMinMaxVarsPerChannel)
```

## Brief

Fake-quantizes the "inputs" tensor of type float
via per-channel floats min and max of shape [d] to "outputs" 
tensor of same shape as inputs

## Inputs

Three inputs, including:
- x: A ND Tensor of type float32. Shape support 1D ~ 8D.
- min: A ND Tensor of type float32. Shape must be 1D.
"min" has the same last dimension size as "x".
- max: A ND Tensor of type float32. Shape must be 1D.
"max" has the same last dimension size as "x". 

## Outputs

y: A ND Tensor of type float32. Shape support 1D ~ 8D.
Has the same dtype and shape as input "x".

## Attributes

- num_bits: An optional attribute specifying the quantization bit width.
Type is int. Defaults to "8".
- narrow_range: An optional attribute specifying whether to use a narrow range for quantization.
Type is bool. Defaults to "False". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float32
- input1 min: float32
- input2 max: float32
- output0 y: float32

## Attention Constraints

- "min" and "max" have one-dimensional shapes.
- "min" has the same last dimension size as "x". "max" has the same last dimension size as "x".
- "num_bits" is between 2 and 16
@see Region()

## Third-party framework compatibility

Compatible with the TensorFlow operator FakeQuantWithMinMaxVarsPerChannel.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
