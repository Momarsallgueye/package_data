import pandas as pd
import numpy as np
from typing import Literal, Any


class MoyenMedianMode:
    """ 
    cette classe permet de faire l'imputation par moyenne, médiane ou mode.
    """
    
    
    Strategy = Literal["moyenne", "mediane", "mode", "mean", "median"]
    
    @staticmethod
    def calcul_imputation(
        df: pd.DataFrame,
        colonne: str,
        type_imputation: Strategy = "moyenne",
        *,
        inplace: bool = False,
        fallback: Any | None = None,
    ) -> pd.DataFrame:
        """
        Impute les valeurs manquantes d'une colonne d'un DataFrame selon une stratégie.

        Paramètres
        ----------
        df : pd.DataFrame
            Jeu de données.
        colonne : str
            Nom de la colonne à imputer.
        type_imputation : {"moyenne","mediane","mode","mean","median"}
            Stratégie d'imputation (synonymes FR/EN acceptés).
        inplace : bool, default False
            Si True, modifie `df` sur place. Sinon, retourne une copie.
        fallback : Any | None, default None
            Valeur de repli si la statistique (moyenne/médiane/mode) est indisponible
            (ex. colonne entièrement NaN).

        Retour
        ------
        pd.DataFrame
            DataFrame avec la colonne imputée.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("`df` doit être un pandas.DataFrame.")
        if colonne not in df.columns:
            raise KeyError(f"Colonne absente: {colonne!r}")

        s = df[colonne]
        strat = type_imputation.lower()

        if strat in ("moyenne", "mean"):
            val = s.mean()
        elif strat in ("mediane", "median"):
            val = s.median()
        elif strat == "mode":
            m = s.mode(dropna=True)
            val = m.iat[0] if not m.empty else np.nan
        else:
            raise ValueError("type_imputation doit être 'moyenne', 'mediane' ou 'mode'.")

        # Si la statistique est NaN (colonne entièrement NaN), on tente fallback
        out_col = s.fillna(val)
        if pd.isna(val) and fallback is not None:
            out_col = out_col.fillna(fallback)

        if inplace:
            df[colonne] = out_col
            return df
        out = df.copy()
        out[colonne] = out_col
        return out

    
    
                 
            
        
        
        
        
        
 