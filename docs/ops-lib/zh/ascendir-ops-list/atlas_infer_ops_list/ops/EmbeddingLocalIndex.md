# EmbeddingLocalIndex

```c
REG_OP(EmbeddingLocalIndex)
    .INPUT(addr_table, TensorType({DT_UINT64}))
    .INPUT(index, TensorType({DT_INT64,DT_INT32,DT_UINT32,DT_UINT64}))
    .OUTPUT(local_idx, TensorType({DT_INT64,DT_INT32,DT_UINT32,DT_UINT64}))
    .OUTPUT(nums, TensorType({DT_INT64,DT_INT32,DT_UINT32,DT_UINT64}))
    .OUTPUT(recover_idx, TensorType({DT_INT64,DT_INT32,DT_UINT32,DT_UINT64}))
    .ATTR(row_memory, Int, 320)
    .ATTR(mode, String, "mod")
    .OP_END_FACTORY_REG(EmbeddingLocalIndex)
```

## Brief

EmbeddingLocalIndex, Sort statistics index according to rank_id. 

## Inputs

- addr_table: A 2D tensor which last dimension must be 3.
- index: A tensor with data type int32, int64, uint32, uint64.

## Outputs

- local_idx:Index on each server.
- nums:The number of local_idx found on each server.
- recover_idx:The sorted local_idx element is at the position corresponding
to the original input index.

## Attributes

- row_memory: An optional int, the size of Embedding vector in a row. Default is 320.
- mode: An optional string, currently there are two options: 'mod' and 'order'. Default is 'mod'.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 addr_table: uint64
- input1 index: int32,int64,uint32,uint64
- output0 local_idx: int32,int64,uint32,uint64
- output1 nums: int32,int64,uint32,uint64
- output2 recover_idx: int32,int64,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator Diag.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
