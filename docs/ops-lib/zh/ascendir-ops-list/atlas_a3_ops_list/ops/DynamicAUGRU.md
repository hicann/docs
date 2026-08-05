# DynamicAUGRU

```c
REG_OP(DynamicAUGRU)
    .INPUT(x, TensorType({DT_FLOAT16}))
    .INPUT(weight_input, TensorType({DT_FLOAT16}))
    .INPUT(weight_hidden, TensorType({DT_FLOAT16}))
    .INPUT(weight_att, TensorType({DT_FLOAT16}))
    .OPTIONAL_INPUT(bias_input, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(bias_hidden, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(seq_length, TensorType({DT_INT32, DT_FLOAT16}))
    .OPTIONAL_INPUT(init_h, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(output_h, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(update, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(update_att, TensorType({DT_FLOAT16, DT_FLOAT}))
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
    .OP_END_FACTORY_REG(DynamicAUGRU)
```

## Brief

DynamicAUGRU calculation.

## Inputs

eight inputs:
- x: A input 3D Tensor. Must be one of the following types: float16. The format must be FRACTAL_ZN_RNN.
- weight_input: A input 2D Tensor. Must be one of the following types: float16. The format must be FRACTAL_ZN_RNN.
- weight_hidden: A input 2D Tensor. Must be one of the following types: float16, float32. The format must be FRACTAL_ZN_RNN.
- weight_att: A input 2D Tensor. Must be one of the following types: float16. The format must be ND.
- bias_input: A input 1D Tensor. Must be one of the following types: float16, float32. The format must be ND.
- bias_hidden: A input 1D Tensor. Must be one of the following types: float16, float32. The format must be ND.
- seq_length: A input Tensor. Dimension is batch_size. Must be one of the following types: int32, float16.
The format must in ND.
- init_h: The initial hidden state. A optional input 3D Tensor. Must be one of the following types: float16, float32.
The format must be FRACTAL_ZN_RNN.

## Outputs

seven outputs:
- y: A 3D Tensor. Must be one of the following types: float16, float32.
- output_h:A 3D Tensor. Must be one of the following types: float16, float32.
- update:Must A 3D Tensor. Must be one of the following types: float16, float32.
- update_att: A 3D Tensor. Must be one of the following types: float16, float32.
- reset:Must  A 3D Tensor. Must be one of the following types: float16, float32.
- new: A 3D Tensor. Must be one of the following types: float16, float32.
- hidden_new: A 3D Tensor. Must be one of the following types: float16, float32.

## Attributes

- direction:An string identifying the direction in the op. Default to "UNIDIRECTIONAL". Only UNIDIRECTIONAL is currently supported.
- cell_depth:An integer identifying the cell depth in the op. Default to 1.
- keep_prob:An float identifying the keep prob in the op. Default to 1.
- cell_clip:An float identifying the cell clip in the op. Default to -1.
- num_proj:An integer identifying the num projection in the op. Default to 0.
- time_major:An bool identifying the time major in the op. Default to true.
- activation:An string identifying the type of activation function in the op. Default to "tanh". Only tanh is currently supported.
- gate_order:An string identifying the gate order in weight and bias. Default to "zrh". "rzh" is another option.
- reset_after:An bool identifying whether to apply reset gate after matrix multiplication. Default to true.
- is_training:An bool identifying is training in the op. Default to true.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- input1 weight_input: float16
- input2 weight_hidden: float16,float32
- input3 weight_att: float16
- input4 bias_input: float16,float32
- input5 bias_hidden: float16,float32
- input6 seq_length: float16,int32
- input7 init_h: float16,float32
- output0 y: float16,float32
- output1 output_h: float16,float32
- output2 update: float16,float32
- output3 update_att: float16,float32
- output4 reset: float16,float32
- output5 new: float16,float32
- output6 hidden_new: float16,float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
