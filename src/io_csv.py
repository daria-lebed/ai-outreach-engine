import os
import pandas as pd

def load_leads(path):
    return pd.read_csv(path)

def save_letters(df, path):
    # создадим папку, если её нет
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    df.to_csv(path, index=False)
