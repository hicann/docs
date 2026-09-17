# Failure in Creating a VPC Channel

## Symptom

The error code  **HI\_ERR\_VPC\_EXIST**  is returned when  **hi\_mpi\_vpc\_create\_chn**  is called to create a channel. Information similar to the following is displayed in the log, which may vary in different versions:

```text
device 0, chn 0 has already been created!
```

Or

```text
dev 0 chnl 0 is busy
```

## Possible Cause

For the VPC module, you must specify a unique channel ID to create a channel by calling  **hi\_mpi\_vpc\_create\_chn**. The cause is that the channel ID already exists.

## Fault Locating

Check the usage of the channel ID in the code.

## Solution

1. Call  **hi\_mpi\_vpc\_create\_chn**  using a unique channel ID.

2. Call  **hi\_mpi\_vpc\_sys\_create\_chn**  first so that the system allocates a unique channel ID.
