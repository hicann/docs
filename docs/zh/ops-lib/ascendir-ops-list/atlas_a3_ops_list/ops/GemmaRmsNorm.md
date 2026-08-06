# GemmaRmsNorm

```c
REG_OP(GemmaRmsNorm)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(gamma, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(rstd, TensorType({DT_FLOAT, DT_FLOAT, DT_FLOAT}))
    .ATTR(epsilon, Float, 1e-6f)
    .OP_END_FACTORY_REG(GemmaRmsNorm)
```

## Brief

GemmaRmsNorm operator interface implementation. 
 calculating: x, gamma 
 rstd = np.rsqrt(np.mean(np.power(x, 2), reduce_axis, keepdims=True) + epsilon)) 
 y = (1 + gamma) * (x * rstd)

## Inputs

Two inputs, including:
- x: A tensor of input. Represens the input data to be normalized. The format must be ND. Shape support 1D ~ 8D.
Must be one of the following types: float16, float32, bfloat16.
- gamma: A tensor of input. Represents a learnable scaling factor.
Must be one of the following types: float16, float32, bfloat16. Must have the same type as "x".
The format must be ND. Shape support 1D ~ 8D.
The shape must meet the requirements of gamma_shape = x_shape[n:], n < x_shape.dims().

## Outputs

Two outputs, including:
- y: A tensor of output. Indicates normalized data. The format must be ND. Shape support 1D ~ 8D.
Must be one of the following types: float16, float32, bfloat16. Must have the same type, format and shape as "x".
- rstd: A tensor of output. Represents root mean square. The format must be ND. The type is float32.
The shape is the same as the first several dimensions of the "x" shape.
The first several dimensions refer to the dimension of "x" minus the dimension of "gamma",
indicating that the norm is not required.

## Attributes

epsilon: Optional attribute to prevent division by 0. The type is float32. Defaults to 1e-6.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 gamma: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
- output1 rstd: float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
