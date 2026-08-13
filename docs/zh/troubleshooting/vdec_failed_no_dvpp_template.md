# 昇腾虚拟化实例场景使用不含DVPP的算力模板时，创建VDEC通道失败

## 问题现象描述

无法创建VDEC视频解码通道。

Device日志示例如下：

```bash
pid 0 usr chn 0 device 0 chn 0 vf_id 1 has created chn num(0) is full, max chn num = 0
```

>**说明：** 
>EP模式下，运行解码进程后，登录Host，在有读、写、执行权限的目录下执行**msnpureport -a**命令，可导出Device的日志信息。
>RC模式下，登录板端环境，执行**cat /proc/umap/vdec**命令，可导出解码相关信息。

## 原因分析

从报错日志提示，可见昇腾虚拟化实例场景下最大通道数为0，怀疑算力模板中不含DVPP，因为若算力模板中不含DVPP，则表示该算力下无DVPP能力，才会导致创建VDEC通道失败，这种情况下的报错属于正常情况。

## 解决方法

1. 查询算力模板资源信息。

    Ascend EP形态下，登录Host，在有读、写、执行权限的目录下执行**msnpureport -a**命令导出Device的日志信息，按导出时间，进入对应时间戳的目录下，打开“module\_info\\dev-os-0\\dvpp\\dvpp\_proc.log”日志查看对应vf 1下有几个vdec core。

    Ascend RC形态下，登录板端环境，执行”cat /proc/umap/sys”，查看对应vf 1下有几个vdec core。

    如下图所示，vf 1下没有分配vdec core，才会导致创建VDEC通道失败，这种情况下的报错属于正常情况。

    ![](figures/image_vf1.png)

2. 若需要使用DVPP能力，可使用含DVPP能力的算力模板，算力模板信息如下所示。

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

    >**说明：** 
    >Atlas 推理系列产品的2P场景下，p0对应的算力模板名称如上表所示，p1对应的算力模板名称均多了p1的标记，比如：p1\_vir04。
