import pandas as pd 
from typing import Optional, Sequence


class NouvelleVariableMoyenne:
    """
    """
    
    @staticmethod
    def qualite_moyenne(
        df: pd.DataFrame,
        *,
        colonnes: Optional[Sequence[str]] = None,  # si None: prend toutes les colonnes numériques
        inplace: bool = True,
        skipna: bool = True                       # True = ignore les NaN dans la moyenne
    ) -> pd.DataFrame:
        """
        Ajoute/Met à jour la colonne 'qualite_label' = moyenne par ligne des variables numériques.

        Paramètres
        ----------
        df : pd.DataFrame
            Base de données d'entrée. val
        colonnes : liste[str] | None
            Sous-ensemble de colonnes sur lesquelles calculer la moyenne.
            Si None, toutes les colonnes numériques sont utilisées.
        inplace : bool
            True  -> modifie df et le renvoie.
            False -> renvoie une copie modifiée.
        skipna : bool
            True  -> ignore les NaN dans la moyenne (pandas par défaut).
            False -> la moyenne devient NaN si une valeur NaN est présente sur la ligne.

        Retour
        ------
        pd.DataFrame
            DataFrame (modifié ou copie) contenant la colonne 'qualite_label'.

        Exceptions
        ----------
        TypeError  : si df n'est pas un DataFrame.
        KeyError   : si des colonnes demandées n'existent pas.
        ValueError : si aucune colonne numérique n'est trouvée.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("`df` doit être un pandas.DataFrame.")

        if colonnes is None:
            cols = df.select_dtypes(include="number").columns.tolist()
        else:
            manquantes = [c for c in colonnes if c not in df.columns]
            if manquantes:
                raise KeyError(f"Colonnes absentes: {manquantes}")
            # Ne garder que les colonnes numériques parmi celles demandées
            cols = [c for c in colonnes if pd.api.types.is_numeric_dtype(df[c])]

        if len(cols) == 0:
            raise ValueError("Aucune colonne numérique trouvée pour calculer 'qualite_label'.")

        cible = df if inplace else df.copy()
        cible["qualite_label"] = cible[cols].mean(axis=1, skipna=skipna)
        return cible
