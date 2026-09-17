# Description

An error code consists of six characters, for example, E10035.

- The first character indicates the error level, which can be E \(error\), W \(warning\), or I \(information\).
- The second character indicates the module.
    - 1: GE
    - 2: FE
    - 3: AI CPU
    - 4: TE Fusion
    - 7: Vector operator plugins
    - 8: Vector operators
    - B: TBE Pass compilation tool
    - C: Auto Tune
    - D: RL Tune
    - E: Runtime
    - F: LxFusion and AutoDeploy
    - G: AOE
    - H: ACL
    - I: HCCL
    - J: HCCP
    - K: Profiling
    - L: Driver
    - M: queue scheduling
    - N: DVPP
    - O: AMCT
    - P: Dump
    - Z: common operator error codes and operator API execution error codes \(for example, aclnn operator API error codes\)

- The remaining four characters indicate error codes. Error codes 0000 to 8999 are user errors, and error codes 9000 to 9999 are internal error codes.

The error code information that is printed varies according to the scenario, use case, and fault cause. In this document, \[%s\] is a variable to denote the actual log. For example, the E10035 error code in this document is displayed in the following format:

The \[--dynamic\_batch\_size\], \[--dynamic\_image\_size\], or \[--dynamic\_dims\] argument has \[%s\] profiles, which is less than the minimum \[%s\].

The following is an example of the error message displayed on the screen. The \[%s\] variable is replaced with the actual information.

The \[--dynamic\_batch\_size\], \[--dynamic\_image\_size\], or \[--dynamic\_dims\] argument has \[_1_\] profiles, which is less than the minimum \[_2_\].

>**NOTE:**
>
>- In the scenario of executing asynchronous tasks, such as issuing multiple operator execution tasks continuously, multiple operators may report errors, so the error message may contain errors of multiple operators. You need to troubleshoot the problems starting from the first error-reporting operator.
>- Generally, E_\*_9_\*\*\*_  indicates an internal error code. If an internal error code is displayed, contact Huawei technical support for troubleshooting.  After obtaining the logs, click  [here](https://www.hiascend.com/support)  to contact technical support.
>- The error code information described in this document has been completely displayed on the screen, including possible causes and solutions. Here is an example for reference only.
