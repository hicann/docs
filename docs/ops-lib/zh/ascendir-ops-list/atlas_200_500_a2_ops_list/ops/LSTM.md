# LSTM

```c
REG_OP(LSTM)
    .INPUT(x, TensorType({DT_FLOAT16}))
    .INPUT(cont, TensorType({DT_FLOAT32,DT_FLOAT16}))
    .INPUT(w_x, TensorType({DT_FLOAT16}))
    .INPUT(bias, TensorType({DT_FLOAT16,DT_FLOAT32,DT_INT16,DT_INT32}))
    .INPUT(w_h, TensorType({DT_FLOAT16}))
    .OPTIONAL_INPUT(x_static, TensorType({DT_FLOAT16}))
    .OPTIONAL_INPUT(h_0, TensorType({DT_FLOAT16,DT_FLOAT32}))
    .OPTIONAL_INPUT(c_0, TensorType({DT_FLOAT16,DT_FLOAT32}))
    .OPTIONAL_INPUT(w_x_static, TensorType({DT_FLOAT16}))
    .OUTPUT(h, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(h_t, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(c_t, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(num_output, Int, 0)
    .ATTR(expose_hidden, Bool, false)
    .OP_END_FACTORY_REG(LSTM)
```

## Brief

Applies a multi-layer long short-term memory (LSTM) RNN to an input sequence . 

## Inputs

- x: A Tensor dtype of float16.
- cont: A Tensor dtype of float16, float32.
- w_x: A Tensor dtype of float16.
- bias: A Tensor dtype of int16, int32, float16, float32.
- w_h: A Tensor dtype of float16.
- x_static: A optinal Tensor dtype of float16.
- h_0: A optinal Tensor dtype of float16, float32.
- c_0: A optinal Tensor dtype of float16, float32.
- w_x_static: A optinal Tensor dtype of float16 .

## Outputs

- h: A Tensor dtype of float16, float32.
- h_t: A optinal Tensor dtype of float16, float32. The hidden state at time t.
- c_t: A optinal Tensor dtype of float16, float32. The cell state at time t .

## Attributes

- num_output: A Scalar of output size dtype of int.
- expose_hidden: A Scalar(bool) of features hidden .

## Third-party framework compatibility

Compatible with the Caffe operator LSTM.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
