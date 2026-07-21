# 不支持的协议字段0x31导致JPEGD图片解码结果异常

## 问题现象描述

JPEGD图片解码的结果数据都是0，查看日志，有报错“**Unsupported marker type 0x31**”，日志示例如下：

```bash
[ERROR] KERNEL(1234,sklogd):2023-10-27-00:39:44.324.726 [701889.574406]  [dvpp] [dvpp_check_decode_status 954] decode unfinish, image height:1440, the decoded line num:1424
[ERROR] KERNEL(1234,sklogd):2023-10-27-00:39:44.324.752 [701889.574946]  [dvpp] [dvpp_jpegd_engine_proc 412] jpegd_done_config failed! errcode:-1, engine id:1
[ERROR] KERNEL(1234,sklogd):2023-10-27-00:39:44.324.777 [701889.575016]  [dvpp] [jpegd_res_off 653] engine 1 decode error, no need to turn off decoder clock
[ERROR] KERNEL(1234,sklogd):2023-10-27-00:39:44.324.804 [701889.575020]  [dvpp] [dvpp_ioctl_jpegd 794] call proc failed:-1, engine_id:1
[ERROR] DVPP(14577,graph_1):2023-10-27-00:39:44.411.853 [JPEGD] [SoftwareProcess:267] [T87] tjDecompressToYUV2 fail: Unsupported marker type 0x31
[ERROR] DVPP(14577,graph_1):2023-10-27-00:39:44.411.977 [JPEGD] [Process:312] [T87] Jpeg hardware and software decode are both failed!
```

## 原因分析

存在JPEGD图片解码模块不支持的协议字段0x31，导致硬解和软解都失败，因此没有输出解码数据，即内存中数据都是默认值0。

以下是常用标记的标记代码和表示的意义：

| 标记 | 标记代码 | 意义 |
| --- | --- | --- |
| SOI | 0xFFD8 | 图像开始 |
| APP0 | 0xFFE0 | 应用程序保留标记0 |
| DQT | 0xFFDB | 定义量化表 |
| SOF0 | 0xFFC0 | 帧图像开始 |
| DHT | 0xFFC4 | 定义哈夫曼表 |
| SOS | 0xFFDA | 扫描开始 |
| EOI | 0xFFD9 | 图像结束 |

## 解决方法

1. 建议用户使用第三方工具打开图片码流，检查码流中的标记。
2. 如果存在0x31的标记，则更换图片，重新解码。
