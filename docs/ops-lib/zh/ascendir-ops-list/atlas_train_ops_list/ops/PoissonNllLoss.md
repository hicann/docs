# PoissonNllLoss

```c
REG_OP(PoissonNllLoss)
    .INPUT(input_x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(target, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(loss, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(log_input, Bool, true)
    .ATTR(full, Bool, false)
    .ATTR(eps, Float, 1e-8f)
    .ATTR(reduction, String, "mean")
    .OP_END_FACTORY_REG(PoissonNllLoss)
```

## Brief

Calculate the PoissonNllLoss function.  
       target follow distribution of Poisson(input)loss(input,target) = input - target * log(input) + log(target!)

## Inputs

Two inputs, including:
- input_x: A tensor. Must be one of the following types: float16, float32.
- target: A tensor. Must be one of the following types: float16, float32.

## Outputs

loss: A Tensor has same element type as two inputs. 

## Attributes

four Attributes, including:
- log_input: An optional bool. Defaults to "True"
- full: An optional bool. Defaults to "False"
- eps: An optional float. Defaults to "1e-8"
- reduction: An optional string from "none", "mean",and "sum". Defaults to "mean"

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_x: float16,float32
- input1 target: float16,float32
- output0 loss: float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator PoissonNllLoss. 


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
