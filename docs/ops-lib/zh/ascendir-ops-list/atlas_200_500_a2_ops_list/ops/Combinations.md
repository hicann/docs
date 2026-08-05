# Combinations

```c
REG_OP(Combinations)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType::ALL())
    .ATTR(r, Int, 2)
    .ATTR(with_replacement, Bool, false)
    .OP_END_FACTORY_REG(Combinations)
```

## Brief

Compute combinations of length of the given tensor.

## Inputs

x:  A list of 1D Tensor objects.

## Outputs

y: A Tensor list with same type as "x" .

## Attributes

- r: An optional int indicates number of elements to combine. Defaults to 2.
- with_replacement: An optional bool indicates whether to allow duplication
in combination. Defaults to "False".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

@ Compatible with the Pytorch operator Combinations.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
