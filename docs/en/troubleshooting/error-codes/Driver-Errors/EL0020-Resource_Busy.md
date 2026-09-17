# EL0020 Resource\_Busy

## Symptom

The following is error format. The placeholder %s indicates the Device ID.

```text
Device %s is occupied by multiple containers.
```

Error example:

```text
Device 0 is occupied by multiple containers.
```

## Solution

1. Check whether the device is shared by multiple containers.
2. If the device needs to be shared by multiple containers, enable the single-device multi-container function by using npu-smi set -t device-share -i id -c chip\_id -d value.
