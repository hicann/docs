# ReduceLogSum

```c
REG_OP(ReduceLogSum)
    .INPUT(x, TensorType::NumberType())
    .INPUT(axes, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::NumberType())
    .ATTR(keep_dims, Bool, false)
    .OP_END_FACTORY_REG(ReduceLogSum)
```

## Brief

Computes the log and sum of elements across dimensions of a tensor.
Reduces "x" along the dimensions given in "axes".
Unless "keep_dims" is true, the rank of the tensor is reduced by 1 for each
entry in "axes". If "keep_dims" is true, the reduced dimensions
are retained with length 1.

## Inputs

Two inputs, including:
- x: A Tensor. Must be one of the following types: float32, float16.
- axes: A 1D list or tuple of int32 or int64. Specifies the dimensions to reduce .

## Outputs

y: The reduced tensor. Has the same type and format as input "x" . 

## Attributes

keep_dims: An optional bool. If "true", retains reduced dimensions with length 1. Defaults to "false" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 axes: int32,int64
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the Onnx operator ReduceLogSum.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
