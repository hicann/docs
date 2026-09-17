# JPEGD Result Exceptions Due to Unsupported Protocol Field 0x31

## Symptom

The JPEGD image decoding results are all 0s. The log has the error message "**Unsupported marker type 0x31**", as shown in the example below:

```text
[ERROR] KERNEL(1234,sklogd):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [701889.574406]  [dvpp] [dvpp_check_decode_status 954] decode unfinish, image height:1440, the decoded line num:1424
[ERROR] KERNEL(1234,sklogd):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [701889.574946]  [dvpp] [dvpp_jpegd_engine_proc 412] jpegd_done_config failed! errcode:-1, engine id:1
[ERROR] KERNEL(1234,sklogd):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [701889.575016]  [dvpp] [jpegd_res_off 653] engine 1 decode error, no need to turn off decoder clock
[ERROR] KERNEL(1234,sklogd):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [701889.575020]  [dvpp] [dvpp_ioctl_jpegd 794] call proc failed:-1, engine_id:1
[ERROR] DVPP(14577,graph_1):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [JPEGD] [SoftwareProcess:267] [T87] tjDecompressToYUV2 fail: Unsupported marker type 0x31
[ERROR] DVPP(14577,graph_1):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [JPEGD] [Process:312] [T87] Jpeg hardware and software decode are both failed!
```

## Possible Cause

The unsupported protocol field  **0x31**  exists, so both hardware decoding and software decoding fail, without outputting decoded data. That is, values of data in the memory are all 0s.

The following table lists some commonly used markers and their meanings.

| Marker | Marker Code | Meaning |
| --- | --- | --- |
| SOI | 0xFFD8 | Start of an image |
| APP0 | 0xFFE0 | Reserved marker 0 for applications |
| DQT | 0xFFDB | Quantization table definition |
| SOF0 | 0xFFC0 | Start of a frame image |
| DHT | 0xFFC4 | Huffman table definition |
| SOS | 0xFFDA | Start of scanning |
| EOI | 0xFFD9 | End of an image |

## Solution

1. Use a third-party tool to view the image stream and check markers in the stream.
2. If a 0x31 marker exists, replace the image and decode the image again.
