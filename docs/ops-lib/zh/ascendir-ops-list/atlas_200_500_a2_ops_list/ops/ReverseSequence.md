# ReverseSequence

```c
REG_OP(ReverseSequence)
    .INPUT(x,
        TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, DT_UINT16, \
        DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(seq_lengths, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y,
        TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, DT_UINT16, \
        DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .REQUIRED_ATTR(seq_dim, Int)
    .ATTR(batch_dim, Int, 0)
    .OP_END_FACTORY_REG(ReverseSequence)
```

## Brief

Reverses variable length slices. 

## Inputs

- x: A ND Tensor. The input to reverse. Support 2D ~ 8D.Must be one of the following types:
complex64, complex128, double, float32, float16, int16, int32, int64, int8, uint16, uint32, uint8, bfloat16.
- seq_lengths: A 1D Tensor of type int32 or int64.

## Outputs

y: A rank ND tensor. Has the same shape as input. The extracted banded tensor. 

## Attributes

- seq_dim: The dimension along which reversal is performed.
- batch_dim: An optional int. Defaults to "0". The dimension along which
reversal is performed. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 seq_lengths: int32,int64
- output0 y: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator ReverseSequence.

## Constraints

- seq_dim != batch_dim.
- seq_dim < rank, batch_dim < rank, rank is the dimension of x.
- x.shape[batch_dim] = seq_lengths.shape(0).
- The value range of seq_lengths is [0, x.shape[seq_dim]].


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
