# Collecting Memory OOM Error Information

The information can be collected manually or automatically.

- Manual collection: Collect host and device logs and files. Only the minimum set of information is collected.
- Automatic collection: On the host server, use the  [asys](https://gitcode.com/cann/oam-tools/blob/master/docs/en/asys/asys_functions_and_restrictions.md)  tool to collect all fault-related information, including the installation version information, device health status information, dump files, operator compilation information, and full log files.

    Note: The asys tool can be used to collect fault information in only limited scenarios, excluding cluster, container, virtual machines, and cloud.

## Manual Collection

To collect application logs, on-device system logs, and other maintenance and debugging information, perform the following steps:

1. Plan a directory for storing log files on the host server, for example,  **$\{HOME\}/err\_log\_info/**.
2. The default path of application log files is  **_$\{HOME\}_/ascend/log**  on the host server. Move the log files to the  **err\_log\_info**  directory.

    ```bash
    mv ${HOME}/ascend/log ${HOME}/err_log_info/
    ```

3. Use the msnpureport tool to export on-device system logs and other maintenance and debugging information to the host, including slogs, syslogs, and black box logs.

    ```bash
    # Create a directory for storing logs and files in the ${HOME}/err_log_info directory.
    cd ${HOME}/err_log_info
    mkdir report

    # Run the msnpureport command in the report directory.
    cd report
    msnpureport -f
    ```

For details about log levels, log paths, and log files, see  [Log Reference](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/maintenref/logreference/logreference_0001.html).

## Automatic Collection Method

For details about the restrictions on using the asys tool, see  [Functions and Restrictions of the asys Tool](https://gitcode.com/cann/oam-tools/blob/master/docs/en/asys/asys_functions_and_restrictions.md). Before using the asys tool, install and configure it. For details, see the prerequisites in  [Environment Setup](https://gitcode.com/cann/oam-tools/blob/master/docs/en/asys/asys_environment_preparation.md).

The following is an example of the asys tool command. Run the  **asys collect**  command to collect fault information.

```bash
asys collect --output="path"
```

**output**  indicates the directory for saving collected information. For details about the parameters and restrictions, see  [Fault Information Collection](https://gitcode.com/cann/oam-tools/blob/master/docs/en/asys/fault_information_collection.md).
