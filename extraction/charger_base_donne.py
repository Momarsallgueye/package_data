import pandas as pd
from urllib.parse import urlparse
from pathlib import PurePosixPath
from typing import Any, Optional, Sequence

class ChargerBaseDonne:
    """ 
    cette classe charge la base de données à partir d'un URL
    """
    
    @staticmethod
    def load_data(
        url: str,
        *,
        sep: Optional[str] = None,        # None => détection auto (engine='python')
        header: Optional[int | str] = "infer",
        names: Optional[Sequence[str]] = None,
        **read_kwargs: Any
    ) -> pd.DataFrame:
        """
        Charge un dataset depuis une URL/chemin en détectant le format.
        Gère CSV/TSV/TXT/DATA/DAT/JSON/JSONL/Excel/Parquet/Feather/Pickle.
        Particularité : .data/.dat (UCI) sont traités comme CSV.
        """

        if not isinstance(url, str) or not url.strip():
            raise TypeError("`url` doit être une chaîne non vide.")

        path = urlparse(url).path
        suffixes = [s.lower() for s in PurePosixPath(path).suffixes]  # ex: ['.csv', '.gz']
        joined = "".join(suffixes)

        def has(*patterns: str) -> bool:
            return any(p in joined for p in patterns)

        # --- petit helper pour CSV avec gestion propre de l'engine ---
        def _read_csv(u: str, sep_arg: Optional[str]):
            csv_kwargs = dict(header=header, names=names, **read_kwargs)
            if sep_arg is None:
                # Sniff du séparateur => engine='python', surtout PAS low_memory
                return pd.read_csv(u, sep=None, engine="python", **csv_kwargs)
            else:
                # Engine par défaut (C) => on peut utiliser low_memory
                return pd.read_csv(u, sep=sep_arg, low_memory=False, **csv_kwargs)

        try:
            # ===== Formats par extension =====
            if has(".csv", ".txt", ".data", ".dat"):
                return _read_csv(url, sep)

            if has(".tsv"):
                return _read_csv(url, "\t")

            if has(".xlsx", ".xls"):
                return pd.read_excel(url, header=0 if header == "infer" else header, **read_kwargs)

            if has(".jsonl"):
                return pd.read_json(url, lines=True, **read_kwargs)
            if has(".json"):
                return pd.read_json(url, **read_kwargs)

            if has(".parquet"):
                return pd.read_parquet(url, **read_kwargs)
            if has(".feather"):
                return pd.read_feather(url, **read_kwargs)

            if has(".pkl", ".pickle"):
                return pd.read_pickle(url, **read_kwargs)

            # ===== Fallbacks si extension inconnue =====
            # 1) CSV sniff (engine='python')
            try:
                return _read_csv(url, None)
            except Exception:
                pass

            # 2) TSV/whitespace
            try:
                return pd.read_csv(url, sep=r"\s+", engine="python",
                                header=header, names=names, **read_kwargs)
            except Exception:
                pass

            # 3) JSONL → JSON
            for kw in (dict(lines=True), dict()):
                try:
                    return pd.read_json(url, **kw, **read_kwargs)
                except Exception:
                    continue

            # 4) Excel
            try:
                return pd.read_excel(url, header=0 if header == "infer" else header, **read_kwargs)
            except Exception:
                pass

            raise ValueError(
                "Format non reconnu et échec des fallbacks "
                "(CSV/whitespace/JSON/Excel). Spécifiez `sep`, `header`, `names` "
                "ou vérifiez la ressource."
            )

        except ImportError as e:
            raise ImportError(
                f"Moteur manquant pour ce format : {e}. "
                "Installez le paquet requis (ex. `pip install pyarrow fastparquet openpyxl`)."
            ) from e
        except Exception as e:
            raise ValueError(f"Échec de lecture de '{url}': {e}") from e
