# Application Process Suspension Due to Child Process Creation in Fork Mode

## Symptom

In the multi-device training scenario, the training process is suspended, the training times out, or the dataloader is suspended.

## Cause Analysis

1. Check the Python stack. The stack information contains the keyword  **fork**.

    The following is an example of the command for viewing Python stack information using the pyspy tool.

    Before running the pyspy command, you need to install GDB and py-spy. If GDB is not installed in the environment, you can install it using package manager \(including the  **apt-get install gdb**  and  **yum install gdb**  command\). For details about the installation procedure and usage, see  [GDB official documentation](https://sourceware.org/gdb/). If py-spy is not installed in the environment, run the  **pip3 install py-spy**  command to install it. \(If a message is displayed indicating that the pip version is low, for example, "You are using pip version 19.2.3, however version 24.0 is available", during the installation, run the  **pip3 install --upgrade pip**  command to upgrade pip as prompted.\)

    ```bash
    # Export the stack information of a specified process to a specified file. pid indicates the ID of the suspended user process, and pyspy.log indicates the file that stores the stack information. Replace them with the actual values.
    py-spy dump -p pid > pyspy.log
    ```

    The following is an example of the stack information \(_xxxx_  indicates the directory name;  _trainApp_  indicates the training program, depending on the actual service\):

    ```text
    1 Process 16203: /train/xxxx/xxxx/xxxx/python3.8 -u -m trainApp --config-dir
    2 Python  v3.8.19 (/train/xxxx/xxxx/xxxx/python3.8)
    3
    4 Thread 0xFFFF9CF35B50 (active): "MainThread"
    5    poll (multiprocessing/popen_fork.py:27)
    6    wait (multiprocessing/popen_fork.py:47)
    7    join (multiprocessing/process.py:149)
    8    _terminate_pool (multiprocessing/pool.py:729)
    9    __call__ (multiprocessing/util.py:224)
    10   _scale_down_hw (datasets/datasets.py:96)
    11   __init__ (datasets/datasets.py:73)
    ......
    ```

2. Check the C/C++ stack. The stack information contains the keyword  **acquire\_lock**.

    Run the GDB command to check the call stack information of the suspended process. If GDB is not installed in the environment, you need to install it using package manager \(including  **apt-get install gdb**  and  **yum install gdb**\). For details about the installation procedure and usage, see  [GDB official documentation](https://sourceware.org/gdb/).

    ```bash
    # Run the gdb command. pid indicates the ID of the suspended process. Replace it with the actual process ID.
    gdb -p pid
    # Check the call stack.
    (gdb)bt
    ```

    The following is an example of stack information:

    ```text
    #0 0x0000ffffa9b2b268 in do_futex_wait.constprop () from /lib/aarch64-linux-gnu/libpthread.so.0
    #1 0x0000ffffa9b2b39c in   new_sem_wait_slow.constprop.0 () from /lib/aarch64-linux-gnu/libpthread.so.0
    #2 0x0000ffffa9e96eb8 in PyThread_acquire_lock_timed () from /usr/local/lib/libpython3.8.so.1.0
    #3 0x0000ffffa9e865a8 in _PyThreadState_DeleteExcept () from /usr/local/lib/libpython3.8.so.1.0
    #4 0x0000ffffa9eb94ac in _PyOS_AfterFork_Child () from /usr/local/lib/libpython3.8.so.1.0
    #5 0x0000ffffa9eb9638 in ?? () from /usr/local/lib/libpython3.8.so.1.0
    ......
    ```

3. According to the  **fork**  keyword of the Python stack and the  **acquire\_lock**  keyword of the C++ stack, check that the training process is suspended because the Python bug is triggered by process startup in  **fork**  mode.

    In Python 3.8 to Python 3.11, if the process creation mode is not specified or the  **fork**  mode is explicitly specified, the lock status of the parent process may be copied when a child process is created. When the lock obtainment is triggered in the child process, a deadlock occurs. As a result, the service process is suspended.

    The Python community also describes the same issue:  [https://github.com/python/cpython/issues/74580](https://github.com/python/cpython/issues/74580).

## Solution

You can select either of the following solutions based on service requirements:

- Solution 1: Install the patches of Python 3.8 to Python 3.11 by following the instructions on  [Python official website](https://www.python.org/downloads/).

    On the Python official website, patches are provided for Python3.8 to Python 3.11 to fix bugs caused by the fork issue.

    ![](figures/image_0000002060369161.png)

    In these patch versions, the fork issue is also described as follows:

    ![](figures/image_0000002024482132.png)

- Solution 2: Modify the customer service code to explicitly use the  **forkserver**  or  **spawn**  mode.

    Note: If there are many positions where the  **fork**  mode needs to be modified or the workload is heavy, solution 1 is recommended to prevent omission.

    1. Find the Python installation directory.

        Run the  **pip show torch**  command to query the Python installation directory. The following is an example of the query result.

        ![](figures/image_0000002060783033.png)

    2. Run the  **find -name popen\_fork.py**  command in the Python installation directory to find the  **popen\_fork.py**  file and add the code that triggers the stack to the positions where the processes are started in  **fork**  mode.

        Add the code to the  **\_launch \(self,process\_obj\)**  function to trigger the stack for all child processes in  **fork**  startup mode.

        ![](figures/image_0000002028178270.png)

        For example, add the following code to line 70 in the preceding figure to trigger stack information printing at the positions where the processes are started in  **fork**  mode.

        ```python
        import traceback
        import time
        timestamp = time.time()
        timestamp_str = str(int(timestamp))
        file_name = f"stack_{timestamp_str}.txt"
        with open("/home/{}.txt".format(file_name),"a") as f:
            traceback.print_stack(file=f)
        ```

    3. Re-run the training service and check the Python stack again.

        In the stack information, ignore the CANN-related stacks and only change the  **fork**  startup mode of the customer service to  **spawn**  or  **forkserver**  startup mode. For details about the startup modes, see  [Python official document](https://docs.python.org/3.8/library/multiprocessing.html). \(Select the document of the corresponding Python version.\)
