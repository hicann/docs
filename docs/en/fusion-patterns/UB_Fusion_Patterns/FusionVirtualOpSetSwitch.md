# FusionVirtualOpSetSwitch

## Description

Controls split_n axis and split_c_to_n axis optimization. Adds the `no_task` attribute to the Split operators (SplitD/SplitVD) that meet the constraints. Skips operator build by concatenating the N axis, thereby improving performance. If the input memory of the Split operators is large, you can choose to disable this fusion pattern.

This special fusion pattern is not written into `fusion_result.json` when it takes effect.

Compares the `_no_task` attribute of SplitD/SplitVD in the current graph `ge_onnx_****PreRunAfterOptimizeGraphBeforeBuild.pbtxt` with that in the previous graph `ge*.pbtxt`. A change from `0` to `1` means the pass has taken effect.

>[!NOTE]
> To generate a .pbtxt file, set the following environment variables before training or inference. For more information about environment variables, see [Environment Variables] <!-- (https://gitcode.com/cann/docs/blob/master/docs/en/env-vars/README.md). -->
> 
> - DUMP_GE_GRAPH=2 // Dumps the graph description of each phase in the entire process to a file. This environment variable specifies the amount of graph content to dump.
> 
> - DUMP_GRAPH_LEVEL=2 // Dumps the graph description of each phase in the entire graph compilation process to a file. This environment variable controls the number of flushed graphs.

## Constraints

**Common constraints**

- Dynamic scenarios are not supported.
- This fusion pattern does not take effect when the attribute lists of `_input_memory_type` and `_output_memory_type` of SplitD/SplitVD contain the value `RT_MEMORY_L1(65536)` or `RT_MEMORY_L2(131072)`.
- The following inputs are not supported:
    - Data -> TransData/Reshape -> Split structure.
    - The peer input nodes of SplitD/SplitVD already have the `no_task` attribute.
    - The peer input nodes of SplitD/SplitVD already have the `atomic_output_index` attribute, and the attribute value is not empty.
    - The peer input nodes of SplitD/SplitVD are Const.

- The following outputs are not supported:
    - The peer output nodes of SplitD/SplitVD are NetOutput, HcomBroadcast, HcomAllGather, HcomAllReduce, HcomReduceScatter, HcomReduce, SplitD, or SplitVD.
    - The peer output nodes of SplitD/SplitVD already have the `no_task` attribute.
    - The peer output nodes of SplitD/SplitVD are not TVM operators (the `imply_type` attribute is not `1`).
    - The `_fusion_virtual_op` attribute of the peer output nodes of SplitD/SplitVD is not empty.
    - The `continuous_input` attribute of the peer output nodes of SplitD/SplitVD is `true`.
    - The peer output nodes of SplitD/SplitVD already have the `atomic_output_index` attribute and the value is not empty.

**Special constraints for split_n axis optimization:**

- This fusion pattern takes effect when the `split_dim` attribute is `0`. In the following special cases, the original `split_dim` is converted. The `split_dim` attribute is subject to the converted value.
- When the data format is converted from ND to NZ for SplitD/SplitVD and the shape dimension is 2, the AI processors convert `split_dim` (0 to 1 or 1 to 0).
- For SplitD/SplitVD in all data formats, if the original `split_dim` is a negative value, the AI processor converts it. The converted `split_dim` value is equal to the original `split_dim` value plus the dimension value of the shape. For example, if `split_dim` is `-2`, the shape is `[1,32,32,1]`, and the dimension of the shape is 4, the converted `split_dim` value is `2`.

**Special constraints for split_c_to_n axis optimization:**

If the `split_dim` attribute of SplitD/SplitVD is `1`, the `origin shape` dimension of SplitD/SplitVD is greater than or equal to `2`, and the N axis is `1` (`shape[0]=1`), the fusion pattern takes effect only when one of the following conditions is met:

>[!NOTE]
>If the original `split_dim` is a negative value, the AI processor converts it. The converted `split_dim` value is equal to the original `split_dim` value plus the dimension value of the shape. For example, if `split_dim` is `-2`, the shape is `[1,32,32,1]`, and the dimension of the shape is 4, the converted `split_dim` value is `2`.

- The original format is ND, the current format is NZ, and the `origin shape` dimension is greater than or equal to 4.
- When the original format is NCHW and the current format is NC1HWC0, the C axis (`shape[1]`) must be aligned according to the data type: fp16 aligned to 16 bits, int8 aligned to 32 bits, and int4 aligned to 64 bits.
- The original format is the same as the current format.
