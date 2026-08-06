# ReluGradV2

```c
REG_OP(ReluGradV2)
    .INPUT(gradients, TensorType::RealNumberType())
    .INPUT(mask, TensorType({DT_UINT8, DT_UINT1}))
    .OUTPUT(backprops, TensorType::RealNumberType())
    .OP_END_FACTORY_REG(ReluGradV2)
```

## Brief

Computes rectified linear gradients for a ReLU operation.

## Inputs

Two inputs, including:
- gradients: A tensor of input gradient. Indicates the gradient of backpropagation. Supported type: TensorType::RealNumberType().
In Ascend 950 AI Processor, support ND format. Others support 5D, format must be NC1HWC0.
- mask: A tensor of input mask. Indicates the positive output. Must be the following types: uint8, uint1.
In Ascend 950 AI Processor, support ND format. Others support 5D, format must be NC1HWC0.

## Outputs

backprops: A tensor of ouput. Indicates the backpropagation result.
When gradient is greater than 0, backprops is the value of gradient.
When the value of gradient is less than or equal to 0, the value of backprops is 0.
Must have the same type, format and shape as "gradients". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 gradients: bfloat16,float16,float32,int8,int32,uint8
- input1 mask: uint1
- output0 backprops: bfloat16,float16,float32,int8,int32,uint8

## Attention Constraints

The corresponding Relu operator needs to be called before using this operator on the network. 


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
