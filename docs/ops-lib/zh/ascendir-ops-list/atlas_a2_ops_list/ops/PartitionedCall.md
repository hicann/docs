# PartitionedCall

```c
REG_OP(PartitionedCall)
    .DYNAMIC_INPUT(args, TensorType::ALL())
    .DYNAMIC_OUTPUT(output, TensorType::ALL())
    .GRAPH(f)
    .ATTR(config, String, "")
    .ATTR(config_proto, String, "")
    .ATTR(executor_type, String, "")
    .OP_END_FACTORY_REG(PartitionedCall)
```

## Brief

Pass the input tensors to the subgraph "f" and return the output tensors . 

## Inputs

args: The input tensors, which will be passed to "f" . It's a dynamic input. 

## Outputs

output: The output tensors returned by "f" . It's a dynamic output. 

## Graphs

f: A subgraph takes 'args' and returns another list of tensors . 

## Attributes

- config: An optional string, default as "".
- config_proto: An optional string, default as "".
- executor_type: An optional string, default as "" .

## Third-party framework compatibility

Compatible with the TensorFlow operator PartitionedCall.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
