# ForeachSubScalarInplace

```c
REG_OP(ForeachSubScalarInplace)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .INPUT(scalar, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .OP_END_FACTORY_REG(ForeachSubScalarInplace)
```

## Brief

Apply sub operation for each tensor in tensor list with a scalar in manner of element-wise

## Inputs

Two inputs:
- x: A tensor list containing multiple tensors
meanwhile, this value is also an output, store the value sub by the scalar.
- scalar: A scalar in form of tensor with only one element, the shape must be (1,)

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int32
- input1 scalar: float16,float32,int32


---

[Back to Operator Specifications (Ascend950)](../README.md)
