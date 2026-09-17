# Core Dump During Single-Operator Execution

## Symptom

After a single-operator is executed, the memory is freed repeatedly. As a result, a core dump occurs, and the following key log information is displayed:

```text
double free or corruption(!prev)
```

## Possible Cause

Memory is freed repeatedly due to incorrect code logic.

## Solution

1. Load the executable file to GDB.
2. Debug with GDB.
3. Check the called stack.
4. After obtaining the logs, click  [here](https://www.hiascend.com/support)  to contact technical support.  Perform this operation if the problem does not lie in the code
