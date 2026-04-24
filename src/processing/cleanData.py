import pandas as pd

def cleanData(df: pd.DataFrame) -> pd.DataFrame:
    """
    limpa e padroniza os dados importados do  csv 
    """
    df.columns = df.columns.str.strip()

    df = df.dropna()

    df =  df.drop_duplicates()

    return df