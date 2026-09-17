# Symptoms of Process Interruption Faults

Application process abnormal exit, the possible causes are as follows:

- Interface error: check whether the plog file contains interface errors such as  **acl\*\*\***,  **\[drv api\]**, and  **rt\*\*\***  and etc.
- Task execution error: the plog file contains errors such as  **fault kernel\_name**,  **Task run failed**  and etc.
- TaskScheduler CPU heartbeat loss: The plogs contain the error information "Device lost heartbeat", and black box logs contain the error information "HEARTBEAT EXCEPTION".
- Control CPU heartbeat loss: Syslogs contain the error information "fatal panic".
- Memory resources are not released in a timely manner: the plog file contains the  **RESOURCE\_ALLOC\_FAIL**  error.
