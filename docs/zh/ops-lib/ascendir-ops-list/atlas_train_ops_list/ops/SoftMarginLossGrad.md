# SoftMarginLossGrad

```c
REG_OP(SoftMarginLossGrad)
    .INPUT(predict, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(label, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(dout, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(gradient, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(reduction, String, "mean")
    .OP_END_FACTORY_REG(SoftMarginLossGrad)
```

## Brief

Computes the gradient of SoftMarginLossGrad. 

## Inputs

Three inputs, including:
- predict: A tensor. Must be one of the following types:
    float16, float32, bfloat16. 
- label: A tensor with same shape of predict. Must be one of the following types:
    float16, float32, bfloat16. 
- dout: A tensor with same shpae of predcit. Must be one of the following types:
    float16, float32, bfloat16. 

## Outputs

gradient: A Tensor with the same type of predict. 

## Attributes

reduction: An optional string. Specifies the reduction to apply to the output:
    'none' | 'mean' | 'sum'. Default: 'mean'. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 predict: float16,float32
- input1 label: float16,float32
- input2 dout: float16,float32
- output0 gradient: float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator SoftMarginLoss Backward. 


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
