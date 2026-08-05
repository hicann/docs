# MoeTutelCombineGates

```c
REG_OP(MoeTutelCombineGates)
    .INPUT(x, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .INPUT(y_grad, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .INPUT(indices, TensorType({ DT_INT32 }))
    .INPUT(locations, TensorType({ DT_INT32 }))
    .OUTPUT(gates_grad, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .OP_END_FACTORY_REG(MoeTutelCombineGates)
```

## Brief

Tutel combine function in moe.

## Inputs

- x: A mutable Tensor of the type DT_FLOAT, DT_FLOAT16, DT_BF16.
- y_grad: A mutable Tensor of the type DT_FLOAT, DT_FLOAT16, DT_BF16.
- indices: A mutable Tensor of the type DT_INT32, for topk's k size.
- locations: A mutable Tensor of the type DT_INT32, for token size.

## Outputs

gates_grad: A mutable Tensor of the type DT_FLOAT, DT_FLOAT16, DT_BF16.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 y_grad: bfloat16,float16,float32
- input2 indices: int32
- input3 locations: int32
- output0 gates_grad: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
