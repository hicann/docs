# EluGrad

```c
REG_OP(EluGrad)
    .INPUT(grads, TensorType({FloatingDataType, DT_BF16}))
    .INPUT(activations, TensorType({FloatingDataType, DT_BF16}))
    .OUTPUT(y, TensorType({FloatingDataType, DT_BF16}))
    .OP_END_FACTORY_REG(EluGrad)
```

## Brief

Computes gradients for the exponential linear (Elu) operation.

## Inputs

- grads: An ND or 5HD tensor. Support 1D~8D. Must be one of the following types:
bfloat16, float16, float32, float64.
The backpropagated gradients to the corresponding Elu operation.
- activations: A tensor. Has the same type, format and shape as "grads".
The outputs of the corresponding Elu operation.

## Outputs

y: A tensor. Has the same type, format and shape as "grads".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grads: bfloat16,float16,float32
- input1 activations: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 grads: double,float16,float32
- input1 activations: double,float16,float32
- output0 y: double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator EluGrad.


---

[Back to Operator Specifications (Ascend950)](../README.md)
