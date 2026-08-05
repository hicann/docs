# Lerp

```c
REG_OP(Lerp)
    .INPUT(start, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(end, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(weight, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OP_END_FACTORY_REG(Lerp)
```

## Brief

Calculate the lerp function. 

## Inputs

Three inputs, including:
- start: A ND tensor. Must be one of the following types:
    float16, float32, bfloat16. 
The shape of start, end and weight should satisfy the broadcast relationship. 
- end: A ND tensor. Must be one of the following types:
    float16, float32, bfloat16. 
- weight: A ND tensor. Must be one of the following types:
    float16, float32, bfloat16. 

## Outputs

y: A ND tensor with the same dtype of start's. 
The shape of 'y' is same as the shape of the tensor 
whose shape is generated after 'start', 'end', and 'weight' broadcast opratioan.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 start: float16,float32
- input1 end: float16,float32
- input2 weight: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the PyTorch operator Lerp. 


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
