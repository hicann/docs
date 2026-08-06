# MoeTutelDispatch

```c
REG_OP(MoeTutelDispatch)
    .INPUT(x, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .INPUT(gates, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .INPUT(indices, TensorType({ DT_INT32 }))
    .INPUT(locations, TensorType({ DT_INT32 }))
    .OUTPUT(y, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .REQUIRED_ATTR(capacity, Int)
    .OP_END_FACTORY_REG(MoeTutelDispatch)
```

## Brief

Tutel dispatch function in moe.

## Inputs

- x: A mutable Tensor of the type DT_FLOAT, DT_FLOAT16, DT_BF16.
- gates: A mutable Tensor of the type DT_FLOAT, DT_FLOAT16, DT_BF16.
- indices: A mutable Tensor of the type DT_INT32, for topk's k size.
- locations: A mutable Tensor of the type DT_INT32, for token size.

## Outputs

y: A mutable Tensor of the type DT_FLOAT, DT_FLOAT16, DT_BF16.

## Attributes

capacity: expert capacity.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 gates: bfloat16,float16,float32
- input2 indices: int32
- input3 locations: int32
- output0 y: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
