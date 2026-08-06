# DynamicRNNGrad

```c
REG_OP(DynamicRNNGrad)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(w, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(b, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(init_h, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(init_c, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(h, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(c, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(dy, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(dh, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(dc, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(i, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(j, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(f, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(o, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(tanhct, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(seq_length, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(mask, TensorType({DT_UINT8}))
    .OPTIONAL_INPUT(wci, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(wcf, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(wco, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(dw, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(db, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(dx, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(dh_prev, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(dc_prev, TensorType({DT_FLOAT16, DT_FLOAT}))
    .DYNAMIC_OUTPUT(dwci, TensorType({DT_FLOAT16, DT_FLOAT}))
    .DYNAMIC_OUTPUT(dwcf, TensorType({DT_FLOAT16, DT_FLOAT}))
    .DYNAMIC_OUTPUT(dwco, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(cell_type, String, "LSTM")
    .ATTR(direction, String, "UNIDIRECTIONAL")
    .ATTR(cell_depth, Int, 0)
    .ATTR(use_peephole, Bool, false)
    .ATTR(keep_prob, Float, -1.0)
    .ATTR(cell_clip, Float, -1.0)
    .ATTR(num_proj, Int, 0)
    .ATTR(time_major, Bool, true)
    .ATTR(forget_bias, Float, 0.0)
    .ATTR(gate_order, String, "ijfo")
    .OP_END_FACTORY_REG(DynamicRNNGrad)
```

## Brief

DynamicRNNGrad calculation.

## Inputs

- x:A 4D Tensor. Must be one of the following types: float16, float32.
- w:A 4D Tensor. Must be one of the following types: float16, float32.
- b:A 1D Tensor. Must be one of the following types: float16, float32.
- y:A 1D Tensor. Must be one of the following types: int32.
- init_h:A 4D Tensor.
Must be one of the following types: float16, float32.
- init_c:A 4D Tensor.
Must be one of the following types: float16, float32.
- h:A 4D Tensor. Must be one of the following types: float16, float32.
- c:A 4D Tensor. Must be one of the following types: float16, float32.
- dy:A 4D Tensor. Must be one of the following types: float16, float32.
- dh:A 4D Tensor. Must be one of the following types: float16, float32.
- dc:A 4D Tensor. Must be one of the following types: float16, float32.
- i:A 4D Tensor. Must be one of the following types: float16, float32.
- j:A 4D Tensor. Must be one of the following types: float16, float32.
- f:A 4D Tensor. Must be one of the following types: float16, float32.
- o:A 4D Tensor. Must be one of the following types: float16, float32.
- tanhct:A 4D Tensor.
Must be one of the following types: float16, float32.
- seq_length:A 1D Tensor. Must be one of the following types: int32.
- mask:A 1D Tensor. Must be one of the following types: uint8.
- wci:A 4D Tensor. Must be one of the following types: float16, float32.
- wcf:A 4D Tensor. Must be one of the following types: float16, float32.
- wco:A 4D Tensor. Must be one of the following types: float16, float32.

## Outputs

- dw:A 4D Tensor. Must be one of the following types: float16, float32.
- db:A 4D Tensor. Must be one of the following types: float16, float32.
- dx:A 4D Tensor. Must be one of the following types: float16, float32.
- dh_prev:A 4D Tensor.
Must be one of the following types: float16, float32.
- dc_prev:A 4D Tensor.
Must be one of the following types: float16, float32.
- dwci:A 4D Tensor. Must be one of the following types: float16, float32.
- dwcf:A 4D Tensor. Must be one of the following types: float16, float32.
- dwco:A 4D Tensor. Must be one of the following types: float16, float32.

## Attributes

- cell_type:An string identifying the cell type in the op.
Default to "LSTM". Only LSTM is currently supported.
- direction:An string identifying the direction in the op.
Default to "UNIDIRECTIONAL". Only UNIDIRECTIONAL is currently supported.
- cell_depth:An integer identifying the cell depth in the op.
Default to 0.
- use_peephole:An bool identifying if use peephole in the op.
Default to false.
- keep_prob:An float identifying the keep prob in the op. Default to -1.
- cell_clip:An float identifying the cell clip in the op. Default to -1.
- num_proj:An integer identifying the num projection in the op.
Default to 0.
- time_major:An bool identifying the time major in the op.
Default to true.
- forget_bias:An float identifying the forget bias in the op.
Default to 0.
- gate_order:An string identifying the type of gate order in the op.
Support "ijfo" and "ifjo". Default to "ijfo".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 w: float16,float32
- input2 b: float16,float32
- input3 y: float16,float32
- input4 init_h: float16,float32
- input5 init_c: float16,float32
- input6 h: float16,float32
- input7 c: float16,float32
- input8 dy: float16,float32
- input9 dh: float16,float32
- input10 dc: float16,float32
- input11 i: float16,float32
- input12 j: float16,float32
- input13 f: float16,float32
- input14 o: float16,float32
- input15 tanhct: float16,float32
- input16 seq_length: float16,float32
- input17 mask: uint8
- input18 wci: float16,float32
- input19 wcf: float16,float32
- input20 wco: float16,float32
- output0 dw: float16,float32
- output1 db: float16,float32
- output2 dx: float16,float32
- output3 dh_prev: float16,float32
- output4 dc_prev: float16,float32
- output5 dwci: float16,float32
- output6 dwcf: float16,float32
- output7 dwco: float16,float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
