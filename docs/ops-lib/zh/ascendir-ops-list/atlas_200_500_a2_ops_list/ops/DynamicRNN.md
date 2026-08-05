# DynamicRNN

```c
REG_OP(DynamicRNN)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(w, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(b, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(seq_length, TensorType({DT_INT32, DT_FLOAT16, DT_FLOAT}))
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
    .ATTR(forget_bias, Float, 0.0)
    .ATTR(gate_order, String, "ijfo")
    .ATTR(is_training, Bool, true)
    .OP_END_FACTORY_REG(DynamicRNN)
```

## Brief

: DynamicRNN calculation.

## Inputs

ten inputs:
- x:A required 3D Tensor. Must be one of the following types: float16, float32.
The format must be ND.
- w:A required 2D Tensor. Must be one of the following types: float16, float32.
The format must be ND.
- b:A required 1D Tensor. Must be one of the following types: float16, float32.
The format must be ND.
- seq_length:A optional 3D Tensor. Must be one of the following types: float16, int32, float32.
The format must be ND.
- init_h:A optional Tensor. Must be one of the following types: float16, float32.
The format must be ND.
- init_c:A optional Tensor. Must be one of the following types: float16, float32.
The format must be ND.
- wci:A optional reserved Tensor. Must be one of the following types: float16, float32. The format must be ND.
- wcf:A optional reserved Tensor. Must be one of the following types: float16, float32. The format must be ND.
- wco:A optional reserved Tensor. Must be one of the following types: float16, float32. The format must be ND.
- mask:A optional reserved Tensor. Must be one of the following types: uint8. The format must be ND.

## Outputs

eight outputs:
- y:A 3D Tensor. Must be one of the following types: float16, float32. The format must be ND.
- output_h:A 3D Tensor. Must be one of the following types: float16, float32. The format must be ND.
- output_c:A 3D Tensor. Must be one of the following types: float16, float32. The format must be ND.
- i:A 3D Tensor. Must be one of the following types: float16, float32. The format must be ND.
- j:A 3D Tensor. Must be one of the following types: float16, float32. The format must be ND.
- f:A 3D Tensor. Must be one of the following types: float16, float32. The format must be ND.
- o:A 3D Tensor. Must be one of the following types: float16, float32. The format must be ND.
- tanhc:A 3D Tensor. Must be one of the following types: float16, float32. The format must be ND.

## Attributes

- cell_type:An string identifying the cell type in the op.
Default to "LSTM". Only LSTM is currently supported.
- direction:An string identifying the direction in the op.
Default to "UNIDIRECTIONAL". Only UNIDIRECTIONAL is currently supported.
- cell_depth:An integer identifying the cell depth in the op.
Default to 1. Only 1 is currently supported.
- use_peephole:An bool identifying if use peephole in the op.
Default to false. Only false is currently supported.
- keep_prob:An float identifying the keep prob in the op. Default to 1.0.
- cell_clip:An float identifying the cell clip in the op. Default to -1.0.
- num_proj:An integer identifying the num projection in the op.
Default to 0. Only 0 is currently supported.
- time_major:An bool identifying the time major in the op. Default to true.
- activation:An string identifying the type of activation function in the op.
Default to "tanh". Only "tanh" is currently supported.
- forget_bias:An float identifying the forget bias in the op. Default to 0.
- gate_order:An string identifying the type of gate order in the op.
Support "ijfo" and "ifjo". Default to "ijfo".
- is_training:An bool identifying is training in the op. Default to true .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- input1 w: float16
- input2 b: float16,float32
- input3 seq_length: float16,int32
- input4 init_h: float16
- input5 init_c: float16,float32
- input6 wci: float16
- input7 wcf: float16
- input8 wco: float16
- input9 mask: uint8
- output0 y: float16,float32
- output1 output_h: float16
- output2 output_c: float16,float32
- output3 i: float16,float32
- output4 j: float16,float32
- output5 f: float16,float32
- output6 o: float16,float32
- output7 tanhc: float16,float32

## Third-party framework compatibility

Compatible with the TF operator LSTM.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
