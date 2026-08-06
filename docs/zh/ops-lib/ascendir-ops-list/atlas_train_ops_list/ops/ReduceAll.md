# ReduceAll

```c
REG_OP(ReduceAll)
    .INPUT(x, TensorType({DT_BOOL, DT_BF16, DT_FLOAT, DT_FLOAT16}))
    .INPUT(axes, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType({DT_BOOL}))
    .ATTR(keep_dims, Bool, false)
    .OP_END_FACTORY_REG(ReduceAll)
```

## Brief

Calculates the "logical sum" of elements of a tensor in a dimension .

## Inputs

Two inputs, including:
- x: The tensor to reduce.
- axis: A mutable Tensor with int dtype, The dimensions to reduce.
If None, reduces all dimensions.
Must be in the range [- rank (input_sensor), rank (input_sensor)) .

## Outputs

y: The reduced tensor .

## Attributes

keep_dims: A bool, default false.
If true, retains reduced dimensions with length 1 .

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

Support bool, fp32, fp16, bf16

## Third-party framework compatibility

Compatible with the TensorFlow operator ReduceAll.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
