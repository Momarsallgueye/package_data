import pandas as pd


class ZScoreAnomalie:
    """ 
    cette permet de détecter les anomalie par la méthode du Z score
    """
    
    @staticmethod
    def calcul_zscore(df: pd.DataFrame, colonne: str) -> pd.DataFrame:
        """
        """
        
        if not isinstance(df, pd.DataFrame):
            raise TypeError("df doit etre un dataframe")
        
        lim_sup=df[colonne].mean() + 3*df[colonne].std()
        lim_INF=df[colonne].mean() - 3*df[colonne].std()
        val_aber=df.loc[(df[colonne] > lim_sup) |(df[colonne]<lim_INF),:]
        
        return val_aber
        
        
        
        
        