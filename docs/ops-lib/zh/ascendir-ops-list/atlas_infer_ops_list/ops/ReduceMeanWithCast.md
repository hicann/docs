# ReduceMeanWithCast

```c
REG_OP(ReduceMeanWithCast)
    .INPUT(x, "T1")
    .INPUT(axes, "T2")
    .OUTPUT(y, "T3")
    .ATTR(keep_dims, Bool, false)
    .ATTR(noop_with_empty_axes, Bool, true)
    .ATTR(dtype, Type, DT_UNDEFINED)
    .DATATYPE(T1, TensorType::NumberType())
    .DATATYPE(T2, TensorType::IndexNumberType())
    .DATATYPE(T3, TensorType::NumberType())
    .OP_END_FACTORY_REG(ReduceMeanWithCast)
```

## Brief

Insert a Cast node for the ReduceMean operator . 

## Inputs

Two inputs, including:
 @li x: A ND Tensor. Must be one of the following types: float16, float32, int8, uint8.
 @li axes: The dimensions to reduce. Must be one of the following types: int, list, tuple, NoneType.
   - If None (the default), reduces all dimensions.
   - Must be in the range [-rank(x), rank(x)) . 

## Outputs

y: A ND Tensor. Has the same type as "x" . 

## Attributes

keep_dims: A bool or NoneType.
 - If true, retains reduced dimensions with length 1.
 - If false, the rank of the tensor is reduced by 1 for each entry in axis.
noop_with_empty_axes: A bool.
 - If true, when axes = [], not reduce.
 - If false, when axes = [], reduce all.
dtype: enum.
 - optional attr, could be one of the following types: DT_FLOAT16, DT_FLOAT, DT_INT8, DT_UINT8.

## Third-party framework compatibility

Compatible with the TensorFlow operator ReduceMeanWithCast.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
