# Too Many Registered Operators

## Symptom

During inference, errors are reported during model loading.

The log contains "ProgramRegister:Program register failed, program out of  _xxx_" and "Register binary failed". The following is an example of the log:

```text
[ERROR] RUNTIME(3093,rtstest_host):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [runtime.cc:967]3093 ProgramRegister:Program register failed, program out of 40000000
[ERROR] RUNTIME(3093,rtstest_host):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [logger.cc:23]3093 DevBinaryRegister:Register binary failed.
[ERROR] RUNTIME(3093,rtstest_host):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:127]3093 rtDevBinaryRegister:ErrCode=507032, desc=[program register num out of use], InnerCode=0x7090007
[ERROR] RUNTIME(3093,rtstest_host):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:26]3093 ReportFuncErrorReason:rtDevBinaryRegister execute failed, reason=[program register num out of use]
```

## Possible Cause

According to the log, the possible cause is that the number of registered resources such as operators in a process exceeds the allowed maximum.

## Solution

To rectify the fault, perform the following steps:

- Simplify the model or reduce the number of dynamic batch size profiles.
- If the model is too large, try to allocate one device per process.
- Do not repeatedly register the same operator in different models.
- Keep the number of registered operators within the specification.
