import pandas as pd 

def createFeatures(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria novas features para analise
    """

    if "Label" in df.columns:
        df['is_attack'] = df['Label'].apply(lambda x: 0 if  x == 'BENIGN' else 1)

        return df