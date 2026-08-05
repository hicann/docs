# MoeInitRouting

```c
REG_OP(MoeInitRouting)
    .INPUT(x, "T1")
    .INPUT(row_idx, "T2")
    .INPUT(expert_idx, "T2")
    .OUTPUT(expanded_x, "T1")
    .OUTPUT(expanded_row_idx, "T2")
    .OUTPUT(expanded_expert_idx, "T2")
    .DATATYPE(T1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DATATYPE(T2, TensorType({DT_INT32}))
    .REQUIRED_ATTR(active_num, Int)
    .OP_END_FACTORY_REG(MoeInitRouting)
```

## Brief

compute init routing for moe input.

## Inputs

- x: A 2D Tensor. Type is:BFloat16, Float16 or Float32. Format support ND.
- row_idx: A 2D Tensor: A Tensor. Type is:Int32. Format support ND.
- expert_idx: A 2D Tensor. Type is:Int32. Format support ND.

## Outputs

- expanded_x: A 2D Tensor. Type is:BFloat16, Float16 or Float32. The data type must be the same as that of x.
                The first dim must be the first dim of row_idx multiply the second dim of row_idx or active_num.
                The second dim must be the second dim of x. Format support ND.
- expanded_row_idx: A 1D Tensor. Type is:Int32. The dim must be  the first dim of row_idx multiply the second
                      dim of row_idx. Format support ND.
- expanded_expert_idx: A 1D Tensor. Type is:Int32. The Shape is same as expanded_row_idx. Format support ND.

## Attributes

- active_num: Required parameter. Type is:Int32. The value 0 indicates a non-active
                scenario, and a value greater than 0 indicates an active scenario. In the active scenario, the size
                of axis 0 of expanded_x must be equal to the value of active_num.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 row_idx: int32
- input2 expert_idx: int32
- output0 expanded_x: bfloat16,float16,float32
- output1 expanded_row_idx: int32
- output2 expanded_expert_idx: int32


---

[Back to Operator Specifications (Ascend950)](../README.md)
