# Copy

```c
REG_OP(Copy)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_UINT8, DT_INT16, \
              DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_UINT8, DT_INT16, \
              DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64}))
    .REQUIRED_ATTR(N, Int)
    .OP_END_FACTORY_REG(Copy)
```

## Brief

Derived from the Caffe operator Split that splits an input blob to
   multiple output blobs for feeding a blob into multiple output layers.
The Split node is removed from the graph after the split operation is completed. 

## Inputs

x: A Tensor. Must be one of the following types:
fp16, fp32, int8, uint8, int16, uint16, int32, uint32, int64, uint64. 

## Outputs

y: A Tensor. Has the same type as "x".It's required and the value should equal to output_num. 

## Attributes

N: A required int. The parameter will get the number of dynamic outputs.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
