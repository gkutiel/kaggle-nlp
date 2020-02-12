from src.paths import *
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


def count_vector_json():
    train = pd.read_csv(data.train_csv)
    test = pd.read_csv(data.test_csv)
    model = CountVectorizer().fit(train['text'])

    train['count_vector'] = model.transform(train['text'])
    test['count_vector'] = model.transform(test['text'])

    train.to_json(out.train_count_vector_json, lines=True, orient='records')
    test.to_json(out.test_count_vector_json, lines=True, orient='records')
