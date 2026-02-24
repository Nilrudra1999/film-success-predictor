"""------------------------------------------------------------------------------------------------
    Main Extractor File - Extracts raw data from APIs as-is, store in unprocessed CSV file
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
------------------------------------------------------------------------------------------------"""
from csv import writer
from json import dumps
from os import getenv
import requests
from dotenv import load_dotenv

load_dotenv()
__IMDB_URL  = getenv("IMDB_API_BASE_URL")
__OMDB_URL  = getenv("OMDB_API_BASE_URL")
__API_KEY   = getenv("API_KEY")

# OMDb API has a total daily limit of 1000 requests
__ID_CURSOR  = int(getenv("ID_CURSOR", "0"))
__MAX_MOVIES = 1000


def fetch_movie_data_from_api(base_directory):
    """
    Opens files for reading IMDb IDs and writing JSON API data. Moves to the cursor indicated
    location of IMDb IDs to start where the pervious run left off, and then fetches API data.
    Stores the data as-is with a "raw/data.csv" file updates cursor position for the next run.
    
    Args: base_directory (string): root to directory path
    """
    ids = base_directory / "data" / "imdb_movie_ids.txt"
    raw = base_directory / "data" / "raw" / "data.csv"
    env_file  = base_directory / "src" / "etl_scripts" / ".env"
    row_count = 0
    with open(ids, "r", encoding="utf-8") as in_f, open(raw, "w", encoding="utf-8") as out_f:
        csv_writer  = writer(out_f)
        csv_writer.writerow(["movie_id", "omdb_data", "box_office_data"])
        __move_to_cursor_position(in_f)
        row_count = __fetching_data(row_count, in_f, csv_writer)
        __update_cursor_position(__ID_CURSOR + row_count, env_file)



def __fetching_data(row_count, dataset_read, dataset_write):
    while row_count < __MAX_MOVIES:
        record = dataset_read.readline()
        if not record: # EOF state
            print("Data for all specified IMDb IDs have been acquired")
            break
        movie_id = record.strip()
        movie_data = __fetch_omdb_data(movie_id)
        box_office_data = __fetch_box_office_data(movie_id)
        dataset_write.writerow([
            movie_id,
            dumps(movie_data),
            dumps(box_office_data)
        ])
        row_count += 1
    return row_count



def __fetch_omdb_data(movie_id):
    params = {"apikey": __API_KEY, "i": movie_id}
    try:
        response = requests.get(__OMDB_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print(f"OMDB Error: Request timed out for {movie_id}")
        return {"error": "OMDB API timeout"}
    except requests.exceptions.RequestException as err:
        print(f"OMDB Error: Ambiguous request error: {err}")
        return {"error": "OMDB connection error"}



def __fetch_box_office_data(movie_id):
    url = f"{__IMDB_URL}{movie_id}/boxOffice"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print(f"BoxOffice Error: Request timed out for {movie_id}")
        return {"error": "BoxOffice API timeout"}
    except requests.exceptions.RequestException as err:
        print(f"BoxOffice Error: Ambiguous request error: {err}")
        return {"error": "BoxOffice connection error"}



def __move_to_cursor_position(dataset):
    for _ in range(__ID_CURSOR):
        dataset.readline()



def __update_cursor_position(value: int, env_file):
    lines = env_file.read_text().splitlines()
    lines[-1] = f"ID_CURSOR={value}"
    env_file.write_text("\n".join(lines) + "\n")
    print(f"ID_CURSOR is at position {value} in .env")
