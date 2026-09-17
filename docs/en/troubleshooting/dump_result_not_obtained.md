# Failure in Obtaining Dump Result

## Symptom

The log shows that the dump function is correctly configured, but no dump result is found in the path. The log contains the following keywords:

```text
[INFO] ASCENDCL ****** "HandleDumpConfig end in HandleDumpConfig."
[INFO] ASCENDCL ****** "set HandleDumpConfig success in aclInit"
```

## Possible Cause

The model name configured in the dump file does not match the actual model name.

## Solution

To rectify the fault, perform the following steps:

Check the validity of the dump configuration file  **acl.json**. For example, check if  **model\_name**  is correctly configured. The following is an example:

```json
{
    "dump":{
        "dump_list":[
             {
                "model_name":"ResNet-50",
                  "layer":[
                             "conv1conv1_relu"
                          ]
             },
             {
                "model_name":"mxnet-model"
             }
        ],
        "dump_mode":"output",
        "dump_path":"/home/test/output/dump"
    }
}
```

 Run the  ATC  command to generate a .json file. In the .json file, search for the  **name**  field. The model name is outside the  **graph**  field and the operator name is inside the  **graph**  field.
