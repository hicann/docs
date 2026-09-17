# EL0023 Resource\_Error

## Symptom

The following is error format. The meanings of the placeholders %s in sequence are: API name, error cause.

```text
%s failed. Reason: %s.
```

Error example:

```text
halMemSetAccess failed. Reason: UB memory address conversion failed because the UB Decoder configuration is abnormal.
```

## Solution

Check whether the LingQu UBM package is correctly installed and use gmsysview in the control node to check whether the UB Decoder is correctly configured.
