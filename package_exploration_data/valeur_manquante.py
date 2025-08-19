import pandas as pd 


class ValeurManquante:
    """
    Cette classe permet de calculer le nombre de valeur manquantes d'une base de données.
    """
    
    @staticmethod
    def valeur_manquante(data : pd.DataFrame):
        """ 
        cette fonction permet de savoir si la base de données data contient elle des valeures manquantes.
        
        Paramétres:
        ----------
        
        data : pd.DataFrame
            Jeu de données à analyser
            
        retour:
            soit un texte indiquant qu il n'a pas de valeur manquantes 
            ou bien les variables avec le nombres de valeurs manquantes qu il contient.    
        
        """
        
        if not isinstance(data, pd.DataFrame):
            raise TypeError("`data` doit être un pd.DataFrame.")
        
        nbre_total_val_mq = int(data.isnull().sum().sum())
        
        if nbre_total_val_mq == 0:
            
            val_retour = "La base de donnée ne contient pas de valeur manquante"
        else:
            val_retour = print(data.isnull().sum())    
            
        return val_retour    
        
    