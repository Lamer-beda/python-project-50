def to_str(value):
    if isinstance(value, (list, dict)):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def make_plain_result_item(item, path=''):
    current_key = item.get('key')
    current_path = f"{path}.{current_key}" if path else current_key
    action = item.get('action_type')
    new_value = to_str(item.get('value'))
    old_value = to_str(item.get('new_value'))

    if action == 'added':
        return f"Property '{current_path}' was added with value: {new_value}"
    if action == 'removed':
        return f"Property '{current_path}' was removed"
    if action == 'changed':
        return (
            f"Property '{current_path}' was updated. "
            f"From {new_value} to {old_value}"
        )
    if action == 'children':
        children = item.get('value')
        return make_plain_result(children, current_path)
    return None


def make_plain_result(diff, path=''):
    result = []
    for item in diff:
        formatted_item = make_plain_result_item(item, path)
        if formatted_item is not None:
            result.append(formatted_item)

    return '\n'.join(result)


def format_diff_plain(data):
    return make_plain_result(data)
