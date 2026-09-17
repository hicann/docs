# VDEC Performance Deterioration

## Symptom

The VDEC performance deteriorates, inferior to the released VDEC performance specifications. As a result, frame freezing occurs.

## Possible Cause

The possible causes are as follows:

- The video decoding callback function takes a long time, affecting the decoding performance.
- If the ratio of I-frames in the input stream is too large, the time required for decoding I-frames is longer than that for decoding P-frames, affecting the decoding performance.
- Abnormal frames exist in the input stream, which affects the decoding performance.

## Solution

To rectify the fault, perform the following steps:

1. Record the dotting test duration in the callback function and check whether the duration is too long.

    The maximum duration allowed by the callback function is related to the frame rate. The formula is as follows: Maximum duration = 1/Frame rate. For example, if the frame rate is 30 fps, the maximum duration is 1/30 fps = 0.033s.

2. Use a third-party tool to open the input stream and check whether the percentage of I-frames is too high. Generally, the GOP value is 30 \(that is, the I-frame interval is 30\). If the percentage of I-frames is too high, replace the stream for performance testing.
3. Use a third-party tool to open the input stream and check whether there are abnormal frames \(for example, artifacts or decoding errors\). If there are abnormal frames, the specifications are not met.
