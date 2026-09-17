# EN0012 Resource\_Error\_Insufficient\_Device\_Memory

## Symptom

The following is error format. The placeholder %s indicates the memory size.

```text
Failed to allocate %s device memory for DVPP.
```

Error example:

```text
Failed to allocate 128 bytes device memory for DVPP.
```

## Possible Cause

Allocation failed due to insufficient NPU memory.

## Solution

Stop unnecessary processes and ensure that the required memory is available.
