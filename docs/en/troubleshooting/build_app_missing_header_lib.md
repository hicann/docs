# An Error Is Reported During Application Sample Compilation and Running, Indicating That the Header File or Library File Missing

## Symptom

Obtain the sample code from the  **samples**  repository \([Image Classification](https://gitee.com/ascend/samples/blob/master/cplusplus/level2_simple_inference/1_classification/resnet50_imagenet_classification/README.md)\):

- During source code compilation, a message is displayed, indicating that the header file  **acl.h**  cannot be found. The following is an example:

    ```text
     fatal error: acl/acl.h: No such file or directory
     #include "acl/acl.h"
              ^~~~~~~~~~~
    compilation terminated.
    CMakeFiles/main.dir/build.make:62: recipe for target 'CMakeFiles/main.dir/main.cpp.o' failed
    make[2]: *** [CMakeFiles/main.dir/main.cpp.o] Error 1
    CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/main.dir/all' failed
    make[1]: *** [CMakeFiles/main.dir/all] Error 2
    Makefile:129: recipe for target 'all' failed
    ```

- During source code compilation, a message is displayed, indicating that the library file  **libascendcl.so**  cannot be found. \(In the error message,  **-l**  in  **-lascendcl**  indicates that the library file was searched for.\) The following is an example:

    ```text
    /usr/bin/ld: cannot find -lascendcl
    collect2: error: ld returned 1 exit status
    CMakeFiles/main.dir/build.make:94: recipe for target '/home/HwHiAiUser/sample/resnet50_firstapp/out/main' failed
    make[2]: *** [/home/HwHiAiUser/sample/resnet50_firstapp/out/main] Error 1
    CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/main.dir/all' failed
    make[1]: *** [CMakeFiles/main.dir/all] Error 2
    Makefile:129: recipe for target 'all' failed
    ```

## Possible Cause

The  **\{DDK\_PATH\}**  and  **\{NPU\_HOST\_LIB\}**  environment variables may be incorrectly set. In this sample, these environment variables are used to search for the acl API header file and library file, which are the dependency files for the compilation of the app source code.

## Solution

1. Log in to the source code compilation environment and run the following commands to check the values of the  **\{DDK\_PATH\}**  and  **\{NPU\_HOST\_LIB\}**  environment variables:
    - Checking the  **\{DDK\_PATH\}**  value:

        ```bash
        echo $DDK_PATH
        ```

        If no information is displayed, the environment variable is not set. Set it by referring to step 4.

    - Checking the  **\{NPU\_HOST\_LIB\}**  value:

        ```bash
        echo $NPU_HOST_LIB
        ```

        If no information is displayed, the environment variable is not set. Set it by referring to step 4.

2. Check whether the header file exists in the directory specified by  **\{DDK\_PATH\}**, the environment variable value obtained in step 1.

    The compilation script of the sample searches for the header file on which compilation depends based on the  **\{DDK\_PATH\}/runtime/include/acl**  directory. Therefore, you can check whether this directory exists. If yes, check whether the  **acl.h**  header file exists in this directory. If either the directory or the header file does not exist, set  **\{DDK\_PATH\}**  again by referring to step 4.

    Go to the directory specified by  **\{DDK\_PATH\}**. The following is a command example:

    ```bash
    cd $DDK_PATH
    ```

3. Check whether the library file exists in the directory specified by  **\{NPU\_HOST\_LIB\}**, the environment variable value obtained in step 1.

    The compilation script of the sample searches for the library file on which compilation depends based on the directory specified by  **\{NPU\_HOST\_LIB\}**. Therefore, you can check whether this directory exists. If yes, check whether the  **libascendcl.so**  library file exists in this directory. If neither the directory nor the library file exists, set  **\{NPU\_HOST\_LIB\}**  again by referring to step 4.

    Go to the directory specified by  **\{NPU\_HOST\_LIB\}**. The following is a command example:

    ```bash
    cd $NPU_HOST_LIB
    ```

4. Set the environment variables.

    The compilation script searches for the header file on which compilation depends based on the  **\{DDK\_PATH\}/runtime/include/acl**  directory, and searches for the library file based on the directory specified by  **\{NPU\_HOST\_LIB\}**.

    Replace  _$\{INSTALL\_DIR\}_  with the CANN component directory. For example, if the installation is performed by the  **root**  user, the default file storage path is  **/usr/local/Ascend/cann**.

    - If the OS architectures of the development and operating environments are the same, set the environment variables as follows:

        ```bash
        export DDK_PATH=${INSTALL_DIR}
        export NPU_HOST_LIB=$DDK_PATH/runtime/lib64/stub
        ```

    - If the OS architectures of the development and operating environments are different, set the environment variables as follows:

        For example, if the development environment uses the x86 architecture and the operating environment uses the AArch64 architecture, cross compilation is involved. In this case, you need to install the software package of the AArch64 architecture in the development environment and set the  **\{DDK\_PATH\}**  environment variable to the installation directory of this software package. In this way, the header file and library file in the software package are the same as those in the operating environment, which facilitates code compilation.

        ```bash
        export DDK_PATH=${INSTALL_DIR}/arm64-linux
        export NPU_HOST_LIB=$DDK_PATH/runtime/lib64/stub
        ```

    >**NOTE:**
    >- You can log in to the corresponding environment and run the  **uname -a**  command to query the OS architecture.
    >- If you do not know the directories of the header file  **acl.h**  and library file  **libascendcl.so**, you can run the  **find -name "_filename_"**  command to search for the file directories and then configure the environment variables.
