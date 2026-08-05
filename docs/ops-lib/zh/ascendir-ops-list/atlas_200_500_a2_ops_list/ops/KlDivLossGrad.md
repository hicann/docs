# KlDivLossGrad

```c
REG_OP(KlDivLossGrad)
    .INPUT(grad, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(input, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(target, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(reduction, String, "mean")
    .ATTR(log_target, Bool, false)
    .OP_END_FACTORY_REG(KlDivLossGrad)
```

## Brief

Computes Kl_div_loss_grad or Kl_div_loss_backward. 

## Inputs

Three inputs, including:
- grad: A tensor. Must be one of the following types: float16, float32, bfloat16.
 Shape needs to satisfy the broadcast relationship with input.
 Required.
- input: A tensor. Has the same type as "grad". Required.
- target: A tensor. Has the same type as "grad". Required.
 Shape needs to satisfy the broadcast relationship with input. 

## Outputs

y: A tensor. Has the same type as "grad".
Has the same shape as "input"  

## Attributes

- reduction: An optional attribute of type String. Defaults to "mean".
 Supports "none" | "mean" | "sum" | "batchmean".  
 'none' means no reduction should be applied.  
 'mean' means the total output will be divided by the number of elements in the output.  
 'sum' means the output will be summed. 
 'batchmean' means the total output will be divided by the number of batches. 
- log_target: An optional attribute of type Bool. Defaults to false.

## Third-party framework compatibility

Compatible with the Pytorch operator KlDivLossGrad.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
