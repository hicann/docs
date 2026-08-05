# GNTrainingUpdate

```c
REG_OP(GNTrainingUpdate)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(sum, TensorType({DT_FLOAT}))
    .INPUT(square_sum, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(scale, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(offset, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(mean, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(variance, TensorType({DT_FLOAT}))
    .ATTR(num_groups, Int, 2)
    .ATTR(epsilon, Float, 0.0001)
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(batch_mean, TensorType({DT_FLOAT}))
    .OUTPUT(batch_variance, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(GNTrainingUpdate)
```

## Brief

Performs update group normalization .

## Inputs

Seven inputs, including: (NCHW NHWC supported)
- x: A Tensor of type float16 or float32.
- sum: A tensor of type float32,
shape is [N, G, 1, 1, 1] for NCHW, [N, 1, 1, G, 1] for NHWC
for the output of operator GNTrainingReduce.
- square_sum: A tensor of type float32,
shape is [N, G, 1, 1, 1] for NCHW, [N, 1, 1, G, 1] for NHWC
for the output of operator GNTrainingReduce.
- scale: A optional tensor of type float32,
shape is [1, G, 1, 1, 1] for NCHW, [1, 1, 1, G, 1] for NHWC
is for the scaling gamma.
- offset: A optional tensor of type float32,
shape is [1, G, 1, 1, 1] for NCHW, [1, 1, 1, G, 1] for NHWC
for the scaling beta.
- mean: A optional tensor of type float32,
shape is [N, G, 1, 1, 1] for NCHW, [N, 1, 1, G, 1] for NHWC
for the updated mean.
- variance: A optional tensor of type float32,
shape is [N, G, 1, 1, 1] for NCHW, [N, 1, 1, G, 1] for NHWC
for the updated variance.

## Outputs

Three outputs, including:
- y: A Tensor of type float16 or float32, for normalized "x".
- batch_mean: A Tensor of type float32, for the updated mean.
- batch_variance: A Tensor of type float32, for the updated variance .

## Attributes

- epsilon: A optional float32, specifying the small value added to variance to avoid dividing by zero, default to
0.0001.
- num_groups: a optional int, specifying the num of groups. required, same to GNTrainingReduce, default to 2.

## Attention Constraints

- This operator is a InstanceNorm fusion operator for updating the moving averages for training.
This operator is used in conjunction with GNTrainingUpdate.
- For Atlas 200/300/500 Inference Product, the result accuracy fails to reach 1/1000 due to the square root
instruction.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
