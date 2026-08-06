# FileConstant

```c
REG_OP(FileConstant)
    .OUTPUT(y, TensorType::ALL())
    .ATTR(file_path, String, "")
    .ATTR(file_id, String, "")
    .REQUIRED_ATTR(shape, ListInt)
    .REQUIRED_ATTR(dtype, Type)
    .OP_END_FACTORY_REG(FileConstant)
```

## Brief

Creates a file constant tensor, The operator is used to process the very large weight which is store in file. 

## Outputs

y: The FileConstant tensor. 

## Attributes

file_path: A string, used to record file path. 
file_id: A string, used to record file id. 
shape: data shape. 
dtype: data type. 


---

[Back to Operator Specifications (Ascend950)](../README.md)
