# ForeachScalarPowTensor

```c
REG_OP(ForeachScalarPowTensor)
    .INPUT(scalar, TensorType({DT_FLOAT, DT_INT64}))
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .OP_END_FACTORY_REG(ForeachScalarPowTensor)
```

## Brief

Apply power operation for each tensor in a tensor list with each tensor in another
tensor list in manner of element-wise

## Inputs

Two inputs:
- x1: A scalar
- x2: A tensor list containing multiple tensors

## Outputs

- y: A tensor list which store the tensors whose value are powering the scalar in scalar list


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
