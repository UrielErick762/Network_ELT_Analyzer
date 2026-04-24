import pandas as pd

def detectAnomalies(df: pd.DataFrame) -> pd.DataFrame:
    """
    verifica trafego suspeito
    """

    if "is_attack" in df.columns:
        suspicious = df[df['is_attack'] == 1]
        return suspicious   
    
    return pd.DataFrame()