# MoeTutelCombineX

```c
REG_OP(MoeTutelCombineX)
    .INPUT(y_grad, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .INPUT(gates, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .INPUT(indices, TensorType({ DT_INT32 }))
    .INPUT(locations, TensorType({ DT_INT32 }))
    .OUTPUT(x_grad, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .OP_END_FACTORY_REG(MoeTutelCombineX)
```

## Brief

Tutel combine function in moe.

## Inputs

- y_grad: A mutable Tensor of the type DT_FLOAT, DT_FLOAT16, DT_BF16.
- gates: A mutable Tensor of the type DT_FLOAT, DT_FLOAT16, DT_BF16.
- indices: A mutable Tensor of the type DT_INT32, for topk's k size.
- locations: A mutable Tensor of the type DT_INT32, for token size.

## Outputs

- x_grad: A mutable Tensor of the type DT_FLOAT, DT_FLOAT16, DT_BF16.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y_grad: bfloat16,float16,float32
- input1 gates: bfloat16,float16,float32
- input2 indices: int32
- input3 locations: int32
- output0 x_grad: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
