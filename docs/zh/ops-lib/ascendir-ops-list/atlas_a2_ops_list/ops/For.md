# For

```c
REG_OP(For)
    .INPUT(start, DT_INT32)
    .INPUT(limit, DT_INT32)
    .INPUT(delta, DT_INT32)
    .DYNAMIC_INPUT(input, TensorType::ALL())
    .DYNAMIC_OUTPUT(output, TensorType::ALL())
    .GRAPH(body)
    .OP_END_FACTORY_REG(For)
```

## Brief

Cyclic execute the "body" subgraph until the first input of For op exceed upper bound . 

## Inputs

- start: An int32 scalar. The lower bound.
- limit: An int32 scalar. The upper bound.
- delta: An int32 scalar. The step size.
- input: The input tensors, which will be passed to "body" . It's a dynamic input.

## Outputs

output: The output tensors returned by "body". Has the same type as "input" . It's a dynamic output. 

## Graphs

body: A subgraph takes 'input' and returns another list of tensors . 

## Third-party framework compatibility

Compatible with the TensorFlow operator For.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
