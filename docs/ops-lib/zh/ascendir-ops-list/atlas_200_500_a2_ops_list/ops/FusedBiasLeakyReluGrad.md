# FusedBiasLeakyReluGrad

```c
REG_OP(FusedBiasLeakyReluGrad)
    .INPUT(y_grad, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(features, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .ATTR(negative_slope, Float, 0.2f)
    .ATTR(scale, Float, 1.414213562373f)
    .OUTPUT(x_grad, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(FusedBiasLeakyReluGrad)
```

## Brief

Computes the output as scale * gradients if features > 0 and
negative_slope * gradients * scale if features <= 0 . 

## Inputs

Two inputs, including:
- y_grad: A Tensor. Must be one of the following types: float16, float32, double.
- features: A Tensor. Has the same type as "gradients" .

## Outputs

x_grad: A Tensor. Has the same type as "y_grad" . 

## Attributes

negative_slope: A float32. Defaults to "0.2" . 
scale : A float32. Defaults to "2**0.5"

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y_grad: float16,float32
- input1 features: float16,float32
- output0 x_grad: float16,float32

## Third-party framework compatibility

Compatible with the MMCV operator FusedBiasLeakyReluGrad.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
