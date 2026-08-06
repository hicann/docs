# InTopKV2

```c
REG_OP(InTopKV2)
    .INPUT(predictions, TensorType({DT_FLOAT}))
    .INPUT(targets, TensorType(IndexNumberType))
    .INPUT(k, TensorType({IndexNumberType}))
    .OUTPUT(precision, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(InTopKV2)
```

## Brief

Says whether the targets are in the top "k" predictions . 

## Inputs

Three inputs, including:
- predictions: A 2D Tensor of type float32. A "batch_size * classes" tensor.
- targets: A 1D Tensor of type IndexNumberType. A batch_size tensor of class ids.
- k: A 1D Tensor of the same type as "targets".
Specifies the number of top elements to look at for computing precision . 

## Outputs

precision: A Tensor of type bool . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 predictions: float32
- input1 targets: int32,int64
- input2 k: int32,int64
- output0 precision: bool

## Attention Constraints

- targets must be non-negative tensor.

## Third-party framework compatibility

- Compatible with the TensorFlow operator InTopKV2.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
