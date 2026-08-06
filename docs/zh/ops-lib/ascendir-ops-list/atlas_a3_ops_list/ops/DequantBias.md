# DequantBias

```c
REG_OP(DequantBias)
    .INPUT(x, TensorType({DT_INT32}))
    .INPUT(weight_scale, TensorType({DT_FLOAT32, DT_BF16}))
    .OPTIONAL_INPUT(activate_scale, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(bias, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT32, DT_INT32}))
    .REQUIRED_ATTR(output_dtype, Int)
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16}))
    .OP_END_FACTORY_REG(DequantBias)
```

## Brief

DequantBias. 

## Inputs

- x: A 2D tensor. Input tensor representing the inverse quantization operation.
Supported format "ND". The shape is [M, N], and the data type supports int32.
- weight_scale: A 1D tensor. Indicates the weight of the multiplication on the N-dimensional input of the anti-quantization operation.
The shape is [N], and the length is consistent with the N-dimensional length of x. The data type supports float32, bfloat16.
- activate_scale: A 1D tensor. The data type supports float32.
Indicates the weight of the multiplication on the M dimension of the input for the anti-quantization operation.
The shape is [M], with a length consistent with the M dimension of x, and the data type supports float32.
Supported format "ND".
- bias: A 1D tensor. Indicates the weight of the addition on the N-dimensional input of the anti-quantization operation.
The shape is [N], with a length consistent with the N-dimensional length of x.
The data type supports float32, bfloat16, float16, int32. Supported format "ND".

## Outputs

y: A 2D tensor. The output tensor of the quantization operation.
The shape is [M, N], and the data type supports float16, bfloat16. Supported format "ND". 

## Attributes

output_dtype: An int attr. Indicates the data type of the output out. The value is [1, 27].
A value of 1 indicates that the output type is float16, and a value of 27 indicates that the output type is bfloat16.
When the weight_scale data type is float32, this parameter is set to 1; when the weight_scale data type is bfloat16,
this parameter is set to 27.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: int32
- input1 weight_scale: bfloat16,float32
- input2 activate_scale: float32
- input3 bias: bfloat16,float16,float32,int32
- output0 y: bfloat16,float16


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
