# ArgMaxWithK

```c
REG_OP(ArgMaxWithK)
     .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
     .OUTPUT(indices, TensorType({DT_INT32, DT_FLOAT, DT_FLOAT16}))
     .OUTPUT(values, TensorType({DT_FLOAT, DT_FLOAT16}))
     .ATTR(axis, Int, 10000)
     .ATTR(out_max_val, Bool, false)
     .ATTR(topk, Int, 1)
     .OP_END_FACTORY_REG(ArgMaxWithK)
```

## Brief

Returns the index number corresponding to the maximum value entered. 

## Inputs

x: A tensor. Must be one of the following types: float16, float32. 

## Outputs

- indices: A tensor of type float16, float32, int32. The index of the maximum value of the output.
- values: A tensor of type float16, float32.Output tensor, including maximum index or maximum value.

## Attributes

- axis: An optional int. Specify the axis to be cut at the input tensor. If this parameter is not provided, find the topk for each batch. Defaults to 10000
- out_max_val: An optional bool. Whether to output the maximum value. If it is True, the maximum value and index are output, otherwise only the index is output.
Defaults to False
- topk: An optional int. It means the number of top tok in each axis (the value is greater than or equal to 1), and the value range must be in [1,x.shape(axis)].
Defaults to 1

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: float16,float32
- output0 indices: float16,float32,int32
- output1 values: float16,float32

## Third-party framework compatibility

Compatible with the Caffe operator ArgMax.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
