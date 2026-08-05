# FakeQuantWithMinMaxArgs

```c
REG_OP(FakeQuantWithMinMaxArgs)
    .INPUT(x, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .ATTR(min, Float, -6.0)
    .ATTR(max, Float, 6.0)
    .ATTR(num_bits, Int, 8)
    .ATTR(narrow_range, Bool, false)
    .OP_END_FACTORY_REG(FakeQuantWithMinMaxArgs)
```

## Brief

Fake-quantizes the input Tensor, type float to output a Tensor of same type.
 [min, max] define the clamping range for the "inputs" data.
 The values of "x" are quantized into the quantization range ([0, 2^num_bits - 1]
 when "narrow_range" is "false" or [1, 2^num_bits - 1] when it is "true") and
 then de-quantized and output as float32 in [min; max] interval.
 "num_bits" is the bit width of the quantization, between 2 and 16, inclusive.
 Quantization is called fake since the output is still in floating point. 

## Inputs

One input:
x: A ND Tensor of type float32. Shape support 1D ~ 8D. 

## Outputs

y: A ND Tensor of type float32. Shape support 1D ~ 8D.
Has the same shape and type of "x". 

## Attributes

- min: An optional attribute. Type is float. Defaults to "-6.0".
- max: An optional attribute. Type is float. Defaults to "6.0".
- num_bits: An optional attribute. Type is float. Defaults to "8".
- narrow_range: An optional attribute. Type is bool. Defaults to "false".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float32
- output0 y: float32

## Third-party framework compatibility

Compatible with TensorFlow operator FakeQuantWithMinMaxArgs.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
