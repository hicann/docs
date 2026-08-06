# BatchNormV3

```c
REG_OP(BatchNormV3)
    .INPUT(x, "T1")
    .INPUT(weight, "T2")
    .INPUT(bias, "T2")
    .INPUT(running_mean, "T4")
    .INPUT(running_var, "T4")
    .OUTPUT(y, "T1")
    .OUTPUT(running_mean, "T4")
    .OUTPUT(running_var, "T4")
    .OUTPUT(save_mean, "T3")
    .OUTPUT(save_rstd, "T3")
    .ATTR(epsilon, Float, 1e-5f)
    .ATTR(momentum, Float, 0.1f)
    .ATTR(is_training, Bool, true)
    .DATATYPE(T1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DATATYPE(T2, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DATATYPE(T3, TensorType({DT_FLOAT}))
    .DATATYPE(T4, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OP_END_FACTORY_REG(BatchNormV3)
```

## Brief

Batch normalization (also known as batch norm) is a method used to
make training of artificial neural networks faster and more stable
through normalization of the layers' inputs by re-centering and re-scaling.

## Inputs

- x: A 4D/5D tensor of type float16/bfloat16/float32, with format NCHW/NHWC/NCDHW/NDHWC. describing the feature_map.
- weight: A 1D tensor with the shape is same as dim C of input x, support dtypes are related to input x dtype,
the following combinations are supported: [x: float16, weight: float16/float32], [x: bfloat16, weight: bfloat16/float32], [x: float32, weight: float32].
describing the weight.
- bias: A 1D tensor of the same dtype and shape as input weight, describing the bias.
- running_mean: A 1D tensor of type float16/bfloat16/float32, the shape is same as dim C of input x,
the following combinations are supported: [x: float16, running_mean: float16/float32], [x: bfloat16, running_mean: bfloat16/float32], [x: float32, running_mean: float32].
describing the running mean.
- running_var: A 1D tensor of the same dtype and shape as input running_mean, describing the running var.

## Outputs

- y: A 4D/5D tensor of the same dtype, shape and format as input x, describing the result.
- running_mean: A 1D tensor of the same dtype and shape as input running_mean, describing the running mean.
- running_var: A 1D tensor of the same dtype and shape as input running_var, describing the running var.
- save_mean: A 1D tensor of type float32, describing the mean of "x".
- save_rstd: A 1D tensor of type float32, describing the rstd of "x".

## Attributes

- epsilon: An optional float32, small value added to variance to avoid dividing by zero. Defaults to "1e-5".
- momentum: An optional float32, the value used for the running_mean and running_var computation. Defaults to "0.1".
- is_training: An optional bool, specifying if the operation is used for training or inference. Defaults to "True", now only support "True".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 weight: bfloat16,float16,float32
- input2 bias: bfloat16,float16,float32
- input3 running_mean: bfloat16,float16,float32
- input4 running_var: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
- output1 running_mean: bfloat16,float16,float32
- output2 running_var: bfloat16,float16,float32
- output3 save_mean: float32
- output4 save_rstd: float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
