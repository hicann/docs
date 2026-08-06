# ProdForceSeA

```c
REG_OP(ProdForceSeA)
    .INPUT(net_deriv, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(in_deriv, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(nlist, TensorType({DT_INT32}))
    .INPUT(natoms, TensorType({DT_INT32}))
    .OUTPUT(atom_force, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .REQUIRED_ATTR(n_a_sel, Int)
    .REQUIRED_ATTR(n_r_sel, Int)
    .OP_END_FACTORY_REG(ProdForceSeA)
```

## Brief

ProdForceSeA computes atomic forces for DeepPot-SE (Angular) model.
      force[k][i][d] = -sum(net_deriv * in_deriv) for center atom,
      force[k][j][d] += sum(net_deriv * in_deriv) for neighbor atoms.

## Inputs

Four inputs, including:
- net_deriv: A 2D Tensor. Must be one of the following types: float16, float32, float64.
- in_deriv: A 2D Tensor. Must be one of the following types: float16, float32, float64.
- nlist: A 2D Tensor. Must be int32. Neighbor list, -1 for virtual neighbors.
- natoms: A 1D Tensor. Must be int32. natoms[0]=nloc, natoms[1]=nall.

## Outputs

atom_force: A 3D Tensor. Must be one of the following types: float16, float32, float64.

## Attributes

- n_a_sel: Int. Angular neighbor selection count, required.
- n_r_sel: Int. Radial neighbor selection count, required.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 net_deriv: float32
- input1 in_deriv: float32
- input2 nlist: int32
- input3 natoms: int32
- output0 atom_force: float32

## Third-party framework compatibility

Compatible with the DeepMD-kit operator ProdForceSeA.


---

[Back to Operator Specifications (Ascend950)](../README.md)
