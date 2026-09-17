# Accuracy Overflow/Underflow During Atomic Add

## Analysis Result

If the  **info.txt**  file contains the following conclusion, the AI Core error is caused by accuracy overflow/underflow.

```text
Analysis result: success.
"**********************Root cause conclusion******************"
Atomic add has a precision overflow. Check the operator precision. Note that if tasks are concurrently executed on the NPU, a false warning may be reported.
```

In the slog file  **\(report/\*/slog/dev-os-_id_/\[run|debug\]/device-os/device-os\_\*.log\)**  of the device, check whether the keyword  **Vm fault failed**  exists. If the keyword does not exist, the AI Core error is caused by atomic accuracy overflow/underflow. If it exists, memory overwriting occurs. The following is an example of the slog file:

```text
[EVENT] KERNEL(4128,sklogd):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [klogd.c:253][2572550.901383] [ascend] [ERROR] [devmm] [devmm_svm_device_fault 438] <kworker/u16:186:9871,9871> Vm fault failed. (hostpid=1885445; devid=0; vfid=0; ret=64; fault_addr=0x1240f1fa0000; start=0x1240f1fa0000)
```

On the  Atlas A2 training products/Atlas A2 inference products, the accuracy overflow/underflow during atomic add does not occur due to hardware optimization.

## Fault Root Causes

During operator computation, extreme data encounters the atomic accumulation instruction. If overflow occurs during atomic accumulation, the 0x800000 error is reported.

## Solution

Generally, this error is caused by incorrect input data. Optimize the accuracy for further locating. For example, in the inference scenario, optimize the accuracy by referring to section "Accuracy/Performance Optimization" in  [Application Development \(C & C++\)](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/others/acldevg/aclcppdevg_000006.html).
