# 如何查看Python、C&C++应用程序的堆栈

## 查看Python应用程序的堆栈

此处以pyspy工具查看Python堆栈信息为例说明。

使用pyspy命令前，需要安装gdb和py-spy。若环境中未安装gdb，可通过包管理（如**apt-get install gdb**命令、**yum install gdb**命令）进行安装，详细安装步骤及使用方法请参见[GDB官方文档](https://sourceware.org/gdb/)；若环境中未安装py-spy，可使用**pip3 install py-spy**命令安装（若安装时提示pip版本低，例如_You are using pip version 19.2.3, however version 24.0 is available_，这时可按照提示使用pip3 install --upgrade pip命令升级pip即可）。

```bash
# 将指定进程的堆栈信息导出到指定文件中，pid表示卡住的用户进程ID，pyspy.log表示存放堆栈信息的文件，请根据实际情况替换
py-spy dump -p pid > pyspy.log
```

堆栈信息示例如下（_xxxx_表示目录名称、_trainApp_表示训练程序，由实际业务情况决定，此处仅为示例）：

```bash
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

## 查看C/C++应用程序的堆栈

通过gdb命令观察卡住进程的调用栈信息，若环境中未安装gdb，则需要安装gdb，可通过包管理（如apt-get install gdb、yum install gdb）进行安装，详细安装步骤及使用方法请参见[GDB官方文档](https://sourceware.org/gdb/)。

```bash
# 先执行gdb命令,pid表示卡住的用户进程ID，请根据实际情况替换
gdb -p pid
# 再查看调用栈
(gdb)bt
```

堆栈信息示例如下：

```bash
#0 0x0000ffffa9b2b268 in do_futex_wait.constprop () from /lib/aarch64-linux-gnu/libpthread.so.0
#1 0x0000ffffa9b2b39c in   new_sem_waut_slow.constprop.0 () from /lib/aarch64-linux-gnu/libpthread.so.0
#2 0x0000ffffa9e96eb8 in PyThread_acquire_lock_timed () from /usr/local/lib/libpython3.8.so.1.0
#3 0x0000ffffa9e865a8 in _PyThreadState_DeleteExcept () from /usr/local/lib/libpython3.8.so.1.0
#4 0x0000ffffa9eb94ac in _PyOS_AfterFork_Child () from /usr/local/lib/libpython3.8.so.1.0
#5 0x0000ffffa9eb9638 in ?? () from /usr/local/lib/libpython3.8.so.1.0
......
```
