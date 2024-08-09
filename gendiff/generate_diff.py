from gendiff.parser import parse_data_from_file
from gendiff.build_diff import generate
from gendiff.formatters.choice_formatter import format_diff


def generate_diff(path_to_file1, path_to_file2, formatter='stylish'):
    content_file_1 = parse_data_from_file(path_to_file1)
    content_file_2 = parse_data_from_file(path_to_file2)
    diff = generate(content_file_1, content_file_2)
    return format_diff(diff, formatter)
