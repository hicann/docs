# EN0016 File\_Operation\_Error\_Open

## Symptom

The following is error format. The meanings of the placeholders %s in sequence are: file name, error cause.

```text
Failed to open file %s. Reason: %s.
```

Error example:

```text
Failed to open file libmpi_dvpp_adapter.so. Reason: libmpi_dvpp_adapter.so: No such file or directory.
```

## Possible Cause

1. The file does not exist.

2. Insufficient file permissions.

3. Package installation error.

## Solution

1. Configure the file path correctly.

2. Configure the file permissions correctly.

3. Reinstall the package.
