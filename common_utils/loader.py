import pandas as pd

def load_csv_with_dates(path, date_columns=None):
    """
    Charge un fichier CSV en parsant certaines colonnes comme des dates.

    Args:
        path (str): chemin vers le fichier CSV
        date_columns (list, optional): liste des colonnes à parser comme dates

    Returns:
        pd.DataFrame: données chargées
    """
    if date_columns is None:
        df = pd.read_csv(path)
    else:
        df = pd.read_csv(path, parse_dates=date_columns)
    return df
