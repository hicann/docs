# ReduceJoin

```c
REG_OP(ReduceJoin)
    .INPUT(input, TensorType({DT_STRING}))
    .INPUT(reduction_indices, TensorType({DT_INT32}))
    .OUTPUT(output, TensorType({DT_STRING}))
    .ATTR(keep_dims, Bool, true)
    .ATTR(separator, String, "")
    .OP_END_FACTORY_REG(ReduceJoin)
```

## Brief

Joins a string Tensor across the given dimensions. 

## Inputs

include:
- input:A Tensor of type string. The text to be processed.
- reduction_indices:A Tensor of type int. The text to be processed.

## Outputs

output:A Tensor of type string.

## Attributes

- keep_dims: An optional bool. Defaults to False. If True, retain reduced dimensions with length 1.
- separator: An optional string. Defaults to "".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input: string
- input1 reduction_indices: int32
- output0 output: string


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
