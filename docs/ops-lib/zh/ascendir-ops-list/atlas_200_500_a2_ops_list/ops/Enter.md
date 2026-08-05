# Enter

```c
REG_OP(Enter)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE,
        DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_UINT8, DT_UINT16, DT_UINT32,
        DT_UINT64, DT_BOOL}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE,
        DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_UINT8, DT_UINT16, DT_UINT32,
        DT_UINT64, DT_BOOL}))
    .REQUIRED_ATTR(frame_name, String)
    .REQUIRED_ATTR(is_constant, Bool)
    .OP_END_FACTORY_REG(Enter)
```

## Brief

Creates or finds a child frame, and makes "x" available to the child
      frame. This op is used together with Exit to create loops in the graph.
      The Executor uses the unique "frame_name" to identify frames.
      If "is_constant" is "true", output "y" is a constant in the child
      frame; otherwise it may be changed in the child frame .

## Inputs

x: The tensor to be made available to the child frame.
  Must be one of the following types: float16, float32, float64, int8,
  int16, int32, int64, uint8, uint16, uint32, uint64, bool . 

## Outputs

y: A Tensor. Has the same type as "x" . 
@see Exit()

## Attributes

- frame_name: A required string. The name of the child frame.
- is_constant: A required bool. If true, the output is constant in
                the child frame . 

## Third-party framework compatibility

Compatible with the TensorFlow operator Enter.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
