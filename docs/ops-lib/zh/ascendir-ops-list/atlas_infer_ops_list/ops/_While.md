# _While

```c
REG_OP(_While)
    .DYNAMIC_INPUT(input, TensorType::ALL())
    .DYNAMIC_OUTPUT(output, TensorType::ALL())
    .GRAPH(cond)
    .GRAPH(body)
    .OP_END_FACTORY_REG(_While)
```

## Brief

Cyclic execute the "body" subgraph until the return tensor of "cond" subgraph means False . 

## Inputs

input: The input tensors . It's a dynamic input. 

## Outputs

output: The output tensors returned by "body". Has the same type as "input" . 

## Graphs

- cond: A subgraph takes 'input' and returns a tensor.
         If the tensor is not a scalar of boolean type,
         it will be converted to a boolean according to the following rule:
         if it is a numerical scalar, non-zero means True and zero means False;
         if it is a string scalar, non-empty means True and empty means False;
         if it is not a scalar, non-empty means True and empty means False.
- body: A subgraph takes 'input' and returns another list of tensors .

## Third-party framework compatibility

Compatible with the TensorFlow operator _While.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
