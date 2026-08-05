# ForeachNonFiniteCheckAndUnscale

```c
REG_OP(ForeachNonFiniteCheckAndUnscale)
    .DYNAMIC_INPUT(scaled_grads, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(found_inf, TensorType({DT_FLOAT}))
    .INPUT(inv_scale, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(ForeachNonFiniteCheckAndUnscale)
```

## Brief

Detect whether there is Inf or Nan in scaled_grads, set found_inf to 1 if it exists,
and do not operate on found_inf if it does not. Finally, multiply all values of scaled_grads by inv_scale

## Inputs

Three inputs:
- scaled_grads: A tensor list containing multiple tensors, format supports ND, can be float16, float, bfloat16,
maximum length of scaled_grads is 256,
meanwhile, this value is also an output, store the value multiplied by inv_scale.
- found_inf: A single-element float tensor to which 1.0 will be written if any scaled_grad contain infs/nans,
with only one element, format supports ND, must be float,
meanwhile, this value is also an output, indicating whether there is Inf or Nan present.
- inv_scale: A single-element float tensor by which scaled_grads are currently multiplied,
with only one element, format supports ND, must be float.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 scaled_grads: bfloat16,float16,float32
- input1 found_inf: float32
- input2 inv_scale: float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
