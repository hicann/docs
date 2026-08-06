# SPP

```c
REG_OP(SPP)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16}))
    .REQUIRED_ATTR(pyramid_height, Int)
    .ATTR(pool_method, Int, 0)
    .OP_END_FACTORY_REG(SPP)
```

## Brief

Spatial Pyramid Pooling, multi-level pooling.
Pooling out(n, sigma(c*2^i*2^i)) tensor, i in range[0,pyramid_height) . 

## Inputs

x: An NCHW tensor, support float16 or float32 type . 

## Outputs

y: A NCHW tensor, support float16 or float32 type . 

## Attributes

- pyramid_height: An required int32.
Multi-level pooling out from 2^0 to 2^(pyramid_height-1).
- pool_method: An optional int32, pooling method: 0-MAX, 1-AVE.
Defaults to "0" . 

## Attention Constraints

- pyramid_height: pyramid_heigjt should be in range [0,7).
Pooling paramter should statisfied with caffe pooling param(pad<kernel).
- feature_size:input feture map h and w should be [1, 510] .

## Third-party framework compatibility

Compatible with the Caffe operator SPP.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
