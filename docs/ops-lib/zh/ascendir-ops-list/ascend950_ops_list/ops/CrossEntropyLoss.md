# CrossEntropyLoss

```c
REG_OP(CrossEntropyLoss)
    .INPUT(input, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(target, TensorType({DT_INT64, DT_INT32}))
    .OPTIONAL_INPUT(weight, TensorType({DT_FLOAT}))
    .OUTPUT(loss, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(log_prob, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(zloss, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(lse_for_zloss, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(reduction, String, "mean")
    .ATTR(ignore_index, Int, -100)
    .ATTR(label_smoothing, Float, 0.0)
    .ATTR(lse_square_scale_for_zloss, Float, 0.0)
    .ATTR(return_zloss, Bool, false)
    .OP_END_FACTORY_REG(CrossEntropyLoss)
```

## Brief

This criterion computes the cross entropy loss between input logits and target.

## Inputs

Three inputs, including:
- input: A ND tensor of type float16 or float32 or bfloat16,
Shape only support 2D [N, C], where N is batch size, C is class.
- target: A ND tensor of type int32 or int64, specifying the target value.
Shape is [N].
- weight: An optional ND tensor of type float32, specifying the weight value.
Shape is [C].

## Outputs

- loss: A ND tensor, Has the same dtype as input, Specifying the cross entropy loss,
When reduction is "none", shape is [N], When reduction is "sum" or "mean"， shape is [1].
- log_prob: A ND tensor, Has the same dtype and shape as input,  Specifying the result of logsoftmax.
- zloss: A ND tensor, Has the same dtype as input. shape is [N], Benchmarking Triton kernel implementation.
- lse_for_zloss: A ND tensor, Has the same dtype as input. shape is [N], Benchmarking Triton kernel implementation,
It is passed to the intermediate variable lse for reverse calculation.

## Attributes

- reduction: An optional string attr from ["none", "mean", "sum"],
 specifying the reduction type to be applied to the output. Defaults to "mean".
- ignore_index: An optional int attr. Specifies a target value that is ignored and does not contribute to the input gradient.
Note that ignore_index is only applicable when the target contains class indices. Defaults to "-100".
- label_smoothing: An optional float attr in [0.0, 1.0]. Specifies the amount of smoothing when computing the loss,
where 0.0 means no smoothing. The targets become a mixture of the original ground truth and a uniform distribution as
described in Rethinking the Inception Architecture for Computer Vision. Default: 0.0
- lse_square_scale_for_zloss: An optional float attr, Default: 0.0,
If is 0 and return_zloss is true, output all 0 tensors.
- return_zloss: An optional bool attr. Default: false, Control whether zloss outputs, when true zloss outputs,
when false zloss dose not output.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input: bfloat16,float16,float32
- input1 target: int32,int64
- input2 weight: float32
- output0 loss: bfloat16,float16,float32
- output1 log_prob: bfloat16,float16,float32
- output2 zloss: bfloat16,float16,float32
- output3 lse_for_zloss: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with PyTorch operator CrossEntropyLoss.


---

[Back to Operator Specifications (Ascend950)](../README.md)
