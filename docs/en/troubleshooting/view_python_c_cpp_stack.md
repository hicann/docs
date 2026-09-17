# How Do I View the Stacks of Python and C&C++ Applications?

## Viewing the Stack of a Python Application

The following uses the pyspy tool as an example to describe how to view Python stack information.

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

## Viewing the Stack of a C/C++ Application

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
