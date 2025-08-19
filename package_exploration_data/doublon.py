import pandas as pd 
from typing import Optional, List


class Doublon:
    """
    cette classe permet de détecter le nombre de doublons dans une base de données.
    """
    
    @staticmethod
    def nombre_lignes_dupliquees(
        df: pd.DataFrame,
        subset: Optional[List[str]] = None,
        keep: str = "first",
    ) -> int:
        """
        Compte le nombre de lignes dupliquées dans un DataFrame.

        Paramètres
        ----------
        df : pd.DataFrame
            Jeu de données à analyser.
        subset : list[str] | None, optionnel
            Sous-ensemble de colonnes à considérer pour détecter les doublons.
            Par défaut, toutes les colonnes sont prises en compte.
        keep : {"first", "last", False}, optionnel (defaut="first")
            - "first" : marque comme doublon toutes les occurrences sauf la première.
            - "last"  : marque comme doublon toutes les occurrences sauf la dernière.
            - False   : marque **toutes** les occurrences dupliquées (y compris la première).

        Retour
        ------
        int
            Nombre de lignes marquées comme doublons selon la règle `keep`.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("df doit être un pandas.DataFrame")
        return int(df.duplicated(subset=subset, keep=keep).sum())

    
    