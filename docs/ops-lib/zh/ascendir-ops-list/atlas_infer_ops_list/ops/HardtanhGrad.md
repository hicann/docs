# HardtanhGrad

```c
REG_OP(HardtanhGrad)
    .INPUT(result, TensorType({ DT_BF16, DT_FLOAT16, DT_FLOAT }))
    .INPUT(grad, TensorType({ DT_B16, DT_FLOAT16, DT_FLOAT }))
    .OUTPUT(y, TensorType({ DT_BF16, DT_FLOAT16, DT_FLOAT }))
    .ATTR(min_val, Float, -1.0)
    .ATTR(max_val, Float, 1.0)
    .OP_END_FACTORY_REG(HardtanhGrad)
```

## Brief

PyTorch hardtanh_backward operator.

## Inputs

Two inputs, including:
- result: Support 1D ~ 8D. Minimum tensor of the linear region range,
datatype: bfloat16/float16/float32, format:ND/5HD.
- grad: Maximum tensor of the linear region range,
datatype: bfloat16/float16/float32, format:ND/5HD. 

## Outputs

One output, including:
y: Hardtanh_backward output tensor. Shape, datatype and format is the same as input result. 

## Attributes

Two attributes, including:
- min_val: Minimum value of the linear region range, datatype:float. Defaults to "-1.0".
- max_val: Maximum value of the linear region range, datatype:float. Defaults to "1.0".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 result: float16,float32
- input1 grad: float16,float32
- output0 y: float16,float32

## Attention Constraints

This operator only supports datatype: bfloat16/float16/float32, format: ND/5HD. 

## Third-party framework compatibility

Compatible with the PyTorch operator HardtanhGrad.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
