# MoeInitRoutingV2Grad

```c
REG_OP(MoeInitRoutingV2Grad)
    .INPUT(grad_expanded_x, "T1")
    .INPUT(expanded_row_idx, "T2")
    .OUTPUT(grad_x, "T1")
    .DATATYPE(T1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DATATYPE(T2, TensorType({DT_INT32}))
    .REQUIRED_ATTR(top_k, Int)
    .ATTR(drop_pad_mode, Int, 0)
    .ATTR(active_num, Int, 0)
    .OP_END_FACTORY_REG(MoeInitRoutingV2Grad)
```

## Brief

compute init routing grad for moe input.

## Inputs

- grad_expanded_x: A 2D or 3D Tensor, tokens squences. Type is:BFloat16, Float16 or Float32. Format support ND.
- expanded_row_idx: A 1D Tensor, token indices in grad_expanded_x. Type is:Int32. Format support ND.

## Outputs

- grad_x: A 2D Tensor, reverse gradient result. Type is:BFloat16, Float16 or Float32，which is same as that of
            grad_expanded_x. axis 0 of grad_x should be same as the value that axis 0 of expanded_row_idx divide
            top_k, axis 1 of grad_x should be same as -1 axis of grad_expanded_x. Format support ND.

## Attributes

- top_k: Required parameter. Type is:Int32. The value must be greater than 0 and can be exactly divided by axis 0
           of expanded_row_idx.
- drop_pad_mode: Optional parameter, identify the dropless or drop/pad scenario. Type is:Int32. The value is
                   0 (dropless scenario) or 1 (drop/pad scenario).
- active_num: Optional parameter, identify activate scenario. Type is:Int32. The value 0 indicates a non-active
                scenario, and a value greater than 0 indicates an active scenario. In the active scenario, the size
                of axis 0 of grad_expanded_x must be equal to the value of active_num.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad_expanded_x: bfloat16,float16,float32
- input1 expanded_row_idx: int32
- output0 grad_x: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
