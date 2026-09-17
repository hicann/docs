# EL0021 Not\_Supported

## Symptom

The following is error format. The meanings of the placeholders %s in sequence are: API name, error cause.

```text
The %s operation is not supported. Reason: %s.
```

Error example:

```text
The halGetPairPhyDevicesInfo operation is not supported. Reason: This API cannot be called in the split-scenario.
```

## Solution

Please adjust the code logic as prompted in the Reason.
