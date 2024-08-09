SEPARATOR = " "
ADD = '+ '
DELETE = '- '
NONE = '  '
DEFAULT_INDENT = 4


def to_str(value, depth=1):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        indent = SEPARATOR * ((depth * DEFAULT_INDENT - 2) + DEFAULT_INDENT)
        lines = []
        for key, inner_value in value.items():
            formatted_value = to_str(
                inner_value,
                depth + 1
            )
            lines.append(f"{indent}{NONE}{key}: {formatted_value}")
        formatted_string = '\n'.join(lines)
        end_indent = SEPARATOR * depth * DEFAULT_INDENT
        return f"{{\n{formatted_string}\n{end_indent}}}"
    return f"{value}"


def make_stylish_result(diff, depth=1):
    indent = SEPARATOR * (depth * DEFAULT_INDENT - 2)
    lines = []
    for item in diff:
        key_name = item['key']
        old_value = to_str(item.get("value"), depth)
        new_value = to_str(item.get("new_value"), depth)
        action = item["action_type"]
        match action:
            case "not_changed":
                current_value = to_str(item.get("value"), depth)
                lines.append(f"{indent}{NONE}{key_name}: {current_value}")
            case "changed":
                lines.append(f"{indent}{DELETE}{key_name}: {old_value}")
                lines.append(f"{indent}{ADD}{key_name}: {new_value}")
            case "removed":
                lines.append(f"{indent}{DELETE}{key_name}: {old_value}")
            case "added":
                lines.append(f"{indent}{ADD}{key_name}: {old_value}")
            case "children":
                children = make_stylish_result(
                    item.get("value"), depth + 1
                )
                lines.append(f"{indent}{NONE}{key_name}: {children}")

    formatted_string = '\n'.join(lines)
    end_indent = SEPARATOR * (depth * DEFAULT_INDENT - 4)

    return f"{{\n{formatted_string}\n{end_indent}}}"


def format_diff_stylish(data):
    return make_stylish_result(data)
