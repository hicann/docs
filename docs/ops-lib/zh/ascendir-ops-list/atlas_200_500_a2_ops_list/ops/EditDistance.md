# EditDistance

```c
REG_OP(EditDistance)
    .INPUT(hypothesis_indices, TensorType({DT_INT64}))
    .INPUT(hypothesis_values, TensorType::BasicType())
    .INPUT(hypothesis_shape, TensorType({DT_INT64}))
    .INPUT(truth_indices, TensorType({DT_INT64}))
    .INPUT(truth_values, TensorType::BasicType())
    .INPUT(truth_shape, TensorType({DT_INT64}))
    .ATTR(normalize, Bool, true)
    .OUTPUT(output, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(EditDistance)
```

## Brief

Computes the (possibly normalized) Levenshtein Edit Distance. 

## Inputs

- hypothesis_indices: The indices of the hypothesis list SparseTensor.
This is an N x R int64 matrix.
- hypothesis_shape: The values of the hypothesis list SparseTensor.
This is an N-length vector.
- hypothesis_shape: The shape of the hypothesis list SparseTensor.
This is an R-length vector.
- truth_indices: The indices of the truth list SparseTensor.
This is an M x R int64 matrix.
- truth_shape: The values of the truth list SparseTensor.
This is an M-length vector.
- truth_shape: The shape of the truth list SparseTensor.
This is an R-length vector.

## Outputs

output: A dense float tensor with rank R - 1. 

## Attributes

normalize: boolean (if true, edit distances are normalized by length of truth). 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 hypothesis_indices: int64
- input1 hypothesis_values: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input2 hypothesis_shape: int64
- input3 truth_indices: int64
- input4 truth_values: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input5 truth_shape: int64
- output0 output: float32

## Third-party framework compatibility

Compatible with TensorFlow EditDistance operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
