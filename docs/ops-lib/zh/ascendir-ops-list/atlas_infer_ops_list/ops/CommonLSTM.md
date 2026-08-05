# CommonLSTM

```c
REG_OP(CommonLSTM)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(w, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(r, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(b, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(sequence_lens, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(initial_h, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(initial_c, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(p, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y_h, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y_c, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(activation_alpha, ListFloat, {})
    .ATTR(activation_beta, ListFloat, {})
    .ATTR(activations, ListString, {})
    .ATTR(clip, Float, -1.0)
    .ATTR(direction, String, "forward")
    .REQUIRED_ATTR(hidden_size, Int)
    .ATTR(input_forget, Int, 0)
    .OP_END_FACTORY_REG(CommonLSTM)
```

## Brief

CommonLSTM calculation.

## Inputs

eight inputs: 
- x:Each time step is a 4D Tensor. Must be one of the following types: float16, float32.
- w:Each direction is a 4D Tensor. Must be one of the following types: float16, float32.
- r:Each direction is a 4D Tensor. Must be one of the following types: float16, float32.
- b:An optional input. Each direction is a 1D Tensor. Must be one of the following types: float16, float32. The
format must be ND.
- sequence_lens:An optional input. A 1D Tensor.Must be one of the following types: int32. The format must be
ND.
- initial_h:An optional input. Each direction is a 4D Tensor. Must be one of the following types: float16,
float32.
- initial_c:An optional input. Each direction is a 4D Tensor. Must be one of the following types: float16,
float32.
- p:An optional input. Each direction is a 1D Tensor.Must be one of the following types: float16, float32. The
format must be ND.

## Outputs

three outputs: 
- y:First dimension is time step, second dimension is direction, others is a 4D Tensor. Must be one of the
following types: float16, float32.
- y_h:Each direction is a 4D Tensor. Must be one of the following types: float16, float32.
- y_c:Each direction is a 4D Tensor. Must be one of the following types: float16, float32.

## Attributes

- activation_alpha:Optional scaling values used by some activation functions. Empty is currently supported.
- activation_beta:Optional scaling values used by some activation functions. Empty is currently supported.
- activations:The list of activation functions. Empty is currently supported.
- clip:An float identifying the cell clip in the op. Default to -1.
- direction:Specify if the RNN is forward, reverse, or bidirectional. Must be one of forward(default), reverse,
or bidirectional.
- hidden_size:Number of neurons in the hidden layer. Reserved.
- input_forget:Couple the input and forget gates if 1. Reserved.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
