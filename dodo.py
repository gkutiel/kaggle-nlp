from src.task_count_vector_json import count_vector_json
from src.task_dummy import dummy
from src.paths import *
from doit.tools import run_once


def task_get_data():
    return {
        'actions': [
            'mkdir -p data out',
            'kaggle competitions download -c nlp-getting-started',
            'unzip -o nlp-getting-started.zip -d data',
        ],
        'file_dep': [],
        'targets': [
            data.train_csv,
            data.test_csv
        ],
        'uptodate': [run_once],
        'verbosity': 2,
    }


def task_label_txt():
    return {
        'actions': [dummy],
        'file_dep': [],
        'targets': [],
        'uptodate': [],
        'verbosity': 2,
    }


def task_count_vector_json():
    return {
        'actions': [count_vector_json],
        'file_dep': [
            src.task_count_vector_json,
            data.train_csv,
            data.test_csv,
        ],
        'targets': [
            out.train_count_vector_json,
            out.test_count_vector_json,
        ],
        'uptodate': [],
        'verbosity': 2,
    }


def task_dummy():
    return {
        'actions': [dummy],
        'file_dep': [],
        'targets': [],
        'uptodate': [],
        'verbosity': 2,
    }
