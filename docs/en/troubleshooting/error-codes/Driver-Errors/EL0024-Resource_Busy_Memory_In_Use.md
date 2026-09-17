# EL0024 Resource\_Busy\_Memory\_In\_Use

## Symptom

The following is error format. The meanings of the placeholders %s in sequence are: API name, memory address.

```text
%s failed. Reason: The memory corresponding to address %s is still in use.
```

Error example:

```text
halMemFree failed. Reason: The memory corresponding to address 0x40000000000 is still in use.
```

## Possible Cause

The memory is still being used by other operations, such as memory copy, address conversion, memory mapping, or memory registration. Or, resources associated with the memory are not released.

## Solution

Before releasing the memory, ensure that all operations involving the memory have been finished and that resources related to the memory have been released. Then, try again.
