# Obtaining Fault IDs from Device Logs and Rectifying RAS Hardware Faults

RAS hardware faults refer to faults related to hardware reliability, availability, and serviceability. You can search for the solution in the error code manual of the corresponding version based on the value of  **event\_id**  \(RAS hardware error code\) in the log.

**Figure  1**  Troubleshooting process
![](figures/RAS_faults_obtaining_event_id.png)

1. On the host server, use the msnpureport tool to export on-device system logs and other maintenance and debugging information, including slogs, syslogs, event logs, and black box logs.

    Run the msnpureport tool command in a directory \(for example,  **/var/log/npu/report**\) on which you have the read, write, and execute permissions.

    The following is an example of the msnpureport tool command:

    ```bash
    msnpureport -f
    ```

    The exported logs and files are stored in the  **/var/log/npu/report**  directory by default.

2. From the event logs collected in step 1 (slog/dev-os-_id_/run/event/event\__\*_.log), find the log content of the corresponding device around the time when the fault occurs, and check whether the keyword  **event\_id**  exists in the log. If not, go to step3. If so, click  _[Health Management Fault Definition](https://support.huawei.com/enterprise/en/ascend-computing/ascend-hdk-pid-252764743)_  to obtain the manual of the corresponding version and refer to the solution provided within.

    If the time in the slog is not around the time when the error occurs, the old log may have been overwritten or deleted. In this case,  **event\_id**  related to the error cannot be found.

    You can run the npu-smi command to query the health status of a specified chip. If an RAS fault occurs, you can query the event IDs of the last eight faults, which can be used as a reference for fault locating.

    The following is an example of the npu-smi command \(_id_  indicates the device ID, and  _chip\_id_  indicates the chip ID. You can run the  **npu-smi info**  command to obtain the device ID and chip ID first\):

    ```bash
    npu-smi info -t health -i id -c chip_id
    ```

    The following is an example of the query result.

    ![](figures/image_0000001937528841.png)

3. From the black box logs collected in step 1, find the black box logs of the corresponding device around the time when the fault occurs in the  **hisi\_logs/device-_id_/_\*_/bbox**  directory, and check whether the keyword  **Hardware Error**  exists in the logs. If not, no hardware failure has been identified. If so, an unknown hardware fault occurs, and it is necessary to contact technical support for further fault locating.  After obtaining the logs, click  [here](https://www.hiascend.com/support)  to contact technical support.
