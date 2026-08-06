# CommonGRU

```c
REG_OP(CommonGRU)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(w, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(r, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(b, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(sequence_lens, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(initial_h, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y_h, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(activation_alpha, ListFloat, {})
    .ATTR(activation_beta, ListFloat, {})
    .ATTR(activations, ListString, {})
    .ATTR(clip, Float, -1.0)
    .ATTR(direction, String, "forward")
    .REQUIRED_ATTR(hidden_size, Int)
    .ATTR(linear_before_reset, Int, 0)
    .OP_END_FACTORY_REG(CommonGRU)
```

## Brief

Common GRU calculation.

## Inputs

Eight inputs, including:
- x: The input sequences packed (and pontentially padded) into on 3D Tesnor(float16).
- w: The weight tensor for the gates is 3D Tensor(float16).
- r: The recurrence weight tesnor is 3D Tensor(float16).
- b: The bias tensor for the gates. The format must be ND
- sequence_lens: Optional tensor specifying lengths of sequences(int32). The format must be ND
- init_h: Optional initial value of the hidden(float16,float32).

## Outputs

- y: A Tensor that concats all the intermediate output values of the hidden(float16,float32).
- y_h: The last output value of the hidden(float16,float32).

## Attributes

- activation_alpha: Optional scaling values used by some activation functions.
- activation_beta: Optional scaling values used by some activation functions.
- activations: A list of 2 (or 4 if bidirectional) activation functions for update, reset, and hidden gates.
- clip: Cell clip threshold.
- direction: Specify if the RNN is forward, reverse, or bidirectional.
- hidden_size: Number of neurons in the hidden layer.
- linear_before_reset: When computing the output of the hidden gate, apply the linear transformation before
multiplying by the output of the reset gate. 


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
