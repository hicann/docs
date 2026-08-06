# SortV2

```c
REG_OP(SortV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .ATTR(axis, Int, -1)
    .ATTR(descending, Bool, false)
    .OP_END_FACTORY_REG(SortV2)
```

## Brief

sort the input tensor without returning the value of index.

## Inputs

x:  A Tensor.Supported type: float16, float32, double, bfloat16. Supported format: ND . 

## Outputs

y:  A Tensor. Must have the same type and format as x . 

## Attributes

- axis: An optional int. The dimension to sort along. This value defaults to -1.
- descending: An optional bool. Controls the sorting order (ascending or descending).
This value defaults to False . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Attention Constraints

- Axis should select the last dim.
- When the sorting data is less than 150K, it is recommended to use this tbe ops,
and the descending performance is better than the ascending.
- The upper limit of data on Atlas Training Series Product is 2000K.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
