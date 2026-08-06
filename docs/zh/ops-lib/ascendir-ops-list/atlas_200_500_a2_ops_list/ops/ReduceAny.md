# ReduceAny

```c
REG_OP(ReduceAny)
    .INPUT(x, TensorType({DT_BOOL, DT_FLOAT}))
    .INPUT(axes, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType({DT_BOOL}))
    .ATTR(keep_dims, Bool, false)
    .OP_END_FACTORY_REG(ReduceAny)
```

## Brief

Computes the "logical or" of elements across dimensions of a tensor.
Reduces "x" along the dimensions given in "axes".
Unless "keep_dims" is true, the rank of the tensor is reduced by 1 for each
entry in "axes". If "keep_dims" is true, the reduced dimensions
are retained with length 1.
If "axes" is None, all dimensions are reduced, and a
tensor with a single element is returned.

## Inputs

- x : The tensor to reduce.
- axes: The int tensor, The dimensions to reduce.
         If "None" (default), reduces all dimensions.
         Must be in the range "[-rank(x), rank(x))".

## Outputs

y: The reduced tensor

## Attributes

keep_dims: bool, default false.
If true, retains reduced dimensions with length 1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bool
- input1 axes: int32,int64
- output0 y: bool
### AI CPU
- input0 x: bool
- input1 axes: int32,int64
- output0 y: bool

## Attention Constraints

Only support bool,fp32

## Third-party framework compatibility

Compatible with the TensorFlow operator reduce_any.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
