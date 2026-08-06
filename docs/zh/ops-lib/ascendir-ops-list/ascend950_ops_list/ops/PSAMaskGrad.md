# PSAMaskGrad

```c
REG_OP(PSAMaskGrad)
    .INPUT(y_grad, TensorType::BasicType())
    .OUTPUT(x_grad, TensorType::BasicType())
    .REQUIRED_ATTR(psa_type, Int)
    .REQUIRED_ATTR(num, Int)
    .REQUIRED_ATTR(h_feature, Int)
    .REQUIRED_ATTR(w_feature, Int)
    .REQUIRED_ATTR(h_mask, Int)
    .REQUIRED_ATTR(w_mask, Int)
    .REQUIRED_ATTR(half_h_mask, Int)
    .REQUIRED_ATTR(half_w_mask, Int)
    .OP_END_FACTORY_REG(PSAMaskGrad)
```

## Brief

Calculate the gradient of operator PSAMask 

## Inputs

y_grad: A Tensor of BasicType that indicates the passed gradient. 

## Outputs

x_grad: A Tensor of BasicType that indicates the calculated gradient. 

## Attributes

- psa_type: An Int value of 1 or 2 that indicates the method used to generate pixel-wise global attention map.
- num: An Int value that indicates the batch_size of input x.
- h_feature: An Int value that indicates the hight of input feature map.
- w_feature: An Int value that indicates the width of input feature map.
- h_mask: An Int value that indicates the hight of the over-completed map.
- w_mask: An Int value that indicates the width of the over-completed map.
- half_h_mask: An Int value that indicates half of the hight of input feature map.
- half_w_mask: An Int value that indicates half of the width of the over-completed map.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 y_grad: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 x_grad: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the mmcv operator PSAMask.


---

[Back to Operator Specifications (Ascend950)](../README.md)
