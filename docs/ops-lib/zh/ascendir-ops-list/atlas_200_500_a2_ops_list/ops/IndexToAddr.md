# IndexToAddr

```c
REG_OP(IndexToAddr)
    .INPUT(base_addr, TensorType({DT_INT64, DT_UINT64}))
    .INPUT(x, TensorType({DT_INT64, DT_UINT64}))
    .OUTPUT(addrs_table, TensorType({DT_INT64, DT_UINT64}))
    .REQUIRED_ATTR(ori_shape, ListInt)
    .REQUIRED_ATTR(block_size, ListInt)
    .ATTR(ori_storage_mode, String, "Matrix")
    .ATTR(block_storage_mode, String, "Matrix")
    .ATTR(rank_id, Int, 0)
    .ATTR(dtype, Type, DT_FLOAT)
    .OP_END_FACTORY_REG(IndexToAddr)
```

## Brief

Converts block index to address table.

## Inputs

- base_addr: Base address tensor, supports DT_INT64 and DT_UINT64.
- x: Index tensor, supports DT_INT64 and DT_UINT64.

## Outputs

- addrs_table: Address table tensor, supports DT_INT64 and DT_UINT64.

## Attributes

- ori_shape: Original matrix shape.
- block_size: Block matrix shape.
- ori_storage_mode: Storage mode of original tensor, default "Matrix".
- block_storage_mode: Storage mode of block tensor, default "Matrix".
- rank_id: Rank id, default 0.
- dtype: Base tensor dtype, default DT_FLOAT.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 base_addr: int64,uint64
- input1 x: int64,uint64
- output0 addrs_table: int64,uint64


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
