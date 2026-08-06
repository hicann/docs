# Case

```c
REG_OP(Case)
    .INPUT(branch_index, DT_INT32)
    .DYNAMIC_INPUT(input, TensorType::ALL())
    .DYNAMIC_OUTPUT(output, TensorType::ALL())
    .DYNAMIC_GRAPH(branches)
    .OP_END_FACTORY_REG(Case)
```

## Brief

Select one of the subgraphs to pass the input tensors and return the output tensors . 

## Inputs

- branch_index: A int32 scalar which determines the selected subgraph.
- input: The input tensors, which will be passed to the subgraph . It's a dynamic input.

## Outputs

output: The output tensors returned by one of branches . It's a dynamic output. 

## Graphs

branches: A list of subgraphs, each of which takes 'input' and returns a list of tensors,
         whose types are the same as what every other subgraph returns . 

## Third-party framework compatibility

Compatible with the TensorFlow operator Case.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
