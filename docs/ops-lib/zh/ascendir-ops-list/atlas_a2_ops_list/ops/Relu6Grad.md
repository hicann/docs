# Relu6Grad

```c
REG_OP(Relu6Grad)
    .INPUT(gradients, TensorType::RealNumberType())
    .INPUT(features, TensorType::RealNumberType())
    .OUTPUT(backprops, TensorType::RealNumberType())
    .OP_END_FACTORY_REG(Relu6Grad)
```

## Brief

Computes rectified linear 6 gradients for a Relu6 operation.
    backprops = gradients * (features > 0) * (features < 6) .

## Inputs

- gradients: A ND Tensor of type TensorType::RealNumberType. The backpropagated
gradients to the corresponding Relu6 operation.
- features: A ND Tensor with the same type as gradients.The features passed
as input to the corresponding Relu6 operation, or its output;
using either one produces the same result.  

## Outputs

backprops: A Tensor of type RealNumberType . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 gradients: bfloat16,float16,float32
- input1 features: bfloat16,float16,float32
- output0 backprops: bfloat16,float16,float32
### AI CPU
- input0 gradients: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 features: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 backprops: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator Relu6Grad.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
