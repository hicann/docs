# FractionalAvgPoolGrad

```c
REG_OP(FractionalAvgPoolGrad)
    .INPUT(orig_input_tensor_shape, TensorType({DT_INT64}))
    .INPUT(out_backprop, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT32, DT_INT64}))
    .INPUT(row_pooling_sequence, TensorType({DT_INT64}))
    .INPUT(col_pooling_sequence, TensorType({DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT32, DT_INT64}))
    .ATTR(overlapping, Bool, false)
    .OP_END_FACTORY_REG(FractionalAvgPoolGrad)
```

## Brief

Computes gradient of the FractionalAvgPool function .

## Inputs

Inputs include:
- orig_input_tensor_shape: A Tensor of type int64.
- out_backprop: A Tensor. Must be one of the following types: float32, double,
int32, int64. 4-D with shape [batch, height, width, channels].
- row_pooling_sequence: A Tensor of type int64.
- col_pooling_sequence: A Tensor of type int64.

## Outputs

y: A Tensor. Has the same type as out_backprop. 

## Attributes

overlapping: An optional bool. Defaults to False. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 orig_input_tensor_shape: int64
- input1 out_backprop: double,float32,int32,int64
- input2 row_pooling_sequence: int64
- input3 col_pooling_sequence: int64
- output0 y: double,float32,int32,int64

## Attention Constraints

The implementation for FractionalAvgPoolGrad on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow FractionalAvgPoolGrad operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
