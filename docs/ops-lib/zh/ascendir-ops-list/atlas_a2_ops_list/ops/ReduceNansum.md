# ReduceNansum

```c
REG_OP(ReduceNansum)
    .INPUT(x, "T1")
    .INPUT(axes, "T2")
    .OUTPUT(y, "T1")
    .ATTR(keep_dims, Bool, false)
    .DATATYPE(T1, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .DATATYPE(T2, TensorType::IndexNumberType())
    .OP_END_FACTORY_REG(ReduceNansum)
```

## Brief

Computes the sum of elements across dimensions of a tensor,
treating Not a Numbers(NaNs) as zero .

## Inputs

Two inputs, including:
- x: A Tensor. Must be one of the following types of "T1":
    float32, float16, bfloat16
- axis: A 1D list or tuple of "T2": int32 or int64. Specifies the dimensions to reduce .

## Outputs

y: The reduced tensor. Has the same type and format as input "x" . 

## Attributes

keepdims: An optional bool. If "true", retains reduced dimensions with length 1. Defaults to "false" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 axes: int32,int64
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator ReduceNansum.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
