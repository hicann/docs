# Manually Collecting Operator Compilation Information \(.o and .json Files\)

Search for the operator .json and .o files in the CANN software installation path, which is  **/usr/local/Ascend/cann**  by default. If no file is found, search for them in the cache directory, which is  **_$\{HOME\}_/atc\_data**  by default. If the  **ASCEND\_CACHE\_PATH**  environment variable is configured, search for the files in the path specified by this environment variable. For details about the environment variables and their restrictions, see  [Environment Variables](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/maintenref/envvar/envref_07_0001.html).

When searching for the operator .json file, use the kernel name as the keyword. If the kernel name contains  **\_mix\_aic**  or  **\_mix\_aiv**, delete them during the search. For example, if the kernel name is  **_xxx_\_mix\_aic\__kernel0_**, use  **_xxx_\__kernel0_**  as the keyword. If the kernel name is  **_xxx_\__tilingkey_\_mix\_aic**, use  **_xxx_\__tilingkey_**  as the keyword. Search for the file in the  **/usr/local/Ascend/cann**  directory. The following is a command example:

```bash
# Delete _mix_aic or _mix_aiv. Replace xxxxxx with the actual kernel name.
kernel_name=xxxxxx
kernel_name=$(echo $kernel_name | sed 's/_mix_aic//g' | sed 's/_mix_aiv//g' )
# Search for the .json file.
find /usr/local/Ascend/cann -name "*.json"|xargs grep -rn $kernel_name

# Copy the .json file to the aic_err_info directory.
cp  xxxxxx.json aic_err_info/
```

When searching for the operator .o file, use the value of the  **binFileName**  field \(name of the .o file\) in the operator .json file as the keyword. Search for the file in the  **/usr/local/Ascend/cann**  directory. The following is a command example:

```bash
# Locate the binFileName: xxxxxx in the .json file to get the .o file name.
find /usr/local/Ascend/cann -name xxxxxx.o

# Copy the .o file to the aic_err_info directory.
cp  xxxxxx.o aic_err_info/
```
