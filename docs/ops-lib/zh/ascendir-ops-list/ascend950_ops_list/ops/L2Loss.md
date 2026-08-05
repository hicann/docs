# L2Loss

```c
REG_OP(L2Loss)
    .INPUT(x, TensorType({FloatingDataType, DT_BF16}))
    .OUTPUT(y, TensorType({FloatingDataType, DT_BF16}))
    .OP_END_FACTORY_REG(L2Loss)
```

## Brief

Computes half the L2 norm of a tensor without the sqrt .

## Inputs

x: A Tensor. TensorType::FloatingDataType() or bfloat16. 

## Outputs

y: A Tensor. Has the same type as "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 x: double,float16,float32
- output0 y: double,float16,float32

## Attention Constraints

if performances better in format NZ, please close
"MatmulTransdataFusionPass" in fusion configuration. 

## Third-party framework compatibility

Compatible with the TensorFlow operator L2Loss.


---

[Back to Operator Specifications (Ascend950)](../README.md)
