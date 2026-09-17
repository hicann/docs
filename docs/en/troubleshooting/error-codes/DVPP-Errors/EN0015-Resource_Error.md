# EN0015 Resource\_Error

## Symptom

The following is error format. The meanings of the placeholders %s in sequence are: module name, API name.

```text
The %s has not been initialized. Call %s to initialize the resource first.
```

Error example:

```text
The vpc resource has not been initialized. Call hi_mpi_sys_init to initialize the resource first.
```

## Solution

Please adjust the code as prompted in the error message.
