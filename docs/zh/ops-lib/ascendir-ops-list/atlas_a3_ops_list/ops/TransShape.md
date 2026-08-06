# TransShape

```c
REG_OP(TransShape)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType::ALL())
    .ATTR(outShape,ListInt ,{})
    .OP_END_FACTORY_REG(TransShape)
```

## Brief

Change the shape of output according to the attr outShape

## Inputs

x: A Tensor. 

## Outputs

y: A Tensor. Has the same type as "x".It's required and the value should equal to output_num. 

## Attributes

outShape: The shape of output will be inferred according to the attribute


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
