# Incorrect Audio Pitch and Speed

## Application Scenario

- Service scenario: audio playing
- Applicable processor:  Atlas 200I/500 A2 inference products
- Processor forms: EP and RC

## Symptom

After the play command is executed, the PCM audio file is successfully read. The music is played, but the speed becomes slow or fast, and the corresponding pitch becomes low or high.

The following figure shows the monophonic sine wave with a frequency of 1 kHz of the original PCM file.

![](figures/image_0000001927915797.png)

After the audio is played, the frequency becomes 2 kHz, with a faster speed and higher pitch.

![](figures/image_0000001927835417.png)

## Possible Cause

The format of the audio playing parameter is inconsistent with that of the PCM audio file. The PCM file is raw data without a file header. Therefore, information, such as the audio channel, bit width, and sampling rate, cannot be obtained from the data alone. For example, if a PCM file is a single-channel file but is read in dual-channel mode, the playback speed is twice the normal speed and the corresponding pitch increases.

## Solution

1. Check whether the parameters such as the audio channel and bit width in the Audio API are the same as those in the PCM file.
2. Modify parameters such as the bit width, sampling rate, and number of audio channels, and set their attributes.
3. Run the audio playing command again.
