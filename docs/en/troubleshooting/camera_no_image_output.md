# No Image Output

## Application Scenario

- Service Scenario: camera image output
- Applicable processor:  Atlas 200I/500 A2 inference products
- Processor forms: EP and RC

## Symptom

Sensor data fails to be obtained, and the ISP fails to be created. Information similar to the following is displayed in the log:

```text
[imx477_sensor_ctl.c:121][sensor]viPipe:0, addr:100, data:0
[imx477_sensor_ctl.c:149][sensor]I2C WRITER DATA error!
[imx477_sensor_ctl.c:209][sensor]imx477 vipipe:0, i2caddr:256,i2cval
```

## Possible Cause

The sensor is not properly installed, or the sensor model is inconsistent with the expected settings.

## Solution

1. Remove and then insert the sensor, or check the corresponding configuration.
2. If the fault persists after step 1 is performed, replace the sensor with a new one.
3. Start the camera again.
