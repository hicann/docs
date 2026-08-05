# LRNGrad

```c
REG_OP(LRNGrad)
    .INPUT(grads, TensorType({DT_FLOAT16,DT_FLOAT}))
    .INPUT(x, TensorType({DT_FLOAT16,DT_FLOAT}))
    .INPUT(y, TensorType({DT_FLOAT16,DT_FLOAT}))
    .OUTPUT(z, TensorType({DT_FLOAT16,DT_FLOAT}))
    .ATTR(depth_radius, Int, 5)
    .ATTR(bias, Float, 1.0)
    .ATTR(alpha, Float, 1.0)
    .ATTR(beta, Float, 0.5)
    .OP_END_FACTORY_REG(LRNGrad)
```

## Brief

Computes the gradient for Local Response Normalization .

## Inputs

- grads: A 4D Tensor of type float16 or float32.
- x: A 4D Tensor of type float16 or float32.
- y: A 4D Tensor of type float16 or float32 .

## Outputs

z: A Tensor. Has the same type and shape as "grads" .

## Attributes

- depth_radius: An optional int, specifying the half-width of the
normalization window. Defaults to "5".
- bias: An optional float32. An offset, usually > 0 to avoid dividing by 0.
Defaults to "1".
- alpha: An optional float32. A scaling factor, usually positive.
Defaults to "1".
- beta: An optional float32. An exponent. Defaults to "0.5" .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grads: float16,float32
- input1 x: float16,float32
- input2 y: float16,float32
- output0 z: float16,float32

## Attention Constraints

"x" and "y" must have the same shape and type as "grads" .

## Third-party framework compatibility

Compatible with the TensorFlow operator LRNGrad.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
