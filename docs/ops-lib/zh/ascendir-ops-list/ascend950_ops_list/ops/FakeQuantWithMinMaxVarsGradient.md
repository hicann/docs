# FakeQuantWithMinMaxVarsGradient

```c
REG_OP(FakeQuantWithMinMaxVarsGradient)
    .INPUT(gradients, TensorType({DT_FLOAT}))
    .INPUT(x, TensorType({DT_FLOAT}))
    .INPUT(min, TensorType({DT_FLOAT}))
    .INPUT(max, TensorType({DT_FLOAT}))
    .OUTPUT(backprops_wrt_x, TensorType({DT_FLOAT}))
    .OUTPUT(backprops_wrt_min, TensorType({DT_FLOAT}))
    .OUTPUT(backprops_wrt_max, TensorType({DT_FLOAT}))
    .ATTR(num_bits, Int, 8)
    .ATTR(narrow_range, Bool, false)
    .OP_END_FACTORY_REG(FakeQuantWithMinMaxVarsGradient)
```

## Brief

Computes gradients for a FakeQuantWithMinMaxVars operation.

## Inputs

Four inputs, including:
- gradients: A ND Tensor of type float32. Shape support 1D ~ 8D.
- x: A ND Tensor of type float32. Shape support 1D ~ 8D.
Has the same shape as "gradients".
- min: A ND Tensor of type float32. Shape must be 1D.
- max: A ND Tensor of type float32. Shape must be 1D.

## Outputs

- backprops_wrt_x: A ND Tensor. Has the same dtype as input "x".
Shape support 1D ~ 8D. Has the same shape as input "x".
- backprops_wrt_min: A ND Tensor. Has the same dtype as input "min". Shape must be 1D.
- backprops_wrt_max: A ND Tensor. Has the same dtype as input "max". Shape must be 1D.

## Attributes

- num_bits: An optional attribute specifying the quantization bit width. Type is int. Defaults to "8".
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

## Attention Constraints

- "gradients" has the same shape as "x".
- "min" and "max" are scalars.
- "num_bits" is between 2 and 16
@see Region()

## Third-party framework compatibility

Compatible with the operator FakeQuantWithMinMaxVarsGradient.


---

[Back to Operator Specifications (Ascend950)](../README.md)
