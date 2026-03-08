import pandas as pd
from pathlib import Path


def load_inventory_data():
    """
    Loads the hyperlocal inventory dataset.

    Returns:
        pandas.DataFrame
    """

    data_path = Path("data/hyperlocal_inventory_data.csv")

    try:
        df = pd.read_csv(data_path)
        return df

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Dataset not found at {data_path}. Please check the data folder."
        )