# DynamicGRUV2

```c
REG_OP(DynamicGRUV2)
    .INPUT(x, TensorType({DT_FLOAT16}))
    .INPUT(weight_input, TensorType({DT_FLOAT16}))
    .INPUT(weight_hidden, TensorType({DT_FLOAT16}))
    .OPTIONAL_INPUT(bias_input, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(bias_hidden, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(seq_length, TensorType({DT_INT32, DT_FLOAT16}))
    .OPTIONAL_INPUT(init_h, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(output_h, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(update, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(reset, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(new, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(hidden_new, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(direction, String, "UNIDIRECTIONAL")
    .ATTR(cell_depth, Int, 1)
    .ATTR(keep_prob, Float, 1.0)
    .ATTR(cell_clip, Float, -1.0)
    .ATTR(num_proj, Int, 0)
    .ATTR(time_major, Bool, true)
    .ATTR(activation, String, "tanh")
    .ATTR(gate_order, String, "zrh")
    .ATTR(reset_after, Bool, true)
    .ATTR(is_training, Bool, true)
    .OP_END_FACTORY_REG(DynamicGRUV2)
```

## Brief

DynamicGRUV2 calculation.

## Inputs

seven inputs:
- x:Must be one of the following types: float16.
- weight_input:Must be one of the following types: float16.
- weight_hidden:Must be one of the following types: float16.
- bias_input:Must be one of the following types: float16, float32. The format must be ND.
- bias_hidden:Must be one of the following types: float16, float32. The format must be ND.
- seq_length:Must be one of the following types: int32, float16 in ND.
- init_h:Must be one of the following types: float16, float32.

## Outputs

six outputs:
- y:Must be one of the following types: float16, float32.
- output_h:Must be one of the following types: float16, float32.
- update:Must be one of the following types: float16, float32.
- reset:Must be one of the following types: float16, float32.
- new:Must be one of the following types: float16, float32.
- hidden_new:Must be one of the following types: float16, float32.

## Attributes

- direction:An string identifying the direction in the op. Default to "UNIDIRECTIONAL". Support "UNIDIRECTIONAL"
and "REDIRECTIONAL".
- cell_depth:An integer identifying the cell depth in the op. Default to 1.
- keep_prob:An float identifying the keep prob in the op. Default to 1.
- cell_clip:An float identifying the cell clip in the op. Default to -1.
- num_proj:An integer identifying the num projection in the op. Default to 0.
- time_major:An bool identifying the time major in the op. Default to true.
- activation:An string identifying the type of activation function in the op. Default to "tanh". Only tanh is
currently supported.
- gate_order:An string identifying the gate order in weight and bias. Default to "zrh". "rzh" is another option.
- reset_after:An bool identifying whether to apply reset gate after matrix multiplication. Default to true.
- is_training:An bool identifying is training in the op. Default to true.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
