# Collecting AI Core Error Information

## Information Types

Note: When collecting logs, you need to collect logs generated around the time when AI Core errors occur. If irrelevant information or other error information in the old logs is collected, the msaicerr tool may report errors when analyzing the AI Core errors.

| Information Type | Description |
| --- | --- |
| Application logs | Debug or run logs generated when applications are running on the host or device. The logs are used to view user-mode logs. |
| Trace logs | The logs are used to check the maintenance and debugging information about the software stack. |
| Operator exception dump files | Dump data, including the operator input, operator data, and workspace data. The data is used by the msaicerr tool to construct single-operator cases when analyzing errors. |
| Abnormal operator compilation information | Operator .o and .json files, which are used by the msaicerr tool to construct single-operator cases when analyzing errors. |
| On-device system logs and other maintenance and debugging information | Logs including slogs, syslogs, and black box logs. The logs are used to view the system running information and kernel-mode driving information of the device. |

Collecting AI Core errors involves obtaining logs and setting environment variables. This section uses the default log paths to describe how to obtain various logs and takes examples to describe how to set environment variables.

- For details about log levels, log paths, and log files, see  [Log Reference](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/maintenref/logreference/logreference_0001.html).
- For details about the environment variables and their restrictions, see  [Environment Variables](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/maintenref/envvar/envref_07_0001.html).

## Determining Whether Service Re-run Is Required Before Collecting Information

Note: If the time of the AI Core error in the log is long after the occurrence time of the error, the old log may have been overwritten or deleted. In this case, you need to re-run the service to collect the fault information again.

| Scenario | Whether Re-run Is Required |
| --- | --- |
| Services that depend on the PyTorch/MindSpore/TensorFlow framework, such as training and online inference services | Service re-run is not required.<br>By default, the system records the information for locating AI Core errors. |
| Services that do not depend on or use the PyTorch/MindSpore/TensorFlow framework, for example, offline inference, single-operator calling, and graph build services | Service re-run is required.<br>To manually collect some information, you need to set environment variables and then re-run services. For example, before collecting the exception dump file of an operator, you need to set the NPU_COLLECT_PATH environment variable. For details about the NPU_COLLECT_PATH environment variable, see "Fault Information Collection" > "NPU_COLLECT_PATH" in [Environment Variables](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/maintenref/envvar/envref_07_0001.html). For details about how to manually collect information, see [Manual Collection](#section420651516422).<br>After the NPU_COLLECT_PATH environment variable is set, service processing becomes slow, affecting the performance. Therefore, you are advised to disable the environment variable in time after faults are located.<br> NOTE: In case that performance is sensitive while disk resources are sufficient, you can call the aclInit API to enable the exception operator dump configuration (configuration of dump_scene in the .json file) to automatically generate exception dump files for analyzing AI Core errors when service re-run is not required. In this case, the performance of most networks deteriorates by less than 1%. However, after the configuration is enabled, dump files generated for multiple AI Core errors consume disk space. You need to clear historical dump data. For details about the API, see Runtime APIs > Initialization and Deinitialization > aclInit. |

## Collection Methods

When locating AI Core errors, you need to collect fault information in advance. The following two methods are available.

| Collection Method | Description |
| --- | --- |
| Manual collection | Collect information related only to AI Core errors, including exception dump files, operator compilation information, and host application log files. For details about the collection method, see [Manual Collection](#section420651516422). |
| Automatic collection | Use the [asys](https://gitcode.com/cann/oam-tools/blob/master/docs/en/asys/asys_functions_and_restrictions.md) tool to collect all fault information (more than manually collected information), including the installation version, device health status, exception dump files, operator compilation information, and full log files. For details about the collection method, see [Automatic Collection](#section194651132144216).<br>Note: The asys tool can be used to collect fault information in only limited scenarios, excluding cluster, container, virtual machines, and cloud. |

<a id="section420651516422"></a>

## Manual Collection

- When service re-run is not required
    1. Create an empty directory \(for example,  **aic\_err\_info**\) for saving all the collected AI Core error information.

        ```bash
        mkdir ${HOME}/aic_err_info
        ```

    2. Collect application logs, trace logs, exception dump files, and abnormal operator compilation information, and move them to the  **_$\{HOME\}_/aic\_err\_info**  directory for unified management.

        Obtain the information from the directories specified by the following environment variables:

        - Obtain application logs from the path specified by the  **ASCEND\_PROCESS\_LOG\_PATH**  environment variable. For details about the  **ASCEND\_PROCESS\_LOG\_PATH**  environment variable, see  Logs \> ASCEND\_PROCESS\_LOG\_PATH.
        - Obtain application logs, trace logs, and exception dump files from the path specified by the  **ASCEND\_WORK\_PATH**  environment variable. For details about the  **ASCEND\_WORK\_PATH**  environment variable, see  Installation and Configuration \> ASCEND\_WORK\_PATH.
        - If the two environment variables exist at the same time, obtain application logs from the path specified by the  **ASCEND\_PROCESS\_LOG\_PATH**  environment variable, and obtain trace logs, exception dump files, and abnormal operator compilation information from the path specified by the  **ASCEND\_WORK\_PATH**  environment variable.

        If the corresponding environment variable is not configured in the current environment, you can obtain the information from the corresponding default storage directories.

        - The default directory for storing application logs is  **_$\{HOME\}_/ascend/log**  on the host server.
        - The default directory for storing trace logs is  **$HOME/ascend/atrace/**  on the host server.
        - The default directory for storing exception dump files and abnormal operator compilation information is the  **extra-info/data-dump/_\{device\_id\}_**  directory of the current path where the inference application or training script is executed. This directory contains the input and output data files  **exception\_info._\{stream\_id\}_._\{task\_id\}_._\{timestamp\}_**  related to AI Core errors and the abnormal operator compilation information \(.o and .json files\).

        >**NOTE:**
        >- If no abnormal operator compilation information is obtained based on the preceding environment variables or default directories, obtain the information by referring to  [Manually Collecting Operator Compilation Information \(.o and .json Files\)](collect_operator_compile_info.md).
        >- The trace logs on the host server cannot be automatically cleared and may occupy a large amount of disk space. If the memory space is limited, you can run the following command to copy the trace logs of a specified process in the  **$HOME/ascend/atrace/**  directory as required:  **cp -rf $HOME/ascend/atrace/trace\__\{PID\}_\* aic\_err\_info/**.
        >- The collected dump files cannot be viewed using a text tool. To view the dump file content, see  [Parsing Dump Files](https://gitcode.com/cann/oam-tools/blob/master/docs/en/msaicerr/Dump_files_parsing.md).

    3. Collect on-device system logs and other maintenance and debugging information, including slogs, syslogs, and black box logs.

        Run the msnpureport tool as the  **root**  user on the host, export the logs to the host, and copy the logs to the  **aic\_err\_info**  directory.

        ```bash
        # Run the msnpureport command in a directory (for example, ${HOME}/ascend/report) on which you possess both the read and write permissions on the host.
        msnpureport -f

        # Move log files to the aic_err_info directory.
        mv ${HOME}/ascend/report aic_err_info/
        ```

    4. Move the information in the  **_$\{HOME\}_/aic\_err\_info**  directory to another directory. The directory name can contain a timestamp so that you can manage the collected fault information by time.

        ```bash
        mv ${HOME}/aic_err_info  ${HOME}/aic_err_info_timestamp
        ```

- When service re-run is required
    1. Create an empty directory \(for example,  **aic\_err\_info**\) for saving all the collected AI Core error information.

        ```bash
        mkdir ${HOME}/aic_err_info
        ```

    2. Set environment variables.

        The following is an example of setting the environment variables:

        ```text
        # By default, the plog and atrace directories are generated in the directory specified by ASCEND_WORK_PATH to store application logs and trace logs, respectively.
        export ASCEND_WORK_PATH=${HOME}/aic_err_info

        # Specify the directory for storing application logs. The directory specified by the ASCEND_PROCESS_LOG_PATH environment variable has a higher priority for storing application logs.
        export ASCEND_PROCESS_LOG_PATH=${HOME}/aic_err_info/plog

        # By default, the extra-info directory is generated in the directory specified by NPU_COLLECT_PATH. The data-dump subdirectory stores the exception dump files and abnormal operator compilation information.
        export NPU_COLLECT_PATH=${HOME}/aic_err_info/
        ```

        For details about the environment variables and their restrictions, see the following sections in  [Environment Variables](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/maintenref/envvar/envref_07_0001.html).

        - Installation \> ASCEND\_WORK\_PATH
        - Logs \> ASCEND\_PROCESS\_LOG\_PATH
        - Fault Information Collection \> NPU\_COLLECT\_PATH

    3. Re-run the service, that is, run the service program of the user again. Obtain the application logs, trace logs, exception dump files, and abnormal operator compilation information from the path specified by the environment variables.

        Check whether the operator compilation information \(.o and .json files\) exists in the path specified by the  **NPU\_COLLECT\_PATH**  environment variable. If not, search for the information in the default CANN installation path  **/usr/local/Ascend/cann**  and then in the default directory  **_$\{HOME\}_/atc\_data**. For details, see  [Manually Collecting Operator Compilation Information \(.o and .json Files\)](collect_operator_compile_info.md).

    4. Collect on-device system logs and other maintenance and debugging information. The collection method is the same as that in the scenario where service re-run is not required.
    5. Move the information in the  **_$\{HOME\}_/aic\_err\_info**  directory to another directory. The directory name can contain a timestamp so that you can manage the information by time.

        ```bash
        mv ${HOME}/aic_err_info  ${HOME}/aic_err_info_timestamp
        ```

<a id="section194651132144216"></a>

## Automatic Collection

For details about the restrictions on using the asys tool, see  [Functions and Restrictions of the asys Tool](https://gitcode.com/cann/oam-tools/blob/master/docs/en/asys/asys_functions_and_restrictions.md). Before using the asys tool, install and configure it. For details, see the prerequisites in  [Environment Setup](https://gitcode.com/cann/oam-tools/blob/master/docs/en/asys/asys_environment_preparation.md).

- When service re-run is not required, run the  **asys collect**  command to collect fault information.

    ```bash
    asys collect --output=path
    ```

    **output**  indicates the directory for saving collected information. For details about the parameters and restrictions, see  [Fault Information Collection](https://gitcode.com/cann/oam-tools/blob/master/docs/en/asys/fault_information_collection.md).

- When service re-run is required, run the  **asys launch**  command to concurrently re-run the service and collect fault information.

    ```bash
    asys launch --task="sh ../app_run.sh" --output=path
    ```

    **task**  indicates the task to be re-run, and  **output**  indicates the directory for storing the collected information. For details about the parameters and restrictions, see  [Service Re-run And Fault Information Collection](https://gitcode.com/cann/oam-tools/blob/master/docs/en/asys/rerun_fault_information_collection.md).

    Note: In an offline inference scenario, to rebuild a model \(for example, using the ATC tool to convert the model\), run the  **asys launch**  command to re-run the model building task, and then run the  **asys launch**  command to re-run the inference service based on the recompiled model. Additionally, place the maintenance and debugging information collected during model building and inference in the same directory, for example,  **$HOME/asys\_output**.

>**NOTE:**
>After information is collected using the tool, check whether dump files and abnormal operator compilation information \(.o and .json files\) exist in the  **dfx/data-dump**  directory, and whether log files exist in the  **dfx/log/host/cann**  directory. If the files do not exist, the AI Core error information cannot be extracted using the msaicerr tool.
