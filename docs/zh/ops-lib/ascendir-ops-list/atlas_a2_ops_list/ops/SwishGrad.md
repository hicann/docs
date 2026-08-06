# SwishGrad

```c
REG_OP(SwishGrad)
    .INPUT(grad, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(grad_x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(scale, Float, 1.0)
    .OP_END_FACTORY_REG(SwishGrad)
```

## Brief

Computes the gradient for the Swish of "x" .

## Inputs

Three inputs, including:
- grad: A tensor, which supports 1D-8D defaultly. Format support ND, NC1HWC0, FRACTAL_NZ and must be one of the
following types: float16, bfloat16, float32.
- x: A tensor of the same type, shape and format as "grad".
- y: A tensor of the same type, shape and format as "grad", and y = x / (1 + e ^ (-scale * x)).

## Outputs

grad_x: A tensor, which is the gradient of x. Has the same type, shape and format as "grad".

## Attributes

scale: An optional scalar, the multiplier of x. The data type is float, default value = 1.0. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad: bfloat16,float16,float32
- input1 x: bfloat16,float16,float32
- input2 y: bfloat16,float16,float32
- output0 grad_x: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the PyTorch operator SwishGrad.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
