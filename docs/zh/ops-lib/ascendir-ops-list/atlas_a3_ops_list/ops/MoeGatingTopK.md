# MoeGatingTopK

```c
REG_OP(MoeGatingTopK)
      .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
      .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
      .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
      .OUTPUT(expert_idx, TensorType({DT_INT32}))
      .OUTPUT(out, TensorType({DT_FLOAT}))
      .REQUIRED_ATTR(k, Int)
      .ATTR(k_group, Int, 1)
      .ATTR(group_count, Int, 1)
      .ATTR(group_select_mode, Int, 0)
      .ATTR(renorm, Int, 0)
      .ATTR(norm_type, Int, 0)
      .ATTR(out_flag, Bool, false)
      .ATTR(routed_scaling_factor, Float, 1.0)
      .ATTR(eps, Float, 1e-20)
      .OP_END_FACTORY_REG(MoeGatingTopK)
```

## Brief

Compute renorm(sigmoid) and topk for moe input.

## Inputs

- x: A 2D tensor which moe gating topk is applied, The shape is: (B*S, E), format supports ND, and data type must be float16, float or bfloat16. E(Expert num) can not be greater than 2048. E(Expert num) should be divisible by group_count.
- bias: A 1D tensor which is "bias" in moe gating topk. The shape is: (E), format supports ND, and data type must be the same as that of x.

## Outputs

- y: A 2D tensor which is the topk value result of moe gating topk, format supports ND, and data type must be the same as that of x.
The size of the non-1 axis must be the same as that of the corresponding axis of x.
The size of the -1 axis must be the same as that of k.
- expert_idx: A 2D tensor which is the topk index result of moe gating topk, format supports ND, and data type must be int. The shape must be the same as that of y.
- out: A 2D tensor which is the renorm result of moe gating topk, format supports ND, and data type must be float. The shape must be the same as that of x.

## Attributes

- k: A required attribute of type int. The value must greater than 0 and less than or equal to expert_num / group_count * k_group, idicating the topk value.
- k_group: An optional attribute of type int. It can not be less than 1, and can not be greater than group_count, indicating the topk group value. The default value is 1.
- group_count: An optional attribute of type int. It can not be less than 1, indicating the group count. The group_count * align_32(expert_num / group_count) can not be greater than 2048. The default value is 1.
- group_select_mode: An optional attribute of type int. 0 indicating that sort group by max values, 1 indicating that sort group by sum of top-2 values. The default value is 0.
- renorm: An optional attribute of type int. It can only be 0 now, indicating that norm firstly and then topk. The default value is 0.
- norm_type: An optional attribute of type int. 0 indicating that the softmax function is used, 1 indicating that the sigmoid function is used. The default value is 0.
- out_flag: An optional attribute of type bool. true indicating that has renorm output, false indicating that does not have renorm output. The default value is false.
- routed_scaling_factor: An optional attribute of type float, indicating the routed_scaling_factor coefficient in use. The default value is 1.0.
- eps: An optional attribute of type float, indicating the eps coefficient in use. The default value is 1e-20.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 bias: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
- output1 expert_idx: int32
- output2 out: float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
