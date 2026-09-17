# Using the Third-Party ASan Tool to Detect Memory Errors

The ASan tool is a third-party memory error detection tool for the C/C++ language. It can be used to detect errors including using released memory, memory overwriting, and memory leaks. In GCC 4.8 and later versions, the ASan tool is deployed and does not need to be installed separately.

1. Find the path of the ASan library.

    The following command is an example:

    ```text
    find Directory to be queried -name "libasan*"
    ```

    This section assumes that the ASan library is in the  **/usr/lib64/libasan.so.6.0.0**  directory.

2. Enter the path of the ASan library when executing the application.

    The following command is an example \(_main_  indicates the executable file of the application and needs to be modified as required\):

    ```text
    LD_PRELOAD=/usr/lib64/libasan.so.6.0.0 ./main
    ```

3. If a memory problem is detected by the ASan tool during application execution, analyze the code problem by referring to the ASan logs.

    The following is an example of the error log indicating that the ASan tool detects memory leaks. In the example, the  **malloc**  API is used to allocate 10 MB memory but the  **free**  API is not used to free the memory.

    ```text
    ERROR: LeakSanitizer: detected memory leaks

    Direct leak of 10485760 byte(s) in 1 object(s) allocated from:
        #0 0xffff98d55034 in malloc (/usr/lib64/libasan.so.6.0.0+0xa5034)
        #1 0xffff93de3500 in SvmInit (/usr/local/Ascend/driver/lib64/driver/libascend_hal.so+0xf3500)
        #2 0xffff9975da48  (/lib/ld-linux-aarch64.so.1+0x3a48)
        #3 0xffff9975db30  (/lib/ld-linux-aarch64.so.1+0x3b30)
        #4 0xffff98c2d190 in _dl_catch_exception (/usr/lib64/libc.so.6+0x12c190)
        #5 0xffff99765f58  (/lib/ld-linux-aarch64.so.1+0xbf58)
        #6 0xffff98c2d130 in _dl_catch_exception (/usr/lib64/libc.so.6+0x12c130)
        #7 0xffff997662c4  (/lib/ld-linux-aarch64.so.1+0xc2c4)
        #8 0xffff98b7c180  (/usr/lib64/libc.so.6+0x7b180)
        #9 0xffff98c2d130 in _dl_catch_exception (/usr/lib64/libc.so.6+0x12c130)
        #10 0xffff98c2d1fc in _dl_catch_error (/usr/lib64/libc.so.6+0x12c1fc)
        #11 0xffff98b7bc5c  (/usr/lib64/libc.so.6+0x7ac5c)
        #12 0xffff98b7c254 in dlopen (/usr/lib64/libc.so.6+0x7b254)
        #13 0xffff98cfb5d0  (/usr/lib64/libasan.so.6.0.0+0x4b5d0)
    ```
