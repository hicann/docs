# SparseCross

```c
REG_OP(SparseCross)
    .DYNAMIC_INPUT(indices, TensorType({DT_INT64}))
    .DYNAMIC_INPUT(values, TensorType({DT_INT64, DT_STRING}))
    .DYNAMIC_INPUT(shapes, TensorType({DT_INT64}))
    .DYNAMIC_INPUT(dense_inputs, TensorType({DT_INT64, DT_STRING}))
    .OUTPUT(output_indices, TensorType({DT_INT64}))
    .OUTPUT(output_values, TensorType({DT_INT64, DT_STRING}))
    .OUTPUT(output_shape, TensorType({DT_INT64}))
    .ATTR(N, Int, 0)
    .REQUIRED_ATTR(hashed_output, Bool)
    .ATTR(num_buckets, Int, 0)
    .REQUIRED_ATTR(hash_key, Int)
    .REQUIRED_ATTR(out_type, Type)
    .REQUIRED_ATTR(internal_type, Type)
    .OP_END_FACTORY_REG(SparseCross)
```

## Brief

Generates sparse cross from a list of sparse and dense tensors. 

## Inputs

- indices: A list of 2D tensor objects of type int64.
Indices of each input SparseTensor.It's a dynamic input.
- values: A list of 1D tensor objects of type int64 or string.
Values of each SparseTensor.It's a dynamic input.
- shapes: A list with the same length as "indices" of 1D tensor objects of type int64.
Shapes of each SparseTensor.It's a dynamic input.
- dense_inputs: A list of 2D tensor objects of type int64 or string.
Columns represented by dense tensor .It's a dynamic input. 

## Outputs

- output_indices: A tensor of type int64.
- output_values: A tensor of type "out_type".
- output_shape: A tensor of type int64.

## Attributes

- N: number of sparse.
- hashed_output: A bool. If true, returns the hash of the cross instead of the string.
- num_buckets: An int that is >= 0. It is used if "hashed_output" is true.
output = hashed_value%num_buckets if num_buckets > 0 else "hashed_value".
- hash_key: An int. Specify the hash_key that will be used by the "FingerprintCat64"
function to combine the crosses fingerprints.
- out_type: An int64 or string.
- internal_type: An int64 or string.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output0 output_indices: int64
- output1 output_values: int64,string
- output2 output_shape: int64

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseCross.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
