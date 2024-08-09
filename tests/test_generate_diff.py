from gendiff.generate_diff import generate_diff
import pytest


@pytest.mark.parametrize(
    'path_to_file1, path_to_file2, formatter, expected_result',
    [
        (
            './tests/fixtures/file-1.json',
            './tests/fixtures/file-2.json',
            'stylish',
            './tests/fixtures/expected_results_stylish.txt'
        ),
        (
            './tests/fixtures/file-1.yml',
            './tests/fixtures/file-2.yml',
            'stylish',
            './tests/fixtures/expected_results_stylish.txt'
        ),
        (
            './tests/fixtures/file-1.json',
            './tests/fixtures/file-2.json',
            'plain',
            './tests/fixtures/expected_results_plain.txt'
        ),
        (
            './tests/fixtures/file-1.yml',
            './tests/fixtures/file-2.yml',
            'plain',
            './tests/fixtures/expected_results_plain.txt'
        ),
        (
            './tests/fixtures/file-1.json',
            './tests/fixtures/file-2.json',
            'json',
            './tests/fixtures/expected_results_json.json'
        ),
        (
            './tests/fixtures/file-1.yml',
            './tests/fixtures/file-2.yml',
            'json',
            './tests/fixtures/expected_results_json.json'
        )
    ]
)
def test_gendiff(path_to_file1, path_to_file2, formatter, expected_result):
    diff = generate_diff(path_to_file1, path_to_file2, formatter).strip('\n')
    with open(expected_result) as file:
        result = file.read().strip('\n')
        if result != diff:
            print("=== Expected ===")
            print(result)
            print("================")
            print("=== Actual ===")
            print(diff)
            print("================")

        assert diff == result
