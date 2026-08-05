# NormalizeBatch

```c
REG_OP(NormalizeBatch)
    .INPUT(input_x, TensorType({ DT_FLOAT }))
    .INPUT(seq_len, TensorType({ DT_INT32 }))
    .OUTPUT(output_y, TensorType({ DT_FLOAT }))
    .REQUIRED_ATTR(normalize_type, String)
    .ATTR(epsilon, Float, 0.00001f)
    .OP_END_FACTORY_REG(NormalizeBatch)
```

## Brief

Performs batch normalization . 

## Inputs

Two inputs
- input_x: A Tensor. Support float32. shape (n, c, d).
- seq_len: A Tensor. Each batch normalize data num. Support Int32. Shape (n, ).

## Outputs

One outputs
- output_y: A Tensor for the normalized "x".Support float32. shape (n, c, d).

## Attributes

- normalize_type: Str. Support "per_feature" or "all_features".
- epsilon: An optional float32, specifying the small value added to
variance to avoid dividing by zero. Defaults to "0.00001" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_x: float32
- input1 seq_len: int32
- output0 output_y: float32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
