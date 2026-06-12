# ----------------Imports----------------
import numpy as np
import pandas as pd

original_csv = "" # INSERT FILE NAME HERE

# ---------Function Definitions----------
def load_and_inspect(file_path: str) -> pd.DataFrame: # Load a dataset and print basic structural health metrics
    global df
    df = pd.read_csv(file_path) # Read the data (ADJUST DELIMITER/ENCODING IF NEEDED)
    print("------ Initial Data Assessment ------")
    print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns\n") # Check row and column counts
    print("Data Types & Missing Values:")
    print(df.info()) # Check data types and missing values
    print("\nDuplicate Rows:", df.duplicated().sum()) # Check for duplicates
    return df

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame: # Standardize columns
    df.columns = (
        df.columns.str.strip() # Remove leading and trailing whitespace from column names
        .str.lower() # Converts column names to lowercase
        .str.replace(" ", "_", regex=False) # Replaces whitespace with underscores
        .str.replace(r"[^\w]", "", regex=True) # Removes any non-alphanumeric/underscore characters
    )
    return df


# ------------Function Calls-------------
load_and_inspect(original_csv)
print("")
print("")
print("Original Dataset Preview")
print("------------------------")
print(df.head())
print("")
print("")

clean_column_names(df)
print("Column Name Cleanup")
print("-------------------")
print(df.head())
print("")
print("")

