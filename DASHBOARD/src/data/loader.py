import pandas as pd
import os
import json


def load_dataframe(path: str, sheetname: str = None) -> pd.DataFrame:
    """
    Load data from a file and return a pandas dataframe.

    Args:
        path (str): The path to the file.
        sheetname (str, optional): The name of the sheet to load (if loading from an excel file). Defaults to None.

    Returns:
        pd.DataFrame: The loaded data as a pandas dataframe.
    """
    if os.path.splitext(path)[1] == '.json':
        # Load the JSON file
        with open(path, 'r') as f:
            data = json.load(f)

        # Convert the JSON file to a pandas dataframe. This will be used to generate graphs for PVA
        df = pd.json_normalize(data)

    elif os.path.splitext(path)[1] == '.xlsx':
        # Load the excel file
        df = pd.read_excel(path, sheet_name=sheetname)

    return df
