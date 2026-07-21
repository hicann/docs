# Camera找不到设备

## 适用场景

- 业务场景：Camera出图

- 适用处理器：Atlas 200I/500 A2 推理产品
- 处理器形态：EP、RC

## 问题现象描述

显示open ISP device error!  返回错误码0xa01c8040。

## 可能原因

没有插入isp ko。

## 处理步骤

1. lsmod检查ko的插入情况。
2. 执行以下命令重新插入ao相关的ko。

    ```bash
    insmod /var/davinci/driver/drv_isp.ko
    ```

3. 再次执行Camera业务。
