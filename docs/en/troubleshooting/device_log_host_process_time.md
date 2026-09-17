# Determining the Start and End Time of the Host Process Based on Device Logs

When locating a fault, you need to preliminarily locate the time when the fault occurs, and then locate the fault based on the detailed logs generated at the time when the fault occurs. In this case, you can search for the  **ringbuffer**  keyword in the device log to determine the start and end time of the service process and locate the time when the problem occurs.

Ringbuffer is a piece of shared memory for reporting error information. When a task is started, the create ringbuffer operation is performed. When the task is complete, the  **delete ringbuffer**  operation is performed. Therefore, you can check the start and end time of the task based on the  **ringbuffer**  log. The detailed operations are as follows:

## Ascend EP  Form

1. Log in to the host server.
2. Use the msnpureport tool to export on-device system logs and other maintenance and debugging information.

    Run the msnpureport tool command in a directory \(for example,  **/var/log/npu/report**\) on which you have the read, write, and execute permissions.

    The following is an example of the msnpureport tool command:

    ```bash
    msnpureport -f
    ```

3. In the root directory of the exported system logs on the non-control CPU of the device, query the process creation and destruction logs.

    For example, run the following command to query the log information about the process startup and end on device 0 in the  **/var/log/npu/report/\*/slog/device-os-0/\[run|debug\]/device-0**  directory. The asterisk \(\*\) indicates the timestamp when the log file is created.

    ```bash
    grep -rn ringbuffer
    ```

    A log snippet is as follows:

    ```text
    device-0_20231201062601524.log:23102:[EVENT] TSCH(-1,null):2023-12-02-14:29:25.780.720 17641 (dieid:0,cpuid:0) ringbuffer.c:177 delete_ringbuffer: pid=3299758, vf_id=0
    device-0_20231201062601524.log:23103:[EVENT] TSCH(-1,null):2023-12-02-14:29:25.780.756 17642 (dieid:0,cpuid:0) ringbuffer.c:134 create_ringbuffer: pid=3299758, vf_id=0, buffer_len=10, runtime ver=2, offset=276096, ringbuffer_addr=0x1f7dc00000.
    device-0_20231201062601524.log:23104:[EVENT] TSCH(-1,null):2023-12-02-14:29:25.780.774 17643 (dieid:0,cpuid:0) ringbuffer.c:163 create_ringbuffer: last_Id=21, vf_id=0, pid=3299758
    device-0_20231204114303693.log:23503:[EVENT] TSCH(-1,null):2023-12-04-11:44:15.752.017 47266 (dieid:0,cpuid:0) ringbuffer.c:177 delete_ringbuffer: pid=3299758, vf_id=0
    ```

    As shown in the preceding figure:

    - The keyword  **create\_ringbuffer**  in the log indicates that the process is started. The creation time of the process whose ID is  **3299758**  on device-0 in the preceding figure is  **2023-12-02-14:29:25**.

        To avoid repeated creation, a ringbuffer is deleted each time before another ringbuffer is created. Therefore, the generated logs include  **delete\_ringbuffer**  and  **create\_ringbuffer**.

        In the log file, if there are multiple  **create\_ringbuffer**  records for the same process, the log time that contains  **ringbuffer\_addr**  indicates the time when the process is started.

    - The keyword  **delete\_ringbuffer**  in the log indicates that the process is ended. The destroy time of the process whose ID is  **3299758**  on device-0 in the preceding figure is  **2023-12-04-11:44:15**.

        In the log, if there are multiple  **delete\_ringbuffer**  records for the same process, the time of the last  **delete\_ringbuffer**  record indicates the end time of the process.

## Ascend RC  Form

1. Log in to the board environment.
2. Check device logs.

    For example, run the following command to query the log information about the process startup and end on device 0 in the  **/var/log/npu/slog/\[run|debug\]/device-0**  directory:

    ```bash
    grep -rn ringbuffer
    ```

    A log example is as follows:

    ```text
    device-0_20231201062601524.log:23102:[EVENT] TSCH(-1,null):2023-12-02-14:29:25.780.720 17641 (dieid:0,cpuid:0) ringbuffer.c:177 delete_ringbuffer: pid=3299758, vf_id=0
    device-0_20231201062601524.log:23103:[EVENT] TSCH(-1,null):2023-12-02-14:29:25.780.756 17642 (dieid:0,cpuid:0) ringbuffer.c:134 create_ringbuffer: pid=3299758, vf_id=0, buffer_len=10, runtime ver=2, offset=276096, ringbuffer_addr=0x1f7dc00000.
    device-0_20231201062601524.log:23104:[EVENT] TSCH(-1,null):2023-12-02-14:29:25.780.774 17643 (dieid:0,cpuid:0) ringbuffer.c:163 create_ringbuffer: last_Id=21, vf_id=0, pid=3299758
    device-0_20231204114303693.log:23503:[EVENT] TSCH(-1,null):2023-12-04-11:44:15.752.017 47266 (dieid:0,cpuid:0) ringbuffer.c:177 delete_ringbuffer: pid=3299758, vf_id=0
    ```

    As shown in the preceding figure:

    - The keyword  **create\_ringbuffer**  in the log indicates that the process is started. The creation time of the process whose ID is  **3299758**  on device-0 in the preceding figure is  **2023-12-02-14:29:25**.

        To avoid repeated creation, a ringbuffer is deleted each time before another ringbuffer is created. Therefore, the generated logs include  **delete\_ringbuffer**  and  **create\_ringbuffer**.

        In the log file, if there are multiple  **create\_ringbuffer**  records for the same process, the log time that contains  **ringbuffer\_addr**  indicates the time when the process is started.

    - The keyword  **delete\_ringbuffer**  in the log indicates that the process is ended. The destroy time of the process whose ID is  **3299758**  on device-0 in the preceding figure is  **2023-12-04-11:44:15**.

        In the log, if there are multiple  **delete\_ringbuffer**  records for the same process, the time of the last  **delete\_ringbuffer**  record indicates the end time of the process.
