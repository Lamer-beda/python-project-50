import pytest
from gendiff.generate_diff import generate_diff


file1_json = 'tests/fixtures/file1.json'
file2_json = 'tests/fixtures/file2.json'
@pytest.mark.parametrize(
    'path1, path2, format, expected',
    [
        (file1_json, file2_json, 'stylish', expected)

    ]
)
def test_gendiff(path1, path2, format, expected):
    with open(expected) as result:
        assert generate_diff(path1, path2, format) == result.read()


def test_empty_file():
    wrong = 'tests/fixtures/empty_file.json'
    path = 'tests/fixtures/file1.json'
    with pytest.raises(ValueError):
        generate_diff(wrong, path)


def test_not_supproted_format():
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'
    with pytest.raises(NameError):
        generate_diff(path1, path2, 'excellent')
