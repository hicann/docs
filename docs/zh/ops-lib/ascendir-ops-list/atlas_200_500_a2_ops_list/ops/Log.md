# Log

```c
REG_OP(Log)
    .INPUT(x, TensorType({DT_UINT8, DT_INT8, DT_INT16, DT_INT32, DT_INT64,
                          DT_FLOAT, DT_DOUBLE, DT_FLOAT16, DT_BF16,
                          DT_BOOL, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType::UnaryDataType())
    .ATTR(base, Float, -1.0)
    .ATTR(scale, Float, 1.0)
    .ATTR(shift, Float, 0.0)
    .OP_END_FACTORY_REG(Log)
```

## Brief

Computes logarithm of x element-wise.
y = log_base(shift + scale * x), with "base" > 0.

## Inputs

x: A ND Tensor of type uint8, int8, int16, int32, int64, float64,
   float16, bfloat16, float32, bool, complex128 or complex64. 

## Outputs

y: A tensor, when the input is of integer type, the y type is float32.
   Other case, y has same type as "x". 

## Attributes

- base: An optional float32, specifying the base "e". Defaults to "-1.0"
- scale: An optional float32, specifying the scale of input "x". Defaults
to "1.0"
- shift: An optional float32, specifying the shift. Defaults to "0.0"

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8
- output0 y: bfloat16,complex64,complex128,double,float16,float32

## Attention Constraints

- "base" is supposed to be greater than 0. Retaining the default
value "-1" sets "base" to "e".
- If the input value of operator Log is within the range (0, 0.01] or
[0.95, 1.05], the output accuracy is subject to change. 

## Third-party framework compatibility

- Compatible with the TensorFlow operator Log.
- Compatible with the Caffe operator Log.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
