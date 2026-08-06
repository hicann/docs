# ConstPlaceHolder

```c
REG_OP(ConstPlaceHolder)
    .OUTPUT(y, TensorType::ALL())
    .REQUIRED_ATTR(origin_shape, ListInt)
    .REQUIRED_ATTR(origin_format, Int)
    .REQUIRED_ATTR(storage_shape, ListInt)
    .REQUIRED_ATTR(storage_format, Int)
    .REQUIRED_ATTR(expand_dim_rules, String)
    .REQUIRED_ATTR(dtype, Type)
    .REQUIRED_ATTR(addr, Int)
    .REQUIRED_ATTR(size, Int)
    .ATTR(placement, Int, 1)
    .OP_END_FACTORY_REG(ConstPlaceHolder)
```

## Brief

Creates a Const PlaceHolder tensor.
This operator is used to handle inputs where the address does not change but the value is uncertain.
Converting the input to this type will help improve the execution performance of the graph
(avoiding the input address from being repeatedly refreshed). 

## Outputs

y: The ConstPlaceHolder tensor. 

## Attributes

origin_shape: Required. The origin shape of a tensor. 
origin_format: Required. The origin format of a tensor. 
storage_shape: Required. The storage shape of a tensor. 
storage_format: Required. The storage format of a tensor.
expand_dim_rules: Required. The expand dim rules while trans tensor with 
                            origin_shape、origin_format and storage_format into storage_shape. 
dtype: Required. The dtype of a tensor. 
addr: Required. The address of a tensor 
size: Required. The size of address. 
placement: The placement of a tensor, 0 represents host, 1 represents device, and the default value is 1. 


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
