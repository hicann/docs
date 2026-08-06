# DynamicRNNV3

```c
REG_OP(DynamicRNNV3)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(w, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(b, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(seq_length, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(init_h, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(init_c, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(wci, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(wcf, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(wco, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(mask, TensorType({DT_UINT8}))
    .OPTIONAL_INPUT(real_mask, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(project, TensorType({DT_FLOAT16, DT_FLOAT}))
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
    .ATTR(is_training, Bool, true)
    .OP_END_FACTORY_REG(DynamicRNNV3)
```

## Brief

: DynamicRNNV3 calculation.

## Inputs

ten inputs:
- x:A required 4D Tensor. Must be one of the following types: float16, float32.
- w:A required 4D Tensor. Must be one of the following types: float16, float32.
- b:A required 1D Tensor. Must be one of the following types: float16, float32. The format must be ND.
- seq_length:A optional 1D Tensor. Must be one of the following types: int32. The format must be ND.
- init_h:A optional 4D Tensor. Must be one of the following types: float16, float32.
- init_c:A optional 4D Tensor. Must be one of the following types: float16, float32.
- wci:A 4D optional Tensor. Must be one of the following types: float16, float32.
- wcf:A 4D optional Tensor. Must be one of the following types: float16, float32.
- wco:A 4D optional Tensor. Must be one of the following types: float16, float32.
- mask:A 1D optional Tensor. Must be one of the following types: uint8. The format must be ND .
- real_mask:A 4D optional Tensor. Must be one of the following types: float16, float32.
- project:A 4D optional Tensor. Must be one of the following types: float16, float32.

## Outputs

eight outputs:
- y:A 4D Tensor. Must be one of the following types: float16, float32.
- output_h:A 4D Tensor. Must be one of the following types: float16, float32.
- output_c:A 4D Tensor. Must be one of the following types: float16, float32.
- i:A 4D Tensor. Must be one of the following types: float16, float32.
- j:A 4D Tensor. Must be one of the following types: float16, float32.
- f:A 4D Tensor. Must be one of the following types: float16, float32.
- o:A 4D Tensor. Must be one of the following types: float16, float32.
- tanhc:A 4D Tensor. Must be one of the following types: float16, float32.

## Attributes

- cell_type:An string identifying the cell type in the op. Default to "LSTM". Only LSTM is currently supported.
- direction:An string identifying the direction in the op. Default to "UNIDIRECTIONAL". Only UNIDIRECTIONAL is currently supported.
- cell_depth:An integer identifying the cell depth in the op. Default to 1.
- use_peephole:An bool identifying if use peephole in the op. Default to false.
- keep_prob:An float identifying the keep prob in the op. Default to 1.
- cell_clip:An float identifying the cell clip in the op. Default to -1.
- num_proj:An integer identifying the num projection in the op. Default to 0.
- time_major:An bool identifying the time major in the op. Default to true.
- activation:An string identifying the type of activation function in the op. Default to "tanh". Only tanh is currently supported.
- forget_bias:An float identifying the forget bias in the op. Default to 0.
- is_training:An bool identifying is training in the op. Default to true .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- input1 w: float16
- input2 b: float16,float32
- input3 seq_length: int32
- input4 init_h: float16
- input5 init_c: float16,float32
- input6 wci: float16,float32
- input7 wcf: float16,float32
- input8 wco: float16,float32
- input9 mask: uint8
- input10 real_mask: float16,float32
- input11 project: float16
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

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
