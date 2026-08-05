# MVNV2

```c
REG_OP(MVNV2)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16}))
    .ATTR(eps, Float, 1e-9f)
    .ATTR(axes, ListInt, {0, 2, 3})
    .OP_END_FACTORY_REG(MVNV2)
```

## Brief

Normalizes the input .

## Inputs

One input:
x: An NCHW tensor of type float16 or float32 . 

## Outputs

y: An NCHW tensor of type float16 or float32 . 

## Attributes

- eps: An optional float32 epsilon for not dividing by zero. Defaults to "1e-9" .
- axes: A list of Intefers, along which axis to reduce. Defaults to "[0, 2, 3]" .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Attention Constraints

The input tensor must have the NCHW format, whose shape length must be 4.

## Third-party framework compatibility

Compatible with the ONNX operator MeanVarianceNormalization.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
