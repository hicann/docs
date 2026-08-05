# FakeQuantWithMinMaxArgsGradient

```c
REG_OP(FakeQuantWithMinMaxArgsGradient)
    .INPUT(gradients, TensorType({DT_FLOAT}))
    .INPUT(x, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .ATTR(min, Float, -6.0)
    .ATTR(max, Float, 6.0)
    .ATTR(num_bits, Int, 8)
    .ATTR(narrow_range, Bool, false)
    .OP_END_FACTORY_REG(FakeQuantWithMinMaxArgsGradient)
```

## Brief

Computes gradients for a FakeQuantWithMinMaxArgs operation.

## Inputs

Two inputs, including:
- gradients: A ND Tensor of type float32. Shape support 1D ~ 8D. Backpropagated gradients above the FakeQuantWithMinMaxArgs operation.
- x: A ND Tensor of type float32. Shape support 1D ~ 8D. Shape should be equal to the shape of "gradients". Has the same dtype and format as "gradients".
This is the input Tensor of the FakeQuantWithMinMaxArgs operator.

## Outputs

y: A ND Tensor of type float32. Shape support 1D ~ 8D. Shape should be equal to the shape of "gradients".

## Attributes

- min: An optional attribute. Type is float. Defaults to "-6.0".
- max: An optional attribute. Type is float. Defaults to "6.0".
- num_bits: An optional attribute. Type is int. Defaults to "8".
- narrow_range: An optional attribute. Type is bool. Defaults to "False".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 gradients: float32
- input1 x: float32
- output0 y: float32

## Third-party framework compatibility

Compatible with TensorFlow operator FakeQuantWithMinMaxArgsGradient.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
