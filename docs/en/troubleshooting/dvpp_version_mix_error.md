# Application Reports an Error and Exits Due to Mixed Use of DVPP APIs of Two Versions

## Symptom

Use the media data processing V1 API \(with  **acldvpp**  as the start of the API name\) to create one channel, and use the media data processing V2 API \(with  **hi\_mpi**  as the start of the API name\) to create another channel. The latter one fails to be created.

A log example is as follows:

```text
acl and himpi mode is incompatible, please check! used channel-num: 10
```

## Possible Cause

The media data processing V1 API \(with  **acldvpp**  as the start of the API name\) and the media data processing V2 API \(with  **hi\_mpi**  as the start of the API name\) are not compatible with each other. Only one version is allowed for multiple processes or threads. Otherwise, the DVPP blocks the request, reports an error, and exits the application.

## Solution

Check the service process and ensure there is no mixed use of V1 and V2 APIs. Mixed use is not supported for either multi-process or multi-thread scenarios.
