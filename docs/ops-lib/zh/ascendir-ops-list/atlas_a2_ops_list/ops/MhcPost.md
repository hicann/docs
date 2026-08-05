# MhcPost

```c
REG_OP(MhcPost)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(h_res, TensorType({DT_FLOAT}))
    .INPUT(h_out, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(h_post, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16}))
    .OP_END_FACTORY_REG(MhcPost)
```

## Brief

Fuse the main branch feature h_out with the residual branch feature x
using the gating mechanism h_post and the doubly stochastic matrix  h_res
to enable information flow.

## Inputs

- x: A Tensor, dtype is bfloat16 or float16. Represents input data in the mHC layer.
Dataformat:ND. Supports 3D (Shape:[T, n, D]) or 4D (Shape:[B, S, n, D]) tensors.
- h_res: A Tensor, dtype is float32. Represents the h_res transformation matrix.
Dataformat:ND. Supports 3D (Shape:[T, n, n]) or 4D (Shape:[B, S, n, n]) tensors.
- h_out: A Tensor, dtype is bfloat16 or float16. Represents output of the Atten/MLP layer.
Dataformat:ND. Supports 2D (Shape:[T, D]) or 3D (Shape:[B, S, D]) tensors.
- h_post: A Tensor, dtype is float32. Represents the h_res transformation matrix.
Dataformat:ND. Supports 2D (Shape:[T, n]) or 3D (Shape:[B, S, n]) tensors.

## Outputs

y: A Tensor. Type is:BFloat16 or Float16. Dataformat:ND. 
Supports 3D (Shape:[T, n, D]) or 4D (Shape:[B, S, n, D]) tensors.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- input1 h_res: float32
- input2 h_out: bfloat16,float16
- input3 h_post: float32
- output0 y: bfloat16,float16


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
