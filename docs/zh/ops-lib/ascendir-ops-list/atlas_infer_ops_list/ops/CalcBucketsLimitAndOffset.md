# CalcBucketsLimitAndOffset

```c
REG_OP(CalcBucketsLimitAndOffset)
    .INPUT(bucket_list, TensorType({DT_INT32}))
    .INPUT(ivf_counts, TensorType({DT_INT32}))
    .INPUT(ivf_offset, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(buckets_limit, TensorType({DT_INT32}))
    .OUTPUT(buckets_offset, TensorType({DT_INT32, DT_INT64}))
    .REQUIRED_ATTR(total_limit, Int)
    .OP_END_FACTORY_REG(CalcBucketsLimitAndOffset)
```

## Brief

Calculate buckets limit and offset. 

## Inputs

Three inputs, including:
- bucket_list: A 1-D tensor of type int32 with the value of ivf_counts and ivf_offset index.
- ivf_counts: A 1-D tensor of type int32 with the value of ivf counts.
- ivf_offset: A 1-D tensor of type int32 or int64 with the value of ivf offset.

## Outputs

- buckets_limit: A 1-D tensor of type int32 with the sum <= total_limit.
- buckets_offset: A 1-D tensor of type int32 or int64 with the value of ivf_offset corresponding to bucket_list.

## Attributes

total_limit: A int64 type maximum value of the sum of ivf_counts corresponding to bucket_list. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 bucket_list: int32
- input1 ivf_counts: int32
- input2 ivf_offset: int32,int64
- output0 buckets_limit: int32
- output1 buckets_offset: int32,int64


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
