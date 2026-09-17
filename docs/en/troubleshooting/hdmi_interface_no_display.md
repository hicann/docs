# No Display over the HDMI

## Application Scenario

- Service scenario: display over the HDMI
- Applicable processor:  Atlas 200I/500 A2 inference products
- Processor forms: EP and RC

## Symptom

When the VO module and HDMI display signals, the HDMI displays no signal and no error log is reported.

## Possible Cause

The possible causes are as follows:

- At the end of the test case,  **hi\_mpi\_hdmi\_start**  is not called to enable a specific HDMI, or the HDMI is incorrectly enabled.
- The HDMI attributes and information frame parameters are incorrectly set in the test case.
- The monitor does not support the current resolution.

## Solution

1. Check whether  **hi\_mpi\_hdmi\_start**  is called to enable a specific HDMI or whether the HDMI is incorrectly enabled.
2. Check parameters in the test case. For example, check whether  **video\_format**  under  **avi infoframe**,  **timing\_mode**  under  **hi\_hdmi\_attr**, and  **pix\_clk**  are consistent with outputs of the VO module.
3. Read the EDID information of the current monitor to check whether the monitor supports the current resolution. If not, replace it with a monitor that supports the resolution.
4. Execute the test case that displays signals over the HDMI again.
