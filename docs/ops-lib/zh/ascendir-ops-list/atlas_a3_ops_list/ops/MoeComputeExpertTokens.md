# MoeComputeExpertTokens

```c
REG_OP(MoeComputeExpertTokens)
    .INPUT(sorted_experts, "T")
    .OUTPUT(total_rows_before_expert, "T")
    .REQUIRED_ATTR(num_experts, Int)
    .DATATYPE(T, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(MoeComputeExpertTokens)
```

## Brief

Binary finds the position of the last row processed by each expert in the sorted_experts array.

## Inputs

- sorted_experts: An 1D Tensor, sorted expert array. Type is:Int32.

## Outputs

- total_rows_before_expert: A Tensor. Type is:Int32.

## Attributes

- num_experts: Required parameter. Type is:Int. The value must be more than 0 and less than 2147483647.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 sorted_experts: int32
- output0 total_rows_before_expert: int32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
