"""------------------------------------------------------------------------------------------------
    Main File - main entry-point and controller of the ETL pipeline
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
------------------------------------------------------------------------------------------------"""
import argparse
from pathlib import Path
import movie_id_selector
import extract
import transform
import load

BASE_DIRECTORY = Path(__file__).resolve().parent.parent.parent

def __process_imdb_ids():
    """Opens a local TSV file to extract IMDb IDs and writes to a text file"""
    movie_id_selector.extract_ids_from_dataset(BASE_DIRECTORY)


def __process_imdb_data():
    """
    Main ETL pipeline, goes through the multi-step process of extraction, transformation,
    and loading into the local data warehouse.
    """
    extract.fetch_movie_data_from_api(BASE_DIRECTORY)
    transform.parse_raw_movie_data(BASE_DIRECTORY)
    load.store_processed_movie_data(BASE_DIRECTORY)


def main():
    """
    Based on runtime arguments, will either generate txt of IMDb IDs based on filters or
    added to movie_id_selector.py, after fetching API data & loading into data warehouse.
    """
    parser = argparse.ArgumentParser(description="IMDb ETL pipeline")
    parser.add_argument(
        "command",
        choices=["IDs", "data"],
        help="Either run 'IDs' or 'data' select arg"
    )
    args = parser.parse_args()
    if args.command == "IDs":
        __process_imdb_ids()
    elif args.command == "data":
        __process_imdb_data()


if __name__ == "__main__":
    main()
