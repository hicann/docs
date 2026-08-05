# CondTake

```c
REG_OP(CondTake)
    .INPUT(data, TensorType({DT_FLOAT}))
    .INPUT(mask, TensorType({DT_FLOAT}))
    .OUTPUT(out_data, TensorType({DT_FLOAT}))
    .OUTPUT(out_index, TensorType({DT_INT32}))
    .OUTPUT(valid_num, TensorType({DT_INT32}))
    .REQUIRED_ATTR(mode, String)
    .REQUIRED_ATTR(val, Float)
    .ATTR(eps, Float, 1e-06f)
    .OP_END_FACTORY_REG(CondTake)
```

## Brief

Take elements from data if specific condition is satisfied on mask. 

## Inputs

- data: input tensor from which to take elements, High-dimension input would
first be flattened.
- mask: condition param; must be the same shape with data.

## Outputs

- out_data: the elements taken
- out_index: the indices corresponding to those elements
- valid_num: elements of out_data and out_index from zeros to valid_num is valid.

## Attributes

- mode:convert by convert in Mode.
- val:convert by <class 'float'>
- eps:convert by <class 'float'> (default: 1e-06)

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 data: float32
- input1 mask: float32
- output0 out_data: float32
- output1 out_index: int32
- output2 valid_num: int32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
