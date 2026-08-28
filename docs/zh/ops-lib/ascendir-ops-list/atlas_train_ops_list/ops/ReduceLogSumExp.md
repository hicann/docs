# ReduceLogSumExp

```c
REG_OP(ReduceLogSumExp)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(axes, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(keep_dims, Bool, false)
    .ATTR(noop_with_empty_axes, Bool, false)
    .OP_END_FACTORY_REG(ReduceLogSumExp)
```

## Brief

Computes the log and sum and exp of elements across dimensions of a tensor.
Reduces "x" along the dimensions given in "axes".
Unless "keep_dims" is true, the rank of the tensor is reduced by 1 for each
entry in "axes". If "keep_dims" is true, the reduced dimensions
are retained with length 1.

## Inputs

Two inputs, including:
- x: A Tensor. Must be one of the following types: float32, float16, bfloat16.
- axes: A 1D list or tuple of int32 or int64. Specifies the dimensions to reduce.

## Outputs

y: The reduced tensor. Has the same type and format as input "x" . 

## Attributes

keep_dims: An optional bool. If "true", retains reduced dimensions with length 1. Defaults to "false" . 
noop_with_empty_axes: An optional bool. Defaults to "false" .
- If true, when axes = [], not reduce.
- If false, when axes = [], reduce all.
This attribute is valid only for Ascend950 AI Processors and later products.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 axes: int32,int64
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the Onnx operator ReduceLogSumExp.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
