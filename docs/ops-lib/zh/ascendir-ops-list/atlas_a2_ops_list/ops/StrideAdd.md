# StrideAdd

```c
REG_OP(StrideAdd)
    .INPUT(x1, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .INPUT(x2, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .OUTPUT(y, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .REQUIRED_ATTR(x1_c1_offset, Int)
    .REQUIRED_ATTR(x2_c1_offset, Int)
    .REQUIRED_ATTR(c1_len, Int)
    .OP_END_FACTORY_REG(StrideAdd)
```

## Brief

Add the partial values of two tensors.

## Inputs

- x1: A ND Tensor in 5HD, and must be one of the following types: float16,
float32, bfloat16. 
- x2: A ND Tensor of the same dtype as "x1", and the same shape as "x1",
except for the C1 value. 

## Outputs

y:  A ND Tensor of the same dtype as "x1", and the same shape as "x1",
except for the C1 value. Record the result after adding. 

## Attributes

- x1_c1_offset: A required int. Offset value of C1 in "x1".
- x2_c1_offset: A required int. Offset value of C1 in "x2".
- c1_len: A required int. C1 len of "y". The value must be less than
the difference between C1 and offset in "x1" and "x2". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32
- input1 x2: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
