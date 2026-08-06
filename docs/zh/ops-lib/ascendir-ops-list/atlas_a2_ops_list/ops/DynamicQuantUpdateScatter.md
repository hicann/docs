# DynamicQuantUpdateScatter

```c
REG_OP(DynamicQuantUpdateScatter)
    .INPUT(var, TensorType({DT_INT8}))
    .INPUT(var_scale, TensorType({DT_FLOAT}))
    .INPUT(indices, TensorType::IndexNumberType())
    .INPUT(updates, TensorType({DT_BF16, DT_FLOAT16}))
    .OPTIONAL_INPUT(smooth_scales, TensorType({DT_BF16, DT_FLOAT16}))
    .OUTPUT(var, TensorType({DT_INT8}))
    .OUTPUT(var_scale, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(reduce, String)
    .ATTR(axis, Int, 0)
    .OP_END_FACTORY_REG(DynamicQuantUpdateScatter)
```

## Brief

Multiplies dynamic quantize and sparse updates into a variable reference .

## Inputs

Five inputs, including:
- var: An ND Tensor.
Must be one of the following types: int8
- var_scale: An ND Tensor.
Must be one of the following types: float
- indices: An ND Tensor.
Must be one of the following types: int32，int64
- updates: An ND Tensor .
Must be one of the following types: bfloat16，float16
- smooth_scales: An ND optional Tensor .
Must be one of the following types: bfloat16，float16 

## Outputs

var: A Tensor. Has the same type and format as input "var" .
var_scale: A Tensor. Has the same type and format as input "var_scale" . 

## Attributes

- axis: An optional attribute. Defaults to 0, not support -1.
- reduce: A required attribute, can be "update".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: int8
- input1 var_scale: float32
- input2 indices: int32,int64
- input3 updates: bfloat16,float16
- input4 smooth_scales: bfloat16,float16
- output0 var: int8
- output1 var_scale: float32

## Third-party framework compatibility

Compatible with the Mindspore operator Scatter.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
