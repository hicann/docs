# StridedSliceAssignV2

```c
REG_OP(StridedSliceAssignV2)
    .INPUT(var, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_INT32, DT_INT64, DT_DOUBLE, DT_INT8}))
    .INPUT(input_value, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_INT32, DT_INT64, DT_DOUBLE, DT_INT8}))
    .INPUT(begin, TensorType::IndexNumberType())
    .INPUT(end, TensorType::IndexNumberType())
    .INPUT(strides, TensorType::IndexNumberType())
    .OPTIONAL_INPUT(axes, TensorType::IndexNumberType())
    .OUTPUT(var, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_INT32, DT_INT64, DT_DOUBLE, DT_INT8}))
    .OP_END_FACTORY_REG(StridedSliceAssignV2)
```

## Brief

Assigns "value" to the sliced l-value reference of "var".
The values of "value" are assigned to the positions in the variable. "var"
that are selected by the slice parameters. The slice parameters "begin, "end",
"strides", etc. work exactly as in "StridedSlice" . 

## Inputs

Five inputs, including:
- var: A mutable ND Tensor of type BasicType.
Support dtype: [float16, float32, bfloat16, int32, int64, double, int8], Supoort format: [ND]. 
- input_value: A mutable ND Tensor of type BasicType .
Support dtype: [float16, float32, bfloat16, int32, int64, double, int8], Supoort format: [ND]. 
- begin: A mutable ND Tensor of type IndexNumberType.
Support dtype: [int64], Supoort format: [ND]. 
Specifies the index of the first value to select.
- end: A mutable ND Tensor of type IndexNumberType.
Support dtype: [int64], Supoort format: [ND]. 
Specifies the index of the last value to select.
- strides: A mutable ND Tensor of type IndexNumberType.
Support dtype: [int64], Supoort format: [ND]. 
Specifies the stride to select.
- axes: Optional. A mutable ND Tensor of type IndexNumberType.
Support dtype: [int64], Supoort format: [ND]. 
Specifies the stride to select. 

## Outputs

var: A mutable Tensor. Has the same type and format as "var" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: bfloat16,double,float16,float32,int8,int32,int64
- input1 input_value: bfloat16,double,float16,float32,int8,int32,int64
- input2 begin: int64
- input3 end: int64
- input4 strides: int64
- input5 axes: int64
- output0 var: bfloat16,double,float16,float32,int8,int32,int64

## Attention Constraints

This operator currently does not support broadcasting. Therefore, the shape
of "value" must be exactly the shape produced by the slice of "var" . 
@see StridedSlice()

## Third-party framework compatibility

- Compatible with the TensorFlow operator StridedSlice.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
