# FractionalMaxPoolGrad

```c
REG_OP(FractionalMaxPoolGrad)
    .INPUT(orig_input, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT32, DT_INT64}))
    .INPUT(orig_output, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT32, DT_INT64}))
    .INPUT(out_backprop, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT32, DT_INT64}))
    .INPUT(row_pooling_sequence, TensorType({ DT_INT64 }))
    .INPUT(col_pooling_sequence, TensorType({ DT_INT64 }))
    .OUTPUT(y, TensorType({ DT_FLOAT, DT_DOUBLE, DT_INT32, DT_INT64 }))
    .ATTR(overlapping, Bool, false)
    .OP_END_FACTORY_REG(FractionalMaxPoolGrad)
```

## Brief

Computes gradient of the FractionalMaxPool function .

## Inputs

Inputs include:
- orig_input: A Tensor. Must be one of the following types: float32, double, int32, int64.
- orig_output: A Tensor. Must have the same type as orig_input.
- out_backprop: A Tensor. Must have the same type as orig_input.
4-D with shape [batch, height, width, channels].
- row_pooling_sequence: A Tensor of type int64.
- col_pooling_sequence: A Tensor of type int64.

## Outputs

y: A Tensor. Has the same type as orig_input. 

## Attributes

overlapping: An optional bool. Defaults to False. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 orig_input: double,float32,int32,int64
- input1 orig_output: double,float32,int32,int64
- input2 out_backprop: double,float32,int32,int64
- input3 row_pooling_sequence: int64
- input4 col_pooling_sequence: int64
- output0 y: double,float32,int32,int64

## Attention Constraints

The implementation for FractionalMaxPoolGrad on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow FractionalMaxPoolGrad operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
