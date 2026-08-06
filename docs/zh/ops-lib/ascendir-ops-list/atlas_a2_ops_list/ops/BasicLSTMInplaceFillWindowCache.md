# BasicLSTMInplaceFillWindowCache

```c
REG_OP(BasicLSTMInplaceFillWindowCache)
    .INPUT(x, TensorType({DT_FLOAT16}))
    .INPUT(w, TensorType({DT_INT8}))
    .INPUT(r, TensorType({DT_INT8}))
    .INPUT(h, TensorType({DT_FLOAT16}))
    .INPUT(c, TensorType({DT_FLOAT16}))
    .OPTIONAL_INPUT(b, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(sequence_lens, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(clean_cache, TensorType({DT_INT32}))
    .INPUT(deq_scale, TensorType({DT_UINT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16}))
    .OUTPUT(h, TensorType({DT_FLOAT16}))
    .OUTPUT(c, TensorType({DT_FLOAT16}))
    .REQUIRED_ATTR(hidden_size, Int)
    .ATTR(activation_alpha, ListFloat, {})
    .ATTR(activation_beta, ListFloat, {})
    .ATTR(activations, ListString, {})
    .ATTR(clip, Float, -1.0)
    .ATTR(direction, String, "forward")
    .ATTR(input_forget, Int, 0)
    .ATTR(quant_scale_x, Float, 0.0)
    .ATTR(quant_offset_x, Float, 0.0)
    .ATTR(quant_sqrt_mode_x, Bool, false)
    .ATTR(quant_scale_h, Float, 0.0)
    .ATTR(quant_offset_h, Float, 0.0)
    .ATTR(quant_sqrt_mode_h, Bool, false)
    .ATTR(quant_dtype, Int, DT_INT8)
    .OP_END_FACTORY_REG(BasicLSTMInplaceFillWindowCache)
```

## Brief

BasicLSTMInplaceFillWindowCache calculation.

## Inputs

eight inputs: 
- x:Each time step is a 3D Tensor. Must be one of the following types: float16.
- w:Each direction is a 3D Tensor. Must be one of the following types: int8.
- r:Each direction is a 3D Tensor. Must be one of the following types: int8.
- h:Each direction is a 3D Tensor. Must be one of the following types: float16.
- c:Each direction is a 3D Tensor. Must be one of the following types: float16.
- b:An optional input. Each direction is a 2D Tensor. Must be one of the following types: int32.
- sequence_lens:An optional input. A 1D Tensor. Must be one of the following types: int32.
- clean_cache:An optional input. A 1D Tensor. Must be one of the following types: int32. clean_cache=None behaves the same as clean_cache=2.
- deq_scale:A 1D Tensor. Must be one of the following types: uint64.

## Outputs

three outputs: 
- y:First dimension is time step, second dimension is direction, others is a 4D Tensor. Must be one of the following types: float16.
- y_h:Each direction is a 3D Tensor. Must be one of the following types: float16.
- y_c:Each direction is a 3D Tensor. Must be one of the following types: float16.

## Attributes

- hidden_size:Number of neurons in the hidden layer. Requied. Reserved.
- activation_alpha: Optional scaling values used by some activation functions. Empty is currently supported.
- activation_beta: Optional scaling values used by some activation functions. Empty is currently supported.
- activations: A list of strings of activation functions. Empty is currently supported.
- clip:An float identifying the cell clip in the op. Default to -1.
- direction: Specify if the RNN is forward, reverse, or bidirectional. Must be forward(default).
- input_forget:Couple the input and forget gates if 1. Reserved.
- quant_scale_x: A float identifying the quant_scale of x_tensor. Default to -0.0.
- quant_offset_x:A float identifying the quant_offset of x_tensor. Default to -0.0.
- quant_sqrt_mode_x:A sqrt_mode of x_tensor. Default to False.
- quant_scale_h:A float identifying the quant_scale of h_tensor. Default to -0.0.
- quant_offset_h:A float identifying the quant_offset of h_tensor. Default to -0.0.
- quant_sqrt_mode_h:A sqrt_mode of h_tensor. Default to False.
- quant_dtype:An Int number identifying the dtype of quant. Default to 2(DT_INT8).


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
