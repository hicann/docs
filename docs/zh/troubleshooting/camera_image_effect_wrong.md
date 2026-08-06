# Camera出图效果不对

## 适用场景

- 业务场景：Camera出图，dump图片
- 适用处理器：Atlas 200I/500 A2 推理产品
- 处理器形态：EP、RC

## 问题现象描述

dump图片后发现图片为花图。

## 可能原因

检查pixel format和看图工具的pixel format是否一致，分辨率大小是否一致。

## 处理步骤

1. 检查pixel format和看图工具的pixel format，例如：YUV420，则选择对应420格式和分辨率。
2. 设置完成后，再次启动Camera。
