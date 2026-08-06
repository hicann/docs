# FlattenV2

```c
REG_OP(FlattenV2)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType::ALL())
    .ATTR(axis, Int, 1)
    .ATTR(end_axis, Int, -1)
    .OP_END_FACTORY_REG(FlattenV2)
```

## Brief

Flattens the input tensor to one-dimensional . 

## Inputs

x: An ND tensor. All data types are supported. 

## Outputs

y: The flattened ND tensor. All data types are supported. 

## Attributes

- axis: An optional int32, specifying the first axis to flatten. All preceding axes are retained in the output. Defaults to "1".
- end_axis: An optional int32, specifying the last axis to flatten. All following axes are retained in the output. Defaults to "-1" .

## Attention Constraints

"axis" and "end_axis" must be within the dimension range of the input. This operator cannot be directly called by the acllopExecute API.

## Third-party framework compatibility

Compatible with the Caffe operator Flatten.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
