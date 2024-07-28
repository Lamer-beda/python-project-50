from gendiff.formatter.make_str import make_str

REPLACER = ' '
SPACES_COUNT = 4


def stringify(value, depth):
    if not isinstance(value, dict):
        return make_str(value)

    lines = ['{']
    for key, val in value.items():
        formatted_value = stringify(val, depth + SPACES_COUNT)
        if formatted_value == "":
            lines.append(f'{REPLACER * (depth + SPACES_COUNT)}{key}: ')
        else:
            lines.append(f'{REPLACER * (depth + SPACES_COUNT)}{key}:{formatted_value}')
    lines.append(f'{REPLACER * depth}}}')
    return '\n'.join(lines)


def format_stylish(diffs):
    def iter_(tree, depth):
        result = ['{']
        offset = depth + SPACES_COUNT
        for node in tree:
            key = node.get('key')
            action_type = node.get('action_type')
            value = node.get('value')
            new_value = node.get('new_value')
            spaces = REPLACER * (offset - 2)

            if action_type == 'added':
                result.append(f'{spaces}+ {key}: {stringify(value, offset)}')
            elif action_type == 'removed':
                result.append(f'{spaces}- {key}: {stringify(value, offset)}')
            elif action_type == 'not_changed':
                result.append(f'{spaces}  {key}: {stringify(value, offset)}')
            elif action_type == 'changed':
                result.append(f'{spaces}- {key}: {stringify(value, offset)}')
                result.append(f'{spaces}+ {key}: {stringify(new_value, offset)}')
            elif action_type == 'children':
                result.append(f'{REPLACER * offset}{key}: {iter_(value, offset)}')

        result.append(f'{REPLACER * depth}}}')
        return '\n'.join(result)
    return iter_(diffs, 0)
