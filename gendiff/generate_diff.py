import json
import yaml

def generate_diff(file_path1, file_path2, format='stylish'):
    # Load JSON or YAML files
    with open(file_path1) as f1, open(file_path2) as f2:
        if file_path1.endswith('.json'):
            data1 = json.load(f1)
            data2 = json.load(f2)
        else:
            data1 = yaml.safe_load(f1)
            data2 = yaml.safe_load(f2)

    # Generate the diff
    diff = {}
    keys = set(data1.keys()).union(set(data2.keys()))
    for key in sorted(keys):
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff[key] = data1[key]
            else:
                diff[f"- {key}"] = data1[key]
                diff[f"+ {key}"] = data2[key]
        elif key in data1:
            diff[f"- {key}"] = data1[key]
        else:
            diff[f"+ {key}"] = data2[key]

    if format == 'stylish':
        return json.dumps(diff, indent=4).replace('"', '').replace(',', '')
    elif format == 'txt':
        return '\n'.join(f'{k}: {v}' for k, v in diff.items())
    elif format == 'yaml':
        return yaml.dump(diff, default_flow_style=False)

    return json.dumps(diff, indent=4)

