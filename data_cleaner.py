# ----------------Imports----------------
import numpy as np
import pandas as pd

original_csv = "" # INSERT FILE NAME HERE

# ---------Function Definitions----------
def load_and_inspect(file_path: str) -> pd.DataFrame: # Load a dataset and print basic structural health metrics
    global df
    df = pd.read_csv(file_path) # Read the data (ADJUST DELIMITER/ENCODING IF NEEDED)
    print("------ Initial Data Assessment ------")
    print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns\n")
    print("Data Types & Missing Values:")
    print(df.info())
    print("\nDuplicate Rows:", df.duplicated().sum())
    return df


# ------------Function Calls-------------
load_and_inspect(original_csv)