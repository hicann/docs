# Failure in Obtaining the VPC Result

## Symptom

The  **hi\_mpi\_vpc\_get\_process\_result**  call returns  **HI\_ERR\_VPC\_ILLEGAL\_PARAM**. Information similar to the following is displayed in the log, which may vary in different versions:

```text
this channel doesn't have taskID 8845!, Channel id 0
```

Or

```text
taskId:8845 does not exist
```

## Possible Cause

An invalid task ID is passed to  **hi\_mpi\_vpc\_get\_process\_result**.

## Solution

Ensure that the task ID passed to the  **hi\_mpi\_vpc\_get\_process\_result**  call is the output from the function API.

Pass the task ID output from the function API to  **hi\_mpi\_vpc\_get\_process\_result**.
