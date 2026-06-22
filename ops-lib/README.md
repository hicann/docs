# 算子库参考

- [简介](zh/简介.md)
- [基本概念](https://gitcode.com/cann/ops-math/blob/master/docs/zh/context/%E5%9F%BA%E6%9C%AC%E6%A6%82%E5%BF%B5.md)
<!-- npu="950,A3,910b,910,310p,310b" id1 -->
- [公共接口](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/aclnn/00_aclnn_api_list.md)
<!-- end id1 -->
<!-- npu="IPV350" id2 -->
- [公共接口（当前版本不支持）](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/aclnn/00_aclnn_api_list.md)
<!-- end id2 -->
<!-- npu="950,A3,910b,910,310p,310b" id3 -->
- [算子接口（aclnn）](zh/算子接口（aclnn）.md)
  - [Math类接口](zh/bookmap_aclnn_math.md)
  - [NN类接口](zh/bookmap_aclnn_nn.md)
  - [CV类接口](zh/bookmap_aclnn_cv.md)
  - [Transformer类接口](zh/bookmap_aclnn_trans.md)
<!-- end id3 -->
<!-- npu="IPV350" id4 -->
- [算子接口（aclnn）（当前版本不支持）](zh/算子接口（aclnn）.md)
  - [Math类接口](zh/bookmap_aclnn_math.md)
  - [NN类接口](zh/bookmap_aclnn_nn.md)
  - [CV类接口](zh/bookmap_aclnn_cv.md)
  - [Transformer类接口](zh/bookmap_aclnn_trans.md)
<!-- end id4 -->

<!-- npu="950,A3,910b" id5 -->
- [算子接口（torch\_extension）](zh/算子接口（torch_extension）.md)
  - [mhc_post](https://gitcode.com/cann/ops-transformer/blob/master/torch_extension/cann_ops_transformer/docs/zh/mhc_post.md)
  - [mhc_pre_sinkhorn](https://gitcode.com/cann/ops-transformer/blob/master/torch_extension/cann_ops_transformer/docs/zh/mhc_pre_sinkhorn.md)
  - [mega_moe](https://gitcode.com/cann/ops-transformer/blob/master/torch_extension/cann_ops_transformer/docs/zh/mega_moe.md)
  <!-- end id5 -->
- [Ascend IR算子规格说明](zh/Ascend-IR算子规格说明.md)
  - [规格简介](zh/规格简介.md)
  - [规格清单](zh/规格清单.md)
- [附录](zh/附录.md)
  <!-- npu="950,A3,910b,910,310p,310b" id6 -->
  - [aclnn开发接口](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/opdev/00_opdev_api_list.md)
  <!-- end id6 -->
  <!-- npu="IPV350" id7 -->
  - [aclnn开发接口（当前版本不支持）](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/opdev/00_opdev_api_list.md)
  <!-- end id7 -->
  - [基础张量操作接口](zh/基础张量操作接口.md)
    - [Cast](zh/L0_api/Cast.md)
    - [Contiguous](zh/L0_api/Contiguous.md)
    - [IsNullptr](zh/L0_api/IsNullptr.md)
    - [Pad](zh/L0_api/Pad.md)
    - [ReFormat](zh/L0_api/ReFormat.md)
    - [Reshape](zh/L0_api/Reshape.md)
    - [Slice](zh/L0_api/Slice.md)
    - [TransData](zh/L0_api/TransData.md)
    - [TransDataSpecial](zh/L0_api/TransDataSpecial.md)
    - [Transpose](zh/L0_api/Transpose.md)
    - [ViewCopy](zh/L0_api/ViewCopy.md)

  <!-- npu="950,910b,910,310p" id8 -->
  - [算子性能提升专题](zh/算子性能提升专题.md)
    - [使用静态Kernel提升算子执行性能](zh/使用静态Kernel提升算子执行性能.md)
      - [基本介绍](zh/基本介绍.md)
      - [环境准备](zh/环境准备.md)
      - [算子调优](zh/算子调优.md)
      <!-- end id8 -->

  - [FAQ](zh/FAQ.md)
    - [如何获取aclnn接口调用过程中的日志](zh/如何获取aclnn接口调用过程中的日志.md)
    - [常见算子故障案例](zh/常见算子故障案例.md)
