# NVR场景语音对讲

本节介绍NVR音频业务处理的典型流程、关键接口及注意事项。

NVR，全称Network Video Recorder，即网络视频录像机，是网络视频系统的存储转发部分，NVR与网络摄像机协同工作，完成音频&视频的录像、存储及转发功能，同时，NVR具备本地人机交互界面、视频解码、视频显示及语音对讲功能。

## NVR音频场景说明

**本章节描述NVR音频业务（语音对讲功能）的接口调用流程。**在语音对讲功能中，包括媒体数据处理系统初始化&去初始化、[接收IP Camera发送的语音并播放声音](#section3741201132710)、[录制声音并向IP Camera发送语音](#section86391611152718)，涉及的模块包括公共模块、音频输入模块（AI）,音频编码模块（AENC）、音频输出模块（AO）、音频解码模块（ADEC）。

![](figures/NVR音频场景说明.png)

<a id="section3741201132710"></a>

## 接收IP Camera发送的语音并播放声音

**图 1** **接收IP Camera发送的语音并播放声音**  
![](figures/接收IP-Camera发送的语音并播放声音.png "接收IP-Camera发送的语音并播放声音")

接口调用流程说明如下：

1. 调用hi\_mpi\_adec\_create\_chn接口**创建音频解码通道**。
2. **启用AO音频输出设备和通道**：
    1. 调用hi\_mpi\_ao\_set\_pub\_attr接口设置AO设备属性。
    2. 调用hi\_mpi\_ao\_enable接口启动AO设备。
    3. 调用hi\_mpi\_ao\_enable\_chn接口启动AO通道
    4. 调用hi\_mpi\_ao\_enable\_resample接口启用AO重采样功能。

        由于AO的采样率固定为48kHz，G.711a、G.711u协议的采样率仅支持8kHz，因此需启用重采样功能；而48kHz在AAC协议采样率支持的范围内，因此使用AAC协议时，在AO时无需重采样。

3. 调用hi\_mpi\_sys\_bind接口**绑定ADEC与AO**。

    | ADEC设备ID | ADEC通道号 | AO设备ID | AO通道号 |
| --- | --- | --- | --- |
| 0 | 0 | 2 | 0 |
| 0 | 1 | 3 | 0 |

4. 循环调用hi\_mpi\_adec\_send\_stream接口将每一帧待解码音频数据发送给解码器进行**解码**。

    解码后的音频数据，根据第3步中的绑定关系，被自动发送到对应的AO设备，用于音频播放。

5. 音频播放完成后，在退出流程中，先调用hi\_mpi\_sys\_unbind接口**解绑ADEC与AO**，再依次调用hi\_mpi\_ao\_disable\_resample接口禁用AO重采样功能、调用hi\_mpi\_ao\_disable\_chn接口禁用AO通道、调用hi\_mpi\_ao\_disable接口禁用AO设备，最后调用hi\_mpi\_adec\_destroy\_chn接口进行销毁ADEC通道。

<a id="section86391611152718"></a>

## 录制声音并向IP Camera发送语音

**图 2** **录制声音并向IP Camera发送语音**  
![](figures/录制声音并向IP-Camera发送语音.png "录制声音并向IP-Camera发送语音")

接口调用流程说明如下：

1. **启用AI音频输入设备和通道**：
    1. 调用hi\_mpi\_ai\_set\_pub\_attr接口设置AI设备属性。
    2. 调用hi\_mpi\_ai\_enable接口启动AI设备。
    3. 调用hi\_mpi\_ai\_set\_chn\_attr接口设置AI通道属性。
    4. 调用hi\_mpi\_ai\_enable\_chn接口启动AI通道。
    5. 调用hi\_mpi\_ai\_enable\_resample接口启用AI重采样功能。

        由于AI的采样率固定为48kHz，G.711a、G.711u协议的采样率仅支持8kHz，因此需启用重采样功能；而48kHz在AAC协议采样率支持的范围内，因此使用AAC协议时，在AI时无需重采样。

2. 调用hi\_mpi\_aenc\_create\_chn接口**创建音频编码通道**。
3. 调用hi\_mpi\_sys\_bind接口**绑定AI与AENC**。

    | AI设备ID | AI通道号 | AENC设备ID | AENC通道号 |
| --- | --- | --- | --- |
| 2 | 0 | 0 | 0 |

4. 循环调用hi\_mpi\_aenc\_get\_stream获取编码数据，编码数据使用完成后，及时调用hi\_mpi\_aenc\_release\_stream接口**释放编码数据**。

    经过AI设备获取到的音频数据，根据第3步中的绑定关系，被自动发送到对应的AENC通道进行编码，用于向IP Camera发送语音。

5. 发送语音完成后，在退出流程中，先调用hi\_mpi\_sys\_unbind接口**解绑AI与AENC**，再调用hi\_mpi\_aenc\_destroy\_chn接口进行销毁AENC通道，最后依次调用hi\_mpi\_ai\_disable\_resample接口禁用AI重采样功能、调用hi\_mpi\_ai\_disable\_chn接口禁用AI通道、调用hi\_mpi\_ai\_disable接口禁用AI设备。
