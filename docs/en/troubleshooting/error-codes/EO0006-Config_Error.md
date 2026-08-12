# EO0006 Config\_Error

## Symptom

The following is error format. The meanings of the placeholders %s in sequence are: configuration item value, configuration item name, configuration file, error cause.

```text
Value %s for configuration item %s in configuration file %s is invalid. Reason: %s
```

Error example:

```text
Value [invalid_layers1, invalid_layers2] for configuration item skip_fusion_layers in configuration file CONFIG_FILE is invalid. Reason: The layer in [invalid_layers1, invalid_layers2] does not exist in the graph.
```

## Solution

Check and rectify the error based on the error message. For details, see the documentation on the official website.
