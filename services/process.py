import pandas as pd
from datetime import datetime

def process_temperature_data(file_path: str):
    """
    1. Read a CSV / XLSX file.
    2. Clean the data and convert timestamps
    3. Return a list of JSON records
    """
    # Pandas Data Frame based on file type
    if file_path.endswith('.csv'):
        df: pd.DataFrame = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df: pd.DataFrame = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format")

    # Cleanup1: Required columns check
    required_columns: set[str] = {"time", "temperature", "location"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"Missing required columns: {required_columns - set(df.columns)}")

    # Cleanup2: Drop rows with missing values
    df = df.dropna()

    # Convert dataframe to JSON
    records = df.to_dict(orient="records")
    return records
