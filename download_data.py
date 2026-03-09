import urllib.request
import os
from typing import List
from pathlib import Path

# Define constants
BASE_URL = "https://raw.githubusercontent.com/JeffSackmann/tennis_atp/refs/heads/master/atp_matches_"
UPPER_YEAR_BOUND = 2024
LOWER_YEAR_BOUND = 2000
DESTINATION_DIR = Path().cwd() / "data" / "raw"

# Create a list of file names to scrape
file_names = [str(year) + ".csv" for year in range(LOWER_YEAR_BOUND, UPPER_YEAR_BOUND + 1)]

def retrieve_data(base_url: str, file_names: List[str], path: Path) -> bool:
    """Retrieves csv files for a given stretch of 
    years (see global vars above) from Jeff Sackmann's 
    GitHub repository (https://github.com/JeffSackmann/tennis_atp)

    Args:
        base_url (str): The shared URL for the raw CSV files
        file_names (List[str]): A list of the names of the 
        CSV files to download
        path (Path): A path object that defines where you 
        want to place the downloaded CSV files

    Returns:
        bool: True if successful
    """
    
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


if __name__ == "__main__":
    print("Retrieving data...")
    
    retrieve_data(base_url=BASE_URL,
                  file_names=file_names,
                  path=DESTINATION_DIR)
    
    print("Finished downloading data.")