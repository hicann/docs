# CosineEmbeddingLoss

```c
REG_OP(CosineEmbeddingLoss)
    .INPUT(x1, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(x2, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(target, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .ATTR(margin, Float, 0)
    .ATTR(reduction, String, "mean")
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(CosineEmbeddingLoss)
```

## Brief

Creates a criterion that measures the loss given input tensors x1 x2 and a Tensor label y with values 1 or -1.

## Inputs

- x1: A ND Tensor with one of the following types: int8, uint8, int32, float16, float32, int16, int64, double.
- x2: A ND Tensor with one of the following types: int8, uint8, int32, float16, float32, int16, int64, double.
x1 and x2 can be broadcast.
- target: A ND Tensor with one of the following types: int8, uint8, int32, float16, float32, int16, int64, double.
target and x1, x2 can be broadcast.

## Outputs

- y: A ND Tensor with Must be float32.

## Attributes

- margin: An optional float32. Defaults to "0.0".
- reduction: An optional string. Defaults to "mean".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16,float32,int32
- input1 x2: float16,float32,int32
- input2 target: float16,float32,int32
- output0 y: float32

## Third-party framework compatibility

Compatible with the PyTorch operator CosineEmbeddingLoss.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
