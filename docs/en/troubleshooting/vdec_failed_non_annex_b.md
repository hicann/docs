# VDEC Failure Due to Non-annex-B Streams

## Symptom

Decoding failed.

A log example is as follows:

```text
pid 0 usr chn 0 device 0 video format unsupport at event chn 0
```

Or

```text
pid 0 usr chn 0 device 0 chn 0, input stream error, can't decode, report to user
```

## Possible Cause

VDEC supports only raw streams in annex-B format. Raw streams in other formats \(such as AVCC\) are not supported.

## Solution

Raw streams in annex-B format start with  **0x00000001**  \(H.264\). You can use a third-party tool to open the streams, view the streams in hexadecimal format, and check the stream format.

![](figures/image_0000001927835353.png)
