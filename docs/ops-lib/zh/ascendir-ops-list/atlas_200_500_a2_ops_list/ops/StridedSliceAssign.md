# StridedSliceAssign

```c
REG_OP(StridedSliceAssign)
    .INPUT(var, TensorType(BasicType))
    .INPUT(begin, TensorType(IndexNumberType))
    .INPUT(end, TensorType(IndexNumberType))
    .INPUT(strides, TensorType(IndexNumberType))
    .INPUT(input_value, TensorType(BasicType))
    .OUTPUT(var, TensorType(BasicType))
    .ATTR(begin_mask, Int, 0)
    .ATTR(end_mask, Int, 0)
    .ATTR(ellipsis_mask, Int, 0)
    .ATTR(new_axis_mask, Int, 0)
    .ATTR(shrink_axis_mask, Int, 0)
    .OP_END_FACTORY_REG(StridedSliceAssign)
```

## Brief

Assigns "value" to the sliced l-value reference of "var".
The values of "value" are assigned to the positions in the variable. "var"
that are selected by the slice parameters. The slice parameters "begin, "end",
"strides", etc. work exactly as in "StridedSlice" . 

## Inputs

Five inputs, including:
- var: A mutable ND Tensor of type BasicType.
Support Dtype: [float16,float32,int32,int16,bfloat16], Support format: [ND].
- begin: A mutable ND Tensor of type IndexNumberType. Support dtype: [int64], support format: [ND].
Specifies the index of the first value to select.
- end: A mutable ND Tensor of type IndexNumberType. Support dtype: [int64], support format: [ND].
Specifies the index of the last value to select.
- strides: A mutable ND Tensor of type IndexNumberType. Support dtype: [int64], support format: [ND].
Specifies the stride to select.
- input_value: A mutable ND Tensor of type BasicType .
Support Dtype: [float16,float32,int32,int16,bfloat16], Support format: [ND]. 

## Outputs

var: A mutable Tensor. Has the same type as "var" . 

## Attributes

- begin_mask: An optional int. Defaults to "0".
- end_mask: An optional int. Defaults to "0".
- ellipsis_mask: An optional int. Defaults to "0".
- new_axis_mask: An optional int. Defaults to "0".
- shrink_axis_mask: An optional int. Defaults to "0" .

## Attention Constraints

This operator currently does not support broadcasting. Therefore, the shape
of "value" must be exactly the shape produced by the slice of "var" . 
@see StridedSlice()

## Third-party framework compatibility

- Compatible with the TensorFlow operator StridedSlice.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
