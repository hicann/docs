# ScatterMaxWithArgmax

```c
REG_OP(ScatterMaxWithArgmax)
    .INPUT(x, TensorType({DT_FLOAT}))
    .INPUT(indices, TensorType({DT_INT32}))
    .INPUT(updates, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .OUTPUT(argmax, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(ScatterMaxWithArgmax)
```

## Inputs

Three inputs, including:
- x: An ND Tensor .
Must be one of the following types: float
- indices: An ND Tensor .
Must be one of the following types: int32
- updates: An ND Tensor .
Must be one of the following types: float

## Outputs

argmax: A Tensor. Has the same type and format as input "indices" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float32
- input1 indices: int32
- input2 updates: float32
- output0 y: float32
- output1 argmax: int32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
