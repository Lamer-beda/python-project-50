import os
import json
import yaml


def get_file_extension(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    return file_extension[1:]


def get_content_of_file(file_path):
    with open(file_path) as file:
        return file.read()


def parse_data(content, format):
    if format == 'json':
        return json.loads(content)
    if format == 'yml' or format == 'yaml':
        return yaml.safe_load(content)


def parse_data_from_file(file_path):
    format = get_file_extension(file_path)
    content = get_content_of_file(file_path)

    return parse_data(content, format)
