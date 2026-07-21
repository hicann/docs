# 手动收集算子编译信息（算子.o和.json文件）

**先从CANN软件安装路径下查找算子.json和.o文件**，CANN软件默认安装路径为/usr/local/Ascend/cann，**如果找不到，再从缓存目录下查找**，默认为$\{HOME\}/atc\_data目录，如果配置了ASCEND\_CACHE\_PATH环境变量，则从该环境变量配置的路径下查找。关于环境变量的详细说明及约束，请参见[《环境变量参考》](https://hiascend.com/document/redirect/CannCommunityEnvRef)。

**查找算子.json文件时**，以日志中的kernel\_name为关键字，但如果kernel\_name中包含\_mix\_aic或\_mix\_aiv，在搜索时需剔除\_mix\_aic或\_mix\_aiv，例如kernel\_name为_xxx_\_mix\_aic\__kernel0_，在搜索时需使用_xxx_\__kernel0_关键字来搜索；再例如kernel\_name为_xxx_\__tilingkey_\_mix\_aic，在搜索时需以关键字_xxx_\__tilingkey_来搜索。查找命令示例如下，在/usr/local/Ascend/cann目录下查找：

```bash
# 剔除_mix_aic或_mix_aiv，其中xxxxxx需替换为实际的kernel_name
kernel_name=xxxxxx
kernel_name=$(echo $kernel_name | sed 's/_mix_aic//g' | sed 's/_mix_aiv//g' )
# 找到对应的json文件
find /usr/local/Ascend/cann -name "*.json"|xargs grep -rn $kernel_name

# 将对应的.json文件拷贝到aic_err_info目录中
cp  xxxxxx.json aic_err_info/
```

**查找算子.o文件时**，以算子.json文件中的binFileName字段值（该值为.o文件名）为关键字搜索。查找命令示例如下，在/usr/local/Ascend/cann目录下查找：

```bash
# 在json文件中查看"binFileName":xxxxxx获取到.o文件名
find /usr/local/Ascend/cann -name xxxxxx.o

# 将对应的.o文件拷贝到aic_err_info目录中
cp  xxxxxx.o aic_err_info/
```
