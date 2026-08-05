# Variable

```c
REG_OP(Variable)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType::ALL())
    .ATTR(index, Int, 0)
    .ATTR(value, Tensor, Tensor())
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .OP_END_FACTORY_REG(Variable)
```

## Brief

Creates a variable tensor . 

## Inputs

x: A tensor, used to assign a value to the variable tensor internally.
The caller does not need to pass the value of the variable tensor . 

## Outputs

y: The created variable tensor . 

## Attributes

- index: An integer. Index of the input tensor.
- value: A tensor, used to pass and record the value of the variable tensor.
- container: A string. The container of the variable tensor.
- shared_name: A string. The shared name of the variable tensor .

## Third-party framework compatibility

Compatible with the TensorFlow operator Variable.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
