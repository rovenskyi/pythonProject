from my_funcs.file_works import files

def clean_test(test_date):
    with open('textfile.txt', 'a') as f_o:
        f_o.write(test_date)

def test_read_form_file():
    test_date = ['one\n', 'two\n', 'three']
    clean_test(test_date)
    assert test_date == files('textfile.txt')
