from pathlib import Path


class data:
    _ = Path('data')

    train_csv = _ / 'train.csv'
    test_csv = _ / 'test.csv'


class src:
    _ = Path('src')

    task_dummy = _ / 'task_dummy.py'
    task_label_txt = _ / 'task_label_txt.py'
    task_count_vector_json = _ / 'task_count_vector_json.py'


class out:
    _ = Path('out')

    train_label_txt = _ / 'train_label.txt'
    test_label_txt = _ / 'test_label.txt'

    train_count_vector_json = _ / 'train_count_vector.json'
    test_count_vector_json = _ / 'test_count_vector.json'
