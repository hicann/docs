# VDEC视频帧解码失败不触发回调函数

## 问题现象描述

用户输入码流给VDEC解码，某些帧或所有帧都没有触发回调函数，用户收不到解码结果。

## 可能原因

码流中某些帧是坏帧，导致语法解析不出这些帧的含义，或者解码这些帧失败，从而不调用回调函数。

## 处理步骤

针对分析的可能原因，请参考以下步骤进行处理：

1. 查看日志中是否有[VDEC视频解码丢帧/丢包](vdec_decode_frame_drop.md)中的日志报错信息，若有，则是因为异常帧解码失败导致没有回调。
2. 若没有[VDEC视频解码丢帧/丢包](vdec_decode_frame_drop.md)中的日志报错信息，则调整DVPP模块或全局日志级别为info，查看下述三条日志打印的总次数是否和输入的帧数相等。

    - <u>（1）"The queue is empty, so call the non-intelligent pointer callback interface."</u>
    - <u>（2）"The queue is not empty, so call the smart pointer callback interface."</u>
    - <u>（3）"The queue is not empty, but hiai\_data\_sp is nullptr."</u>

    生成上述3种日志信息的场景如下：

    - 未使用hiai\_data\_sp，成功解码返回，打印（1）日志，然后调用用户注册的回调函数。
    - 每一帧对应设置一个hiai\_data\_sp，成功解码返回，打印（2）日志，然后调用用户注册的回调函数。
    - N帧对应设置一个hiai\_data\_sp，第1帧成功解码返回，打印（2）日志，然后调用用户注册的回调函数；其他N-1帧，成功解码后打印（3）日志信息，并调用用户注册的回调函数。

    不论上述场景中哪一种，均会调用用户注册的回调函数，即只要调用一次用户回调函数就说明解码返回一帧。所以上述三条日志出现的次数总和与用户输入总帧数相等，则说明无解码丢帧，用户需排查自身接收解码结果的统计是否有误。
