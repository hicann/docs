# VDEC Failure Due to Stream Size Verification Failure

## Symptom

The error code  **HI\_ERR\_VDEC\_ILLEGAL\_PARAM**  is returned when  **hi\_mpi\_vdec\_send\_stream**  is called. The application log contains the error message  **stream len can't be zero!**, as shown in the example below.

```text
[Vdec]:vdec_check_send_stream [Line]:6563 pid 578 usr chn 64 device 0 chn 64 stream len can't be zero!
```

## Possible Cause

The error  **stream len can't be zero!**  is reported in the log, which is intercepted by the VDEC code parameter verification. Check whether the input parameter  **stream-\>len**  or  **stream-\>addr**  is valid.

## Solution

Check the value of  **stream-\>len**  in the code. If  **len**  is  **0**, modify the code logic to assign a value to the parameter.
