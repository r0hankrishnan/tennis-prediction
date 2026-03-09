from pathlib import Path

BASE_URL = "https://raw.githubusercontent.com/JeffSackmann/tennis_atp/refs/heads/master/atp_matches_"
UPPER_YEAR_BOUND = 2024
LOWER_YEAR_BOUND = 2000
DESTINATION_PATH = Path().cwd() / "data" / "raw"

