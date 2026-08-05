# Relu6D

```c
REG_OP(Relu6D)
    .INPUT(x, TensorType::RealNumberType())
    .OUTPUT(y, TensorType::RealNumberType())
    .ATTR(scale, Float, 1.0)
    .OP_END_FACTORY_REG(Relu6D)
```

## Brief

Relu6D: elementwise Relu6 with scale. y = min(max(x, 0), 6*scale).

## Inputs

One input, including:
 @li x: A Tensor. Must be one of RealNumberType. Layout ND.

## Outputs

 @li y: A Tensor. Same type and shape as input x, value range [0, 6*scale].

## Attributes

 @li scale: Float. Threshold scale factor; upper bound = 6*scale. Default: 1.0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int32
- output0 y: float16,float32,int32

## Third-party framework compatibility

Compatible with the CANN Relu6D operator (Relu6 with private scale extension).


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
