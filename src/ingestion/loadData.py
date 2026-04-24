import pandas as pd 

def loadData(path: str) -> pd.DataFrame:  
    """
    Carrega o arquivo CSV retornando um DataFrame
    """

    df = pd.read_csv(path, encoding= 'latin1')
    return df