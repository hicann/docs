# Camera一直丢帧，无图片dump出来

## 适用场景

- 业务场景：Camera出图，同时dump raw和yuv图片
- 适用处理器：Atlas 200I/500 A2 推理产品
- 处理器形态：EP、RC

## 问题现象描述

反复刷屏打印：pipe  _x_  chn  _x_  get buffer fail,hi\_size  _xxxx_!

## 可能原因

申请的pipe depth小于或者等于dump raw depth，导致无多余buffer送给后端chn。

## 处理步骤

1. 查看相关depth数，修改相关属性，确保pipe depth + chn attr depth - dump\_attr depth大于零即可。
2. 再次启动Camera。
