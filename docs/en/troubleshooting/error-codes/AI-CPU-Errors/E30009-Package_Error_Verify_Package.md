# E30009 Package\_Error\_Verify\_Package

## Symptom

The following is error format. The meanings of the placeholders %s in sequence are: package name, error cause.

```text
Failed to verify the signature of package %s on the device. Reason: %s.
```

Error example:

```text
Failed to verify the signature of package Ascend-aicpu_legacy.tar.gz on the device. Reason: Signature verification failed. The possible cause is that a multi-bit ECC error occurred on the device or the software package has been tampered with. Obtain the device log, check whether ECC errors are reported, and contact technical support at https://www.hiascend.com/support.
```

## Solution

Please use the correct package as prompted in the Reason.
