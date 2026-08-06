# InTopK

```c
REG_OP(InTopK)
    .INPUT(x1, TensorType({DT_FLOAT}))
    .INPUT(x2, TensorType(IndexNumberType))
    .INPUT(k, TensorType({IndexNumberType}))
    .OUTPUT(y, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(InTopK)
```

## Brief

Says whether the targets are in the top "k" predictions . 

## Inputs

- x1: A 2D Tensor of type float32. A "batch_size * classes" tensor.
- x2: A 1D Tensor of type IndexNumberType. A batch_size tensor of class ids.
- k: A 1D Tensor of the same type as "x2".
Specifies the number of top elements to look at for computing precision . 

## Outputs

y: A Tensor of type bool . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x1: float32
- input1 x2: int32,int64
- input2 k: int32,int64
- output0 y: bool

## Attention Constraints

- x2 must be non-negative tensor.

## Third-party framework compatibility

- Compatible with the TensorFlow operator InTopKV2.


---

[Back to Operator Specifications (Ascend950)](../README.md)
