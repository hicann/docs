# 算子库参考

- [简介](introduction.md)
- [头文件和库文件说明](header_and_library.md)
- [基本概念](https://gitcode.com/cann/ops-math/blob/master/docs/zh/context/%E5%9F%BA%E6%9C%AC%E6%A6%82%E5%BF%B5.md)
<!-- npu="950,A3,910b,910,310p,310b" id1 -->
- [公共接口](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/aclnn/00_aclnn_api_list.md)
<!-- end id1 -->
<!-- npu="IPV350" id2 -->
- [公共接口（当前版本不支持）](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/aclnn/00_aclnn_api_list.md)
<!-- end id2 -->
<!-- npu="950,A3,910b,910,310p,310b" id3 -->
- [算子接口（aclnn）](op_interface_aclnn.md)
  - [Math类接口](bookmap_aclnn_math.md)
  - [NN类接口](bookmap_aclnn_nn.md)
  - [CV类接口](bookmap_aclnn_cv.md)
  - [Transformer类接口](bookmap_aclnn_trans.md)
<!-- end id3 -->
<!-- npu="IPV350" id4 -->
- [算子接口（aclnn）（当前版本不支持）](op_interface_aclnn.md)
  - [Math类接口](bookmap_aclnn_math.md)
  - [NN类接口](bookmap_aclnn_nn.md)
  - [CV类接口](bookmap_aclnn_cv.md)
  - [Transformer类接口](bookmap_aclnn_trans.md)
<!-- end id4 -->
<!-- npu="950,A3,910b" id5 -->
- [算子接口（torch\_extension）](op_interface_torch_extension.md)
  - [mhc_post](https://gitcode.com/cann/ops-transformer/blob/master/torch_extension/cann_ops_transformer/docs/zh/mhc_post.md)
  - [mhc_pre_sinkhorn](https://gitcode.com/cann/ops-transformer/blob/master/torch_extension/cann_ops_transformer/docs/zh/mhc_pre_sinkhorn.md)
  - [mega_moe](https://gitcode.com/cann/ops-transformer/blob/master/torch_extension/cann_ops_transformer/docs/zh/mega_moe.md)
  <!-- end id5 -->
- [Ascend IR算子规格说明](ascendIR_op_specification.md)
  - [规格简介](ascendIR_spec_intro.md)
  - [规格清单](ascendIR_spec_list.md)
- [附录](appendix/appendix.md)
  <!-- npu="950,A3,910b,910,310p,310b" id6 -->
  - [nnopbase接口](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/opdev/00_opdev_api_list.md)
  <!-- end id6 -->
  <!-- npu="IPV350" id7 -->
  - [nnopbase接口（当前版本不支持）](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/opdev/00_opdev_api_list.md)
  <!-- end id7 -->
  <!-- npu="950,A3,910b,910,310p,310b" id9 -->
  - [op_common接口](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/op_common/00_op_common_list.md)
  <!-- end id9 -->
  <!-- npu="IPV350" id10 -->
  - [op_common接口（当前版本不支持）](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/op_common/00_op_common_list.md)
  <!-- end id10 -->
  <!-- npu="950,910b,910,310p" id8 -->
  - [算子性能提升专题](appendix/performance_improve_series.md)
    - [使用静态Kernel提升算子执行性能](appendix/performance_improve_by_staticKernel.md)
      - [基本介绍](appendix/staticKernel_introduction.md)
      - [环境准备](appendix/staticKernel_env_setup.md)
      - [算子调优](appendix/staticKernel_tuning.md)
      <!-- end id8 -->

  - [FAQ](appendix/FAQ.md)
    - [如何获取aclnn接口调用过程中的日志](appendix/faq_get_aclnn_call_logs.md)
    - [常见算子故障案例](appendix/faq_failure_cases.md)
