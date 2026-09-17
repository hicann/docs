# EL0018 Resource\_Error\_Insufficient\_Host\_Memory

## Symptom

The following is error format. The meanings of the placeholders %s in sequence are: API name, memory size, module name.

```text
%s failed. Failed to allocate %s host memory requested by the %s module.
```

Error example:

```text
halMemCreate failed. Failed to allocate 1024 bytes host memory requested by hdc module.
```

## Possible Cause

Allocation failed due to insufficient host memory.

## Solution

Ensure that the required memory is available. Take measures such as stopping unnecessary processes to free memory.
