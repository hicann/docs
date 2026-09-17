# Inconsistent Dispensation Before And After The Operator Input Arg

## Analysis result

If the  **info.txt**  file contains the following analysis conclusion, the args error occurs:

```text
"**********************Root cause conclusion******************"
If the arguments are inconsistent before and after operator execution, memory access may be out of bounds. You are advised to use the memory error detection model to locate the fault.
```

In the  **info.txt**  file, the following information is displayed in  **4. Operator Input/Output Memory**:

```text
****************4. Operator Input/Output Memory*******************
input[0] addr: 0x124080042000 end_addr:0x124080042100 size: 0x100
input[1] addr: 0x124080022000 end_addr:0x124080022008 size: 0x8
input[2] addr: 0x0 end_addr:0x4 size: 0x4
output[0] addr: 0x0 end_addr:0x8 size: 0x8
workspace_bytes:0

args before execute: [[0x124080042000, 0x124080022000, 0x124080032000, 0x124080052000, 0x1240003e5070, 0x124080010000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x124080010000, 0x100000001, 0x100000040, 0x100000002]]
args after  execute: [[0x124080042000, 0x124080022000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x124080010000, 0x100000001, 0x100000040, 0x100000002]]
```

## Fault root causes

Check the values of  **args before execute**  and  **args after execute**  in the preceding information. It is found that the values of  **args**  before and after the dispensation are different.  **args**  is the input parameter of the operator kernel. The first several digits indicate the addresses of the input, output, workspace, and tiling\_gm \(memory for storing tiling data\). If the value of  **args**  is incorrect, an AI Core error may occur.

## Solution

If the preceding information is displayed, perform the following operations:

Enable the memory corruption detection function of the operator \(for details, see the following description\), use the asys to rerun services to collect fault information, and use the  [https://gitee.com/ascend](https://gitee.com/ascend)  to submit an issue for help.

**Inference scenario**: Perform ATC model conversion and enable the memory detection function by using the  **--op\_debug\_config**  debugging option.

Assume that the configuration file for enabling global memory detection is  **_gm\_debug.cfg_**. The file configuration content is as follows:

```text
op_debug_config=ccec_O0,ccec_g,oom
```

Upload the file to any directory \(for example,  **_$HOME/module_**\) on the server where ATC is located, an example is as follows:

```text
--op_debug_config=$HOME/module/gm_debug.cfg
```

**Training scenario**: Modify the NPU's default configuration item  **npu.global\_options\(\).op\_debug\_config**  to enable memory detection.

You need to modify the default configuration items and set the global configuration items before initializing the NPU device. The following is an example:

```python
import npu_device as npu
npu.global_options().op_debug_config="/root/gm_debug.cfg"
npu.open().as_default()
```

The  **gm\_debug.cfg**  file contains the following information:

```text
op_debug_config = ccec_O0,ccec_g,oom
```
