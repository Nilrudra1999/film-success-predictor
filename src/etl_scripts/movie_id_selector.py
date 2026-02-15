"""------------------------------------------------------------------------------------------------
    ID Extractor File - Extracts IDs from IMDb dataset using filter year and "movie" titleType 
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
    --------------------------------------------------------------------------------------------
    ETL pipeline relies on local Microsoft SQL express server for data warehousing, and fetches
    data from all used APIs based on IMDb IDs, extracted from IMDb public dataset tsv file.
------------------------------------------------------------------------------------------------"""
from csv import DictReader

__START_YEAR = 2014  # filter movies by year

def extract_ids_from_dataset(base_directory):
    """
    Opens public IMDb dataset to extract IDs based off filters such as year and title type,
    all movies >= filter year and up to current year and all title types of "movie". Adds the
    extracted IDs into a text file which the ETL pipeline uses to request data from APIs.
    
    Args: base_directory (string): root to directory path
    
    Returns: Nothing, only performs actions and creates a text file
    """
    tsv  = base_directory / "data" / "title.basics.tsv"
    text = base_directory / "data" / "imdb_movie_ids.txt"
    with open(tsv, "r", encoding="utf-8") as reader, open(text, "w", encoding="utf-8") as writer:
        tsv_records = DictReader(reader, delimiter="\t")
        for record in tsv_records:
            if record["startYear"] == r"\N":
                continue
            if record["titleType"] == "movie" and int(record["startYear"]) >= __START_YEAR:
                writer.write(record["tconst"] + "\n")
        print("Movie Id extraction complete.")
