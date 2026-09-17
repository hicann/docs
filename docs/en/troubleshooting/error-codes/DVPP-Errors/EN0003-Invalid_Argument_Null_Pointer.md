# EN0003 Invalid\_Argument\_Null\_Pointer

## Symptom

The following is error format. The meanings of the placeholders %s in sequence are: API name, parameter name.

```text
%s failed because %s cannot be a NULL pointer.
```

Error example:

```text
hi_mpi_vpc_crop_resize failed because source_pic cannot be a NULL pointer
```

## Solution

Try again with a correct pointer parameter.
