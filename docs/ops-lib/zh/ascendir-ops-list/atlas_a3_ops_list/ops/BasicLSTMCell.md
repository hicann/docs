# BasicLSTMCell

```c
REG_OP(BasicLSTMCell)
    .INPUT(x, TensorType({DT_FLOAT16}))
    .INPUT(h, TensorType({DT_FLOAT16}))
    .INPUT(c, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(w, TensorType({DT_FLOAT16}))
    .INPUT(b, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(mask, TensorType({DT_UINT8}))
    .OUTPUT(ct, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(ht, TensorType({DT_FLOAT16}))
    .OUTPUT(it, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(jt, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(ft, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(ot, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(tanhct, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(keep_prob, Float, 1.0)
    .ATTR(forget_bias, Float, 1.0)
    .ATTR(state_is_tuple, Bool, true)
    .ATTR(activation, String, "tanh")
    .OP_END_FACTORY_REG(BasicLSTMCell)
```

## Brief

: Basic LSTM Cell forward calculation.

## Inputs

six inputs:
- x:A 4D Tensor. Must be one of the following types: float16. The format
must be FRACTAL_NZ.
- h:A 4D Tensor. Must be one of the following types: float16. The format
must be FRACTAL_NZ.
- c:A 4D Tensor. Must be one of the following types: float16, float32. The
format must be FRACTAL_NZ.
- w:A 4D Tensor. Must be one of the following types: float16. The format
must be FRACTAL_ZN_LSTM.
- b:A 1D Tensor. Must be one of the following types: float16, float32. The
format must be ND.
- mask:A optional 1D Tensor. Must be one of the following types: uint8. The
format must be ND. 

## Outputs

seven outputs:
- ct:A 4D Tensor. Must be one of the following types: float16, float32. The
format must be FRACTAL_NZ.
- ht:A 4D Tensor. Must be one of the following types: float16. The format
must be FRACTAL_NZ.
- it:A 4D Tensor. Must be one of the following types: float16, float32. The
format must be FRACTAL_NZ.
- jt:A 4D Tensor. Must be one of the following types: float16, float32. The
format must be FRACTAL_NZ.
- ft:A 4D Tensor. Must be one of the following types: float16, float32. The
format must be FRACTAL_NZ.
- ot:A 4D Tensor. Must be one of the following types: float16, float32. The
format must be FRACTAL_NZ.
- tanhct:A 4D Tensor. Must be one of the following types: float16, float32.
The format must be FRACTAL_NZ. 

## Attributes

- keep_prob:An Float identifying the keep prob in the op. Default to 1.
- forget_bias:An Float identifying the forget bias in the op. Default to 1.
- state_is_tuple:An bool identifying if the hidden state and cell state is tuple. Default to true.
- activation:An string identifying the type of activation function in the op. Default to "tanh". Only tanh is currently supported .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- input1 h: float16
- input2 c: float16,float32
- input3 w: float16
- input4 b: float16,float32
- input5 mask: uint8
- output0 ct: float16,float32
- output1 ht: float16
- output2 it: float16,float32
- output3 jt: float16,float32
- output4 ft: float16,float32
- output5 ot: float16,float32
- output6 tanhct: float16,float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
