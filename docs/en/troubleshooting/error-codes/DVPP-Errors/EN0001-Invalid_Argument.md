# EN0001 Invalid\_Argument

## Symptom

The following is error format. The meanings of the placeholders %s in sequence are: API name, parameter value, parameter name, error cause.

```text
%s failed, value %s for parameter %s is invalid. Reason: %s.
```

Error example 1:

```text
VdecWrapperHdc::hi_mpi_vdec_send_stream failed, Value -2 for parameter milli_sec is invalid. Reason: milli_sec must only be -1, 0 or positive number.
```

Error example 2:

```text
SysManager::hi_mpi_dvpp_malloc failed, Value -1 for parameter size is invalid. Reason: size must be greater than 0.
```

## Solution

Please enter the correct parameter value as prompted in the Reason.
