# SmoothL1LossGrad

```c
REG_OP(SmoothL1LossGrad)
    .INPUT(predict, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(label, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(dout, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(gradient, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(sigma, Float, 1.0)
    .OP_END_FACTORY_REG(SmoothL1LossGrad)
```

## Brief

Performs the backpropagation of SmoothL1Loss for training scenarios .

## Inputs

Three inputs, including:
- predict: A multi-dimensional Tensor of type float16 or float32 or bfloat16, specifying the predictive value.
- label: A multi-dimensional Tensor of float16 or float32 or bfloat16, specifying the target value.
- dout: A multi-dimensional Tensor of float16 or float32 or bfloat16,
specifying the gradient transferred from the upper layer . 

## Outputs

gradient: Return gradient. Has the same dimensions and type as "predict" . 

## Attributes

sigma: Must be a floating point number. Defaults to "1.0" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 predict: float16,float32
- input1 label: float16,float32
- input2 dout: float16,float32
- output0 gradient: float16,float32

## Third-party framework compatibility

Compatible with the scenario where "reduction" is set to "none"of PyTorch operator SmoothL1LossGrad.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
