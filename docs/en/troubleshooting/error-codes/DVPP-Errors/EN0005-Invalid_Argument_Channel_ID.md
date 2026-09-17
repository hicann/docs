# EN0005 Invalid\_Argument\_Channel\_ID

## Symptom

The following is error format. The meanings of the placeholders %s in sequence are: channel ID, error cause.

```text
An error occurred on channel resource %s. Reason: %s.
```

Error example 1:

```text
An error occurred on channel resource 0. Reason: dev[0] all channels are being used.
```

Error example 2:

```text
An error occurred on channel resource 0. Reason: input stream addr invalid or too large len.
```

## Solution

Check the input channel ID or the number of created channels.
