# Upsample

```c
REG_OP(Upsample)
   .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
   .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
   .ATTR(scale, Float, 1)
   .ATTR(stride_h, Int, 2)
   .ATTR(stride_w, Int, 2)
   .OP_END_FACTORY_REG(Upsample)
```

## Brief

Upsample the layer, similar to the nearest-neighbor
difference scaling algorithm.

## Inputs

one input, including:
x: A tensor of type float16 or float32. Supported format "NC1HWC0".
Shape support 5D.

## Outputs

y: A tensor of type float16 or float32. Has same dtype as "x".
Supported format "NC1HWC0". Shape support 5D.

## Attributes

- scale: A optional float32, scale factor of x. Defaults to "1".
- stride_h: An optional int, broadcast the axis of h. Defaults to "2".
- stride_w: An optional int, broadcast the axis of w. Defaults to "2".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
