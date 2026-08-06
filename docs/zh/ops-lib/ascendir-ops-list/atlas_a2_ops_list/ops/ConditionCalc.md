# ConditionCalc

```c
REG_OP(ConditionCalc)
    .DYNAMIC_INPUT(x, TensorType::ALL())
    .OUTPUT(cond, TensorType({DT_INT32}))
    .REQUIRED_ATTR(cond_func, String)
    .REQUIRED_ATTR(x_dependency, ListInt)
    .OP_END_FACTORY_REG(ConditionCalc)
```

## Brief

Calculate condition value by input tensor which will be used for if input or case input. 

## Inputs

x: the data or shape of input.  all types are available. It's a dynamic input.

## Outputs

cond: condition value calculated by cond fuction.
It will be cond input of if or branch_index input of case. 

## Attributes

- cond_func: A string. real condition function registered to calculate condition value.
- x_dependency: List of int. It should be the same number of inputs: 0(shape) 1(data).


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
