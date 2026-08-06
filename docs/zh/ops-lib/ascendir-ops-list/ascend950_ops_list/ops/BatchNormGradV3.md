# BatchNormGradV3

```c
REG_OP(BatchNormGradV3)
    .INPUT(dy, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(weight, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(running_mean, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(running_var, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(save_mean, TensorType({DT_FLOAT}))
    .INPUT(save_rstd, TensorType({DT_FLOAT}))
    .OUTPUT(dx, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(dweight, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(dbias, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(is_training, Bool, true)
    .ATTR(epsilon, Float, 1e-5)
    .OP_END_FACTORY_REG(BatchNormGradV3)
```

## Brief

Computes the gradients for Batch Normalization.
This operation computes the gradients of the input tensor, weight, and bias during the backpropagation step
of batch normalization, using the saved mean and inverse standard deviation from the forward pass. It is typically
used in the context of training deep learning models with batch normalization layers.

## Inputs

- dy: Gradient of the loss w.r.t the output, a tensor of type float16/bfloat16/float32. Supported formats: NCHW, NHWC, NDHWC, NCDHW.
- x: Input feature map, a tensor of type float16/bfloat16/float32. Supported formats: NCHW, NHWC, NDHWC, NCDHW.
- weight: Scale parameter, a 1D tensor of type float16/bfloat16/float32. Supported formats: ND.
- running_mean: Running mean, a 1D tensor of type float16/bfloat16/float32. Supported formats: ND.
- running_var: Running variance, a 1D tensor of type float16/bfloat16/float32. Supported formats: ND.
- save_mean: Saved mean from the forward pass, a 1D tensor of type float32. Supported formats: ND.
- save_rstd: Saved inverse standard deviation from the forward pass, a 1D tensor of type float32. Supported formats: ND.

## Outputs

- dx: Gradient of the loss w.r.t the input, a tensor of type float16/bfloat16/float32. Supported formats: NCHW, NHWC, NDHWC, NCDHW.
- dweight: Gradient of the loss w.r.t the scale parameter, a 1D tensor of type float16/bfloat16/float32. Supported formats: ND.
When is_training is false, this output is meaningless.
- dbias: Gradient of the loss w.r.t the bias, a 1D tensor of type float16/bfloat16/float32. Supported formats: ND.
When is_training is false, this output is meaningless.

## Attributes

- is_training: (Optional) A bool value. Whether the operation is in training mode. Default: true
- epsilon: (Optional) A small float32 value added for numerical stability. Default: 1e-5

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: bfloat16,float16,float32
- input1 x: bfloat16,float16,float32
- input2 weight: bfloat16,float16,float32
- input3 running_mean: bfloat16,float16,float32
- input4 running_var: bfloat16,float16,float32
- input5 save_mean: float32
- input6 save_rstd: float32
- output0 dx: bfloat16,float16,float32
- output1 dweight: bfloat16,float16,float32
- output2 dbias: bfloat16,float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
