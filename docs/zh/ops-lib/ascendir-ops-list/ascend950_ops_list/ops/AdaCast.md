# AdaCast

```c
REG_OP(AdaCast)
    .INPUT(x, "T1")
    .OUTPUT(y, "T2")
    .ATTR(pixel, Int, 65535)
    .DATATYPE(T1, TensorType({DT_UINT16}))
    .DATATYPE(T2, TensorType({DT_FLOAT16}))
    .OP_END_FACTORY_REG(AdaCast)
```

## Brief

AdaCast: uint16 → float16 cast with pixel normalization for HDRnet.
  y = Cast_FP16(Cast_FP32(int32(uint32(x))) × (1/pixel))

## Inputs

- x: A ND Tensor of type uint16, rank 1~4. HDR image data.

## Outputs

- y: A ND Tensor of type float16, shape identical to x. Normalized result.

## Attributes

- pixel: Int, default 65535. White level normalization base (positive integer).

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: uint16
- output0 y: float16


---

[Back to Operator Specifications (Ascend950)](../README.md)
