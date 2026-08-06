# DynamicRNNV2

```c
REG_OP(DynamicRNNV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(weight_input, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(weight_hidden, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(b, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(seq_length, TensorType({DT_INT32, DT_FLOAT16}))
    .OPTIONAL_INPUT(init_h, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(init_c, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(wci, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(wcf, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(wco, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(mask, TensorType({DT_UINT8}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(output_h, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(output_c, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(i, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(j, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(f, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(o, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(tanhc, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(cell_type, String, "LSTM")
    .ATTR(direction, String, "UNIDIRECTIONAL")
    .ATTR(cell_depth, Int, 1)
    .ATTR(use_peephole, Bool, false)
    .ATTR(keep_prob, Float, 1.0)
    .ATTR(cell_clip, Float, -1.0)
    .ATTR(num_proj, Int, 0)
    .ATTR(time_major, Bool, true)
    .ATTR(activation, String, "tanh")
    .ATTR(recurrent_activation, String, "sigmoid")
    .ATTR(forget_bias, Float, 0.0)
    .ATTR(gate_order, String, "ijfo")
    .ATTR(stateful, Bool, false)
    .ATTR(merge_mode, String, "concat")
    .ATTR(is_training, Bool, true)
    .OP_END_FACTORY_REG(DynamicRNNV2)
```

## Brief

: DynamicRNNV2 calculation.

## Inputs

ten inputs:
- x:A required Tensor. Must be one of the following types: float16, float32.
- weight_input:A required Tensor. Must be one of the following types: float16, float32.
- weight_hidden:A required Tensor. Must be one of the following types: float16, float32.
- b:A required Tensor. Must be one of the following types: float16, float32. The format must be ND.
- seq_length:A optional Tensor. Must be one of the following types: float16, int32.
- init_h:A optional Tensor. Must be one of the following types: float16, float32.
- init_c:A optional Tensor. Must be one of the following types: float16, float32.
- wci:A optional Tensor. Must be one of the following types: float16, float32.
- wcf:A optional Tensor. Must be one of the following types: float16, float32.
- wco:A optional Tensor. Must be one of the following types: float16, float32.
- mask:A optional Tensor. Must be one of the following types: uint8. The format must be ND .

## Outputs

eight outputs:
- y:A Tensor. Must be one of the following types: float16, float32.
- output_h:A Tensor. Must be one of the following types: float16, float32.
Return the last output_h.
- output_c:A Tensor. Must be one of the following types: float16, float32.
Return the last output_c.
- i:A Tensor. Must be one of the following types: float16, float32.
- j:A Tensor. Must be one of the following types: float16, float32.
- f:A Tensor. Must be one of the following types: float16, float32.
- o:A Tensor. Must be one of the following types: float16, float32.
- tanhc:A Tensor. Must be one of the following types: float16, float32.

## Attributes

- cell_type:An string identifying the cell type in the op.
Default to "LSTM". Only LSTM is currently supported.
- direction:An string identifying the direction in the op.
Default to "UNIDIRECTIONAL". Support "UNIDIRECTIONAL" and "REDIRECTIONAL".
- cell_depth:An integer identifying the cell depth in the op.
Default to 1. Only 1 is currently supported.
- use_peephole:An bool identifying if use peephole in the op.
Default to false. Only false is currently supported.
- keep_prob:An float identifying the keep prob in the op.
Default to 1. Only 1.0 is currently supported.
- cell_clip:An float identifying the cell clip in the op.
Default to -1. Only -1.0 is currently supported.
- num_proj:An integer identifying the num projection in the op.
Default to 0. Only 0 is currently supported.
- time_major:An bool identifying the time major in the op. Default to true.
- activation:An string identifying the type of activation function in
the op. Default to "tanh". Only "tanh" is currently supported.
- recurrent_activation:An string identifying the type of activation
function in the op. Default to "sigmoid". Only support "sigmoid" in
Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component
and Atlas A3 Training Series Product/Atlas A3 Inference Series Product.
Support "sigmoid" and "hard_sigmoid"
in other series produces. In general, set "hard_sigmoid" for TF Keras LSTM.
- forget_bias:An float identifying the forget bias in the op. Default to 0.
- gate_order:An string identifying the type of gate order in the op.
Support "ijfo" and "ifco". Default to "ijfo".
Set "ijfo" for TF operator LSTM, Set "ifco" for TF Keras LSTM.
- stateful: An bool identifying the type of stateful in the op.
Default to fasle. Only false is currently supported.
- merge_mode: An string identifying the type of merge_modein the op.
Default to "concat". Only "concat" is currently supported
- is_training:An bool identifying is training in the op. Default to true .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- input1 weight_input: float16
- input2 weight_hidden: float16
- input3 b: float16,float32
- input4 seq_length: float16,int32
- input5 init_h: float16
- input6 init_c: float16,float32
- input7 wci: float16
- input8 wcf: float16
- input9 wco: float16
- input10 mask: uint8
- output0 y: float16,float32
- output1 output_h: float16
- output2 output_c: float16,float32
- output3 i: float16,float32
- output4 j: float16,float32
- output5 f: float16,float32
- output6 o: float16,float32
- output7 tanhc: float16,float32

## Third-party framework compatibility

Compatible with the TF operator LSTM or TF keras operator LSTM or the Pytorch operator LSTM.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
