import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from path import Path
import numpy as np
from pathlib import Path
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_df(fname, columns, skiprows=0, exceptrows=0):
    df = pd.read_csv(fname, skiprows=1)[:exceptrows]
    if columns: df = df.loc[:, columns].copy()
    df = df.dropna(axis='columns', how='all')
    df = df.dropna()
    return df

def get_features(df, target_col_name, feature_list):
    X = pd.DataFrame([])
    y = df[target_col_name]
    for feature in feature_list:
        X[feature] = df[feature]
    return X, y

def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    return X_train, X_test, y_train, y_test

def scale_data(X_train, X_test):
    scaler = StandardScaler()
    X_scaler = scaler.fit(X_train)
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
    return X_train_scaled, X_test_scaled

def fix_percents(df, col_name):
    df[col_name] = df[col_name].str.replace('%', '')
    df[col_name] = df[col_name].astype('float') / 100.0
    return df ### superfluous

def filter_rows(df, col_name, value_list):
    for value in value_list:
        mask = df[col_name] != value
        df = df.loc[mask]
    return df ### superfluous

def encode_strings(df):
    columns = []
    for column in df:
        if type(df[column][0]) is str:
            columns.append(column)
            print(column, df[column][0])
    df = pd.get_dummies(df, columns=columns)
    df.reset_index(inplace=True, drop=True)
    return df

