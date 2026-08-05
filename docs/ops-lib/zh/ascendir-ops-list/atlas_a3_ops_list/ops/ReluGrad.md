# ReluGrad

```c
REG_OP(ReluGrad)
    .INPUT(gradients, TensorType::RealNumberType())
    .INPUT(features, TensorType::RealNumberType())
    .OUTPUT(backprops, TensorType::RealNumberType())
    .OP_END_FACTORY_REG(ReluGrad)
```

## Brief

Computes rectified linear gradients for a ReLU operation.
 Gradients/features support broadcasting operations. 

## Inputs

Two inputs, including:
- gradients: A tensor of type RealNumberType. The backpropagated gradients to the corresponding Relu operation .
- features: A tensor of type RealNumberType. The features passed as input to the corresponding Relu operation .

## Outputs

backprops: A tensor of type RealNumberType . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 gradients: bfloat16,float16,float32,int8,int32,int64,uint8
- input1 features: bfloat16,float16,float32,int8,int32,int64,uint8
- output0 backprops: bfloat16,float16,float32,int8,int32,int64,uint8
### AI CPU
- input0 gradients: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 features: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 backprops: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

The corresponding Relu operator needs to be called before using this operator on the network . 

## Third-party framework compatibility

Compatible with TensorFlow operator ReluGrad.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
