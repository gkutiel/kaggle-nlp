from src.paths import *
import pandas as pd


def dummy():
    train = pd.read_csv(data.train_csv)
    print(train.head())
