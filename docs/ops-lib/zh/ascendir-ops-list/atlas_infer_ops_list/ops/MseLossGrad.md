# MseLossGrad

```c
REG_OP(MseLossGrad)
    .INPUT(predict, TensorType({DT_FLOAT32, DT_FLOAT16, DT_BF16}))
    .INPUT(label, TensorType({DT_FLOAT32, DT_FLOAT16, DT_BF16}))
    .INPUT(dout, TensorType({DT_FLOAT32, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT32, DT_FLOAT16, DT_BF16}))
    .ATTR(reduction, String, "mean")
    .OP_END_FACTORY_REG(MseLossGrad)
```

## Brief

Computes gradients of mse loss.

## Inputs

- predict: An ND tensor of type float16, float32 or bfloat16.
- label: An ND tensor of type float16, float32 or bfloat16.
- dout: An ND tensor of type float16, float32 or bfloat16.

## Outputs

y: An ND tensor tensor with the same shape and type as "predict". 

## Attributes

reduction: An optional string.Defaults to "mean". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 predict: float16,float32
- input1 label: float16,float32
- input2 dout: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator MseLossGrad.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
