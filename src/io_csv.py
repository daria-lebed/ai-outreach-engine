import pandas as pd

def load_leads(path: str) -> pd.DataFrame:
    """Load leads CSV into DataFrame"""
    return pd.read_csv(path)

def save_letters(df: pd.DataFrame, path: str):
    """Save generated letters to CSV"""
    df.to_csv(path, index=False)
