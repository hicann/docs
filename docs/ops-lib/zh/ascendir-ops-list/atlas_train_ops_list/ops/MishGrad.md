# MishGrad

```c
REG_OP(MishGrad)
    .INPUT(grad, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .INPUT(x, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .OPTIONAL_INPUT(tanhx, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .OUTPUT(x_grad, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .OP_END_FACTORY_REG(MishGrad)
```

## Brief

PyTorch mish_grad operator.

## Inputs

Three input, including:
- grad: A tensor. Shape, datatype and format is the same as x.
- x: A tensor. Support 1D ~ 8D. Must be one of the following types: float16, float32, bfloat16. Format:ND.
- tanhx: A tensor. Shape, datatype and format is the same as x.

## Outputs

One output, including:
x_grad: A tensor. Shape, datatype and format is the same as x.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad: float16,float32
- input1 x: float16,float32
- input2 tanhx: float16,float32
- output0 x_grad: float16,float32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
