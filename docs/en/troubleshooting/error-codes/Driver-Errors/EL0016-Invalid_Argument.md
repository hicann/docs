# EL0016 Invalid\_Argument

## Symptom

The following is error format. The meanings of the placeholders %s in sequence are: API name, parameter value, parameter name, error cause.

```text
%s failed. Value %s for parameter %s is invalid. Reason: %s.
```

Error example:

```text
MemMap failed. Value 10 for parameter cmd is invalid. Reason: The input address does not meet the 4 KB alignment requirement.
```

## Solution

Check the input parameter range of the function.
