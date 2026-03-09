import pandas as pd
import numpy as np
import os
from pathlib import Path
from download_data import DESTINATION_DIR
from typing import List

# RAW_DATA_DIR = DESTINATION_DIR
# LOWER_YEAR_BOUND = 2000
# files_to_open = [file for file in sorted(os.listdir(RAW_DATA_DIR)) if int(file.split(".")[0]) >= 2000]

def create_concatenated_data(raw_data_dir:Path, files_to_open:List[str]) -> pd.DataFrame:
    matches_df_list = [pd.read_csv(Path().cwd()/"data"/"raw"/file) for file in files_to_open]
    full_matches_df = pd.concat(matches_df_list)
    
    return full_matches_df

def fix_date_col(df: pd.DataFrame, date_col:str = "tourney_date") -> pd.DataFrame:
    df[date_col] = df[date_col].apply(lambda x: f"{str(x)[0:4]}-{str(x)[4:6]}-{str(x)[6:8]}")
    df[date_col] = pd.to_datetime(df[date_col])
    
    return df

def process_na_values():
    pass

def display_NAs(df:pd.DataFrame) -> pd.DataFrame:
    cols = df.columns.to_list()
    na_counts = [df[col].isna().sum() for col in cols]
    na_ratio = [round(na_count / df.shape[0], 4) for na_count in na_counts]
    dtypes = [df[col].dtype for col in cols]
    
    na_display = pd.DataFrame({
        "Column": cols,
        "Count of NA Values": na_counts,
        "Ratio of NA Values": na_ratio,
        "Column Data Type": dtypes
    }).sort_values(by = "Ratio of NA Values", ascending = False)
    
    return na_display