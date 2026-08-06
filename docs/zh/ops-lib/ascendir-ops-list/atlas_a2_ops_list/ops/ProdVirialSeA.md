# ProdVirialSeA

```c
REG_OP(ProdVirialSeA)
    .INPUT(net_deriv, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(in_deriv, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(rij, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(nlist, TensorType({DT_INT32}))
    .INPUT(natoms, TensorType({DT_INT32}))
    .OUTPUT(virial, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(atom_virial, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .REQUIRED_ATTR(n_a_sel, Int)
    .REQUIRED_ATTR(n_r_sel, Int)
    .OP_END_FACTORY_REG(ProdVirialSeA)
```

## Brief

Calculate ProdVirialSeA.

## Inputs

Five inputs, including:
- net_deriv: A 2D Tensor with shape [nframes, nloc * nnei * 4]. Must be one of the following types: float16,
float32, float64.
- in_deriv: A 2D Tensor with shape [nframes, nloc * nnei * 4 * 3]. Must be one of the following types: float16,
float32, float64.
- rij: A 2D Tensor with shape [nframes, nloc * nnei * 3]. Must be one of the following types: float16, float32,
float64.
- nlist: A 2D Tensor with shape [nframes, nloc * nnei]. dtype is int32.
- natoms: A 1D Tensor with shape [2 + ntypes,]. dtype is int32.

## Outputs

Two outputs, including:
- virial: A 2D Tensor with shape [nframes, 9]. Must be one of the following types: float16, float32,
float64.
- atom_virial: A 2D Tensor with shape [nframes, nall * 9]. Must be one of the following types: float16,
float32, float64. 

## Attributes

Two attributes, including:
- n_a_sel: A required int32. The value must be greater than or equal to 0.
- n_r_sel: A required int32. The value must be greater than or equal to 0. Additionally,
the sum of n_a_sel and n_r_sel must be greater than 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 net_deriv: float32
- input1 in_deriv: float32
- input2 rij: float32
- input3 nlist: int32
- input4 natoms: int32
- output0 virial: float32
- output1 atom_virial: float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
