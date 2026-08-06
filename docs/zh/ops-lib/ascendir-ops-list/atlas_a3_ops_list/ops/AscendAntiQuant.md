# AscendAntiQuant

```c
REG_OP(AscendAntiQuant)
    .INPUT(x, TensorType({DT_INT8, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(scale, Float)
    .REQUIRED_ATTR(offset, Float)
    .ATTR(dtype, Int, DT_FLOAT)
    .ATTR(sqrt_mode, Bool, false)
    .OP_END_FACTORY_REG(AscendAntiQuant)
```

## Brief

Per-tensor anti-quantization with scalar scale / offset attributes.
  y = cast\<TOut>((x + offset) * scale)              when sqrt_mode == false
  y = cast\<TOut>((x + offset) * scale * scale)      when sqrt_mode == true

## Inputs

- x: A tensor. Type is one of DT_INT8, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN.

## Outputs

- y: A tensor. Type is one of DT_FLOAT16, DT_FLOAT. Shape is the same as x.

## Attributes

- scale: Required float. Per-tensor scale value.
- offset: Required float. Per-tensor offset value.
- dtype: Optional int, output dtype. Defaults to DT_FLOAT (0). Allowed: DT_FLOAT16 (1), DT_FLOAT (0).
- sqrt_mode: Optional bool. Defaults to false.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
