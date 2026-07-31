# 昇腾虚拟化实例场景下VDEC通道数量达到上限，无法创建通道

## 问题现象描述

创建一定数量的通道后，无法继续创建vdec通道。

Device日志示例如下：

```bash
pid 0 usr chn 0 device 0 chn 0 vf_id 1 has created chn num(27) is full, max chn num = 27
```

>**说明：** 
>EP模式下，运行解码进程后，登录Host，在有读、写、执行权限的目录下执行**msnpureport -a**命令，可导出Device的日志信息。
>RC模式下，登录板端环境，执行**cat /proc/umap/vdec**命令，可导出解码相关信息。

## 原因分析

不同的算力模板有不同的总通道数上限，超过通道上限就无法继续创建通道。

## 解决方法

1. 根据所使用的算力模板查询该模板中的VDEC资源信息。

    **表 1** **昇腾虚拟化实例配置表**（Atlas 推理系列产品）

    | name（切分名称） | 切分规格 | AIC核数（aicore数量配置） | 内存容量(GB) | AICPU（device_aicpu数量配置） | VPC | JPEGD | JPEGE | VENC | VDEC |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | 总资源 | 1 | 8 | 等于通过dsmi_get_memory_info接口获取的memory_size取值。 | 7 | 12 | 16 | 8 | 3 | 12 |
    | vir04 | 1/2 | 4 | memory_size/2 | 4 | 6 | 8 | 4 | 2 | 6 |
    | vir04_3c | 1/2 | 4 | memory_size/2 | 3 | 6 | 8 | 4 | 1 | 6 |
    | vir04_4c_dvpp | 1/2 | 4 | memory_size/2 | 4 | 12 | 16 | 8 | 3 | 12 |
    | vir04_3c_ndvpp | 1/2 | 4 | memory_size/2 | 3 | 0 | 0 | 0 | 0 | 0 |
    | vir02 | 1/4 | 2 | memory_size/4 | 2 | 3 | 4 | 2 | 1 | 3 |
    | vir02_1c | 1/4 | 2 | memory_size/4 | 1 | 3 | 4 | 2 | 0 | 3 |
    | vir01 | 1/8 | 1 | memory_size/8 | 1 | 1 | 2 | 1 | 0 | 1 |

2. 根据VDEC资源信息计算通道总数上限。

    解码通道总数上限=\(JPEGD + VDEC\) / \(16 + 12\) \* 256.

    例如vir01模板，解码通道总数上限=\(2 + 1\) / \(16 + 12\) \* 256 = 27
