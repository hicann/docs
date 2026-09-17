# Multi-Process Error Reported During Display over the HDMI and VO Module

## Application Scenario

- Service scenario: display over the HDMI and VO module
- Applicable processor:  Atlas 200I/500 A2 inference products
- Processor forms: EP and RC

## Symptom

When the display function of the VO module and HDMI is enabled, the following error message is displayed in the log, indicating that multiple processes are not supported.

```text
[ERROR] KERNEL(3720,sklogd):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [klogd.c:246][3146.816065] [drv_vo][ERR][vo open:433]:VO functions must work in the same pid!!!
[ERROR] DSS(5303,vo test nvr hdmi hi test):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [mpi hdmi com.c:264][Lib_hdmi][mpi hdmi_com_init]:open HDMI err.
```

## Possible Cause

Other cases that call the VO module and HDMI are executed in the background.

## Solution

1. Check whether multiple ports are enabled by using software such as mobax and whether test cases that call the VO module and HDMI are being executed.
2. Run the  **ps -elf**  command to check whether there are other test cases that call the VO module and HDMI in the background.
3. Close other test cases that call the VO module and HDMI.
4. Execute the test case that display signals through the VO module and HDMI.
