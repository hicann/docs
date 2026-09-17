# EN0010 Resource\_Error\_Insufficient\_Host\_Memory

## Symptom

The following is error format. The placeholder %s indicates the memory size.

```text
Failed to allocate %s host memory for DVPP.
```

Error example:

```text
Failed to allocate 128 bytes host memory for DVPP.
```

## Possible Cause

Allocation failed due to insufficient host memory.

## Solution

Ensure that the required memory is available. Take measures such as stopping unnecessary processed to free memory.
