# Bucketize

```c
REG_OP(Bucketize)
    .INPUT(x, TensorType({DT_INT32, DT_INT64, DT_DOUBLE, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64}))
    .REQUIRED_ATTR(boundaries, ListFloat)
    .ATTR(dtype, Type, DT_INT32)
    .ATTR(right, Bool, true)
    .OP_END_FACTORY_REG(Bucketize)
```

## Brief

Bucketize 'input' based on 'boundaries'. For example, if the inputs
are boundaries = [0, 10, 100] input = [[-5, 10000] [150, 10] [5, 100]] then
the output will be output = [[0, 3] [3, 2] [1, 3]].

## Inputs

The dtype of input x  int float double. Inputs include:
x:Any shape of Tensor contains with int or float type. 

## Outputs

y:Same shape with 'input', each value of input replaced with bucket index. 

## Attributes

- boundaries:A sorted list of floats gives the boundary of the buckets.
- dtype: An optional int32 or int64. The output data type. Defaults to int32.
- right: An optional true or false. If true, return unpperbound index. If false return lowerbound index.
If the intput value falls outside the specified boundaries, return 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float32,int32,int64
- output0 y: int32,int64

## Third-party framework compatibility.

Compatible with tensorflow Bucketize operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
