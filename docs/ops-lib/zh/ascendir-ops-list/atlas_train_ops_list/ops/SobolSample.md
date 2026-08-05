# SobolSample

```c
REG_OP(SobolSample)
    .INPUT(dim, TensorType({DT_INT32}))
    .INPUT(num_results, TensorType({DT_INT32}))
    .INPUT(skip, TensorType({DT_INT32}))
    .OUTPUT(samples, TensorType({DT_FLOAT,DT_DOUBLE}))
    .ATTR(dtype, Type, DT_FLOAT)
    .OP_END_FACTORY_REG(SobolSample)
```

## Brief

Get sobol samples. 

## Inputs

Three inputs, including:
- dim: Dimension of results, which must be a scalar of type int32.
- num_results: Number of results, which must be a scalar of type int32.
- skip: Number of initial points, which must be a scalar of type int32.

## Outputs

- y: A Tensor with the float32 or double type generated samples.

## Attributes

- dtype: Data type of output samples. Defaults to float32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 dim: int32
- input1 num_results: int32
- input2 skip: int32
- output0 samples: double,float32

## Third-party framework compatibility

- compatible with tensorflow SobolSample operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
