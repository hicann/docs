# LogSpaceD

```c
REG_OP(LogSpaceD)
    .INPUT(assist, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR (start, Float)
    .REQUIRED_ATTR (end, Float)
    .ATTR(steps, Int, 100)
    .ATTR(base, Float, 10.0)
    .ATTR(dtype, Int, 1)
    .OP_END_FACTORY_REG(LogSpaceD)
```

## Brief

Creates a one-dimensional tensor of size steps whose values are evenly spaced from start to
	end, inclusive, on a logarithmic scale with base base.

## Inputs

One inputs, including:
assist: A tensor. Must be one of the following types:
    float16, float32, bfloat16. 

## Outputs

y: A Tensor with the same type and shape of assist's. 

## Attributes

- start: An required float. Used to select the start.
- end: An required float. Used to select the end.
- steps: An optional int.Defaults to 100.
- base: An optional float.Defaults to 10.0.
- dtype: An optional int.Defaults to 1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 assist: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Attention Constraints

The operator will not be enhanced in the future.

## Third-party framework compatibility

Compatible with the Pytorch operator logspaced. 


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
