# EN0007 Execution\_Error\_DVPP\_Operator\_Timeout

## Symptom

The following is error format. The meanings of the placeholders %s in sequence are: task name, error cause.

```text
%s times out. Reason: %s.
```

Error example:

```text
GetResult times out. Reason: the configured timeout might be too short.
```

## Possible Cause

1. The input timeout interval is improper;
2. The buffer is full.

## Solution

1. Set the timeout interval to a proper value.
2. Call interface hi\_mpi\_vpc\_get\_result to release buffer.
