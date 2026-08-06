# If

```c
REG_OP(If)
    .INPUT(cond, TensorType::ALL())
    .DYNAMIC_INPUT(input, TensorType::ALL())
    .DYNAMIC_OUTPUT(output, TensorType::ALL())
    .GRAPH(then_branch)
    .GRAPH(else_branch)
    .OP_END_FACTORY_REG(If)
```

## Brief

Select one of the subgraphs to pass the input tensors and return the output tensors.
      If "cond" means True, the selected subgraph is "then_branch".
      Otherwise, the selected subgraph is "else_branch" . 

## Inputs

- cond: A Tensor. If "cond" is not a scalar of boolean type,
         it will be converted to a boolean according to the following rule:
         if "cond" is a numerical scalar, non-zero means True and zero means False;
         if "cond" is a string scalar, non-empty means True and empty means False;
         if "cond" is not a scalar, non-empty means True and empty means False.
- input: The input tensors . It's a dynamic input.

## Outputs

output: The output tensors returned by either then_branch(input) or else_branch(input).
       It's a dynamic output. 

## Graphs

- then_branch: A subgraph takes 'input' and returns a list of tensors,
                whose types are the same as what else_branch returns.
- else_branch: A subgraph takes 'input' and returns a list of tensors,
                whose types are the same as what then_branch returns . 

## Third-party framework compatibility

Compatible with the TensorFlow operator If.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
