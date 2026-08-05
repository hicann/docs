# RefData

```c
REG_OP(RefData)
    .INPUT(x, "T")
    .OUTPUT(y, "T")
    .ATTR(index, Int, 0)
    .DATATYPE(T, TensorType::ALL())
    .OP_END_FACTORY_REG(RefData)
```

## Brief

Input data for other operators.
It could be overwritten by ref ops, acting like a variable. 

## Inputs

x: A tensor. 

## Outputs

x: A tensor. Same with input name, which means ref with input. 

## Attributes

index: Index of the input tensor.The data type must be int32 or int64.
Assume that net has two data nodes and one ref_data node, previous two data index set as (0, 1),
and the left ref_data should be set 2. 


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
