# 无法正常播音

## 适用场景

- 业务场景：播音
- 适用处理器：Atlas 200I/500 A2 推理产品
- 处理器形态：EP、RC

## 问题现象描述

在执行播音业务时，不能正常播音，并产生报错，返回错误码0xa0168009。

```bash
sample_comm_audio_start_ao: hi_mpi_ao_set_pub_attr(2) failed with 0xa0168009!
```

## 可能原因

没有插入播音相关的ko。

## 处理步骤

1. lsmod检查ko的插入情况。
2. 执行以下命令重新插入ao相关的ko。

    ```bash
    insmod /var/davinci/driver/drv_ao.ko
    ```

3. 再次执行播音命令。
