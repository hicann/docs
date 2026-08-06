# FlowFunc

```c
REG_OP(FlowFunc)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, \
        DT_INT16, DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_UINT32, DT_UINT64, DT_BOOL, DT_DOUBLE}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, \
        DT_INT16, DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_UINT32, DT_UINT64, DT_BOOL, DT_DOUBLE}))
    .REQUIRED_ATTR(bin_path, String)
    .REQUIRED_ATTR(func_name, String)
    .ATTR(output_shapes, ListListInt, {})
    .REQUIRED_ATTR(output_types, ListType)
    .OP_END_FACTORY_REG(FlowFunc)
```

## Brief

User define function process. 

## Inputs

- x: A list of input tensor objects. It's a dynamic input.

## Outputs

- y: A list of output tensor objects. It's a dynamic output.

## Attributes

- bin_path: User's binary path.
- func_name: User defined function name.
- output_types: Types of outputs data.
- output_shapes: Shapes of outputs data.
- _flow_attr_process_node_engine_id: Default process node engine of FlowFunc.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
