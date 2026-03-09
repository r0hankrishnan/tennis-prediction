import urllib.request
import os
from pathlib import Path
from config import BASE_URL, DESTINATION_PATH, LOWER_YEAR_BOUND, UPPER_YEAR_BOUND
import pandas as pd

def retrive_data(base_url:str = BASE_URL, path:Path = DESTINATION_PATH) -> bool:
    """_summary_

    Args:
        base_url (str): _description_
        file_names (List[str]): _description_
        path (Path): _description_

    Returns:
        bool: _description_
    """
    file_names = [str(year) + ".csv" for year in range(LOWER_YEAR_BOUND, UPPER_YEAR_BOUND + 1)]
    # Loop over each file, download it from GitHub, and store in destination directory
    for file in file_names:
        
        # Create CSV file's URL and the destination file path
        url = base_url + file
        file_path = DESTINATION_DIR / file
        
        # Download and store the CSV
        urllib.request.urlretrieve(url, file_path)
        
        # Check if the file went to the right place
        if os.path.exists(file_path):
            print(f"Downloaded {file} to {path}.")
        else:
            raise FileNotFoundError("Something went wrong. Start by checking if the URL or file names have changed on the GitHub.")
    return True

def load_directly_from_github(base_url:str = BASE_URL) -> pd.DataFrame:
    """Load data directly from Github. Loop over raw GitHub URLs, load with 
    pd.read_csv(), add to list of data frames, and concatenate to join together.

    Args:
        base_url (str, optional): Common raw GitHub URL. Files all
        follow the following naming convention: apt_matches_{year}.csv. 
        Defaults to BASE_URL.

    Returns:
        pd.DataFrame: Concatenated dataframe of matches from LOWER_YEAR_BOUND
        to UPPER_YEAR_BOUND
    """
    
    raw_dfs = []
    for year in range(LOWER_YEAR_BOUND, UPPER_YEAR_BOUND + 1):
        raw_dfs.append(pd.read_csv(base_url + str(year) + ".csv"))
    
    return pd.concat(raw_dfs)

def clean_raw_data(data:pd.DataFrame) -> pd.DataFrame:
    # Filer out Davis Cup Matches
    
    # Convert tourney_date
    
    # Standardize entry columns (winner and loser)
    
    # Create unseeded indicator columns (winner and loser)
    
    # Standardize hand columns (just loser)
    
    # 
    
    
    pass