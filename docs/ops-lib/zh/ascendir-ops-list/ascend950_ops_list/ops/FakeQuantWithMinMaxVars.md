# FakeQuantWithMinMaxVars

```c
REG_OP(FakeQuantWithMinMaxVars)
    .INPUT(x, TensorType({DT_FLOAT}))
    .INPUT(min, TensorType({DT_FLOAT}))
    .INPUT(max, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .ATTR(num_bits, Int, 8)
    .ATTR(narrow_range, Bool, false)
    .OP_END_FACTORY_REG(FakeQuantWithMinMaxVars)
```

## Brief

Fake-quantize the 'inputs' tensor of type float via global float scalars.

## Inputs

Three inputs, including:
- x: A ND Tensor of type float32. Shape support 1D ~ 8D.
- min: A ND Tensor of type float32. Has the same dtype and format as "x".
Shape must be 1D.
- max: A ND Tensor of type float32. Has the same dtype and format as "x".
[min; max] define the clamping range for the inputs data. Shape must be 1D. 

## Outputs

y: A ND Tensor of type float32. Shape support 1D ~ 8D. Has the same shape as input "x". 

## Attributes

- num_bits: An optional attribute. Type is int. Defaults to "8".
- narrow_range: An optional attribute. Type is bool. Defaults to "False".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float32
- input1 min: float32
- input2 max: float32
- output0 y: float32

## Third-party framework compatibility

Compatible with TensorFlow operator FakeQuantWithMinMaxVars.


---

[Back to Operator Specifications (Ascend950)](../README.md)
