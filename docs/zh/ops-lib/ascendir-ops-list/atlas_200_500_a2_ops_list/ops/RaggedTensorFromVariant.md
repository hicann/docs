# RaggedTensorFromVariant

```c
REG_OP(RaggedTensorFromVariant)
    .INPUT(encoded_ragged, TensorType({DT_VARIANT}))
    .DYNAMIC_OUTPUT(output_nested_splits, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(output_dense_values, TensorType::BasicType())
    .REQUIRED_ATTR(input_ragged_rank, Int)
    .REQUIRED_ATTR(output_ragged_rank, Int)
    .REQUIRED_ATTR(Tvalues, Type)
    .ATTR(Tsplits, Type, DT_INT64)
    .OP_END_FACTORY_REG(RaggedTensorFromVariant)
```

## Brief

Decodes a variant Tensor into a RaggedTensor. 

## Outputs

- output_nested_splits: A list of output_ragged_rank Tensor objects with type int32 or int64.
- output_dense_values:  A Tensor, which must be one of the following types:
double, float32, float16, bfloat16, complex32, complex64, complex128,
int8, uint8, int16, uint16, int32, uint32, int64, uint64, qint8, quint8, qint16, quint16, qint32.

## Attributes

- input_ragged_rank: An int that is >= -1. The ragged rank of each encoded RaggedTensor component in the input.
        If set to -1, this is inferred as output_n - rank(encoded_ragged).
- output_ragged_rank: An int that is >= 0. The expected ragged rank of the output RaggedTensor.
         The following must hold: output_n = rank(encoded_ragged) + input_n.
- Tvalues: The data type of output_dense_values.
- Tsplits: The data type of output_nested_splits. An optional DType of "int32, int64". Defaults to `int64`.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 encoded_ragged: variant
- output0 output_dense_values: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Input

encoded_ragged:  A Tensor of type variant. A variant Tensor containing encoded RaggedTensors. 

## Third-party framework compatibility.

Compatible with tensorflow RaggedTensorFromVariant operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
