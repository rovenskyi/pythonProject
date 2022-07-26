from my_funcs.file_workers import read_from_files


def test_read_form_file():
    test_date = ['one\n', 'two\n', 'three']
    assert test_date == read_from_files("tests/testfile.txt")