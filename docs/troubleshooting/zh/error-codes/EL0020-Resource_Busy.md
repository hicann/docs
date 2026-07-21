# EL0020 Resource\_Busy

## 错误信息

报错格式如下，占位符%s表示Device ID：

```text
Device %s is occupied by multiple containers.
```

报错示例如下：

```text
Device 0 is occupied by multiple containers.
```

## 解决方法

1. 检查设备是否被多容器共享。
2. 如果需要多容器共享，通过npu-smi set -t device-share -i id -c chip\_id -d value开启单机多容器功能。
