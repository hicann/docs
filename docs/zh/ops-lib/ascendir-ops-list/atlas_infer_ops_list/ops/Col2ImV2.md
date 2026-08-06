# Col2ImV2

```c
REG_OP(Col2ImV2)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(output_size, TensorType({DT_INT32, DT_INT32}))
    .INPUT(kernel_size, TensorType({DT_INT32, DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16}))
    .REQUIRED_ATTR(dilation, ListInt)
    .REQUIRED_ATTR(padding, ListInt)
    .REQUIRED_ATTR(stride, ListInt)
    .OP_END_FACTORY_REG(Col2ImV2)
```

## Brief

Performs Col2ImV2 for each batch entry. 

## Inputs

- x: The Col Tensor. 3-D, shape: `(n, c*kernel_h*kernel_w, ho*wo)`.
where ho/wo is do = (output_d + 2*padding_d - dilation_d*(kernel_d - 1) - 1)//stride_d + 1.
- output_size: The img shape Tensor. 1-D, shape:`(2)`, value: (output_h, output_w).
- kernel_shape: The kernel size Tensor. 1-D , value: `(kernel_h, kernel_w)`, the shape of kernel in convolution.

## Outputs

y: The img Tensor. 4-D, shape: `(n, c, output_h, output_w)`. 

## Attributes

- dilation: ListInt, value: `(dilation_h, dilation_w)`, the dilation in convolution.
- padding: ListInt, value: `(padding_h, padding_w)`, the dilation in convolution.
- stride:  ListInt, value: `(stride_h, stride_w)`, the dilation in convolution.

## Third-party framework compatibility

Compatible with ONNX Col2Im operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
