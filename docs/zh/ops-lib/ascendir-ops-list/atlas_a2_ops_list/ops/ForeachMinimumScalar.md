# ForeachMinimumScalar

```c
REG_OP(ForeachMinimumScalar)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .INPUT(scalar, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .OP_END_FACTORY_REG(ForeachMinimumScalar)
```

## Brief

Apply minimum operation for each tensor in tensor list with a scalar in manner of element-wise

## Inputs

Two inputs:
- x: A tensor list containing multiple tensors
- scalar: A scalar in form of tensor with only one element, the shape must be (1,)

## Outputs

- y: A tensor list which store the tensors whose value are minimum with the scalar

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int32
- input1 scalar: float16,float32,int32
- output0 y: bfloat16,float16,float32,int32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
