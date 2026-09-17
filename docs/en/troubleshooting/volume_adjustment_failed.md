# Volume Adjustment Failure

## Application Scenario

- Service scenario: volume adjustment during audio playing or recording
- Applicable processor:  Atlas 200I/500 A2 inference products
- Processor forms: EP and RC

## Symptom

The volume does not change when you adjust the volume during audio playing or recording. As a result, the volume adjustment fails.

## Possible Cause

1. The adjusted volume is out of range. Currently, the volume of the left and right audio channels for audio playing and recording can be adjusted separately, and the value of the volume control parameter ranges from 0 to 127. If the volume exceeds the range, an error is reported and the volume adjustment fails.

    ```text
    HI_ACODEC_SET_ADCL_VOLUME failed!
    ```

2. The volume adjustment API for recording is incorrectly used during audio playing, or the volume adjustment API for audio playing is incorrectly used during recording.

## Solution

1. Check whether the volume adjustment range of the Audio API is correctly configured.
2. Ensure that the DAC-related API is called to adjust the volume during audio playing and the ADC-related API is called to adjust the volume during recording.
3. Run the audio playing or recording command again.
