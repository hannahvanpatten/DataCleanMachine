# ----------------Imports----------------
import numpy as np
import pandas as pd

dataset = "" # INSERT FILE NAME HERE
original_dataset = pd.read_csv(dataset) # Provide a way to access original dataset for comparability

# ---------Function Definitions----------
def load_and_inspect(file_path: str) -> pd.DataFrame: # Load a dataset and print basic structural health metrics
    global df
    df = pd.read_csv(file_path) # Read the data (ADJUST DELIMITER/ENCODING IF NEEDED)
    print("Initial Data Assessment")
    print("-----------------------")
    print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns\n") # Check row and column counts
    print("Data Types & Missing Values:")
    print(df.info()) # Check data types and missing values
    print("\nDuplicate Rows:", df.duplicated().sum()) # Check for duplicates
    print("Dataset Preview")
    print("---------------")
    print(df.head())
    print("")
    print("")
    return df

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame: # Standardize columns
    df.columns = (
        df.columns.str.strip() # Remove leading and trailing whitespace from column names
        .str.lower() # Converts column names to lowercase
        .str.replace(" ", "_", regex=False) # Replaces whitespace with underscores
        .str.replace(r"[^\w]", "", regex=True) # Removes any non-alphanumeric/underscore characters
    )
    print("Column Name Cleanup")
    print("-------------------")
    print(df.head())
    print("")
    print("")
    return df

def handle_duplicates(df: pd.DataFrame) -> pd.DataFrame: # Remove exact duplicate rows from the dataset
    initial_rows = len(df)
    df = df.drop_duplicates().reset_index(drop=True) # Remove duplicates and clean up index
    print("Exact Duplicates Cleanup")
    print("------------------------")
    print(df.head())
    print(f"Dropped {initial_rows - len(df)} exact duplicate rows.")
    print("")
    print("")
    return df


# ------------Function Calls-------------
load_and_inspect(dataset)

clean_column_names(df)

handle_duplicates(df)