"""------------------------------------------------------------------------------------------------
    Transformer File - Transforms raw CSV data to tabular format, and stores in processed CSV
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
------------------------------------------------------------------------------------------------"""
from json import loads
import pandas as pd

__MOVIE_JSON_FIELDNAMES = [
    "Title", "Runtime", "Released", "Country", 
    "Director", "Writer", "Actors",
    "Genre", "Ratings", "Awards"
]

__BOX_OFFICE_JSON_FIELDNAMES = [
    "productionBudget", "domesticGross",
    "worldwideGross", "openingWeekendGross"
]


def parse_raw_movie_data(base_directory):
    """
    Opens CSV files containing raw JSON data and reads both the OMDb and the BoxOffice data.
    Then picks apart values related to specified fieldnames, normalizes these values using a
    panda dataframe and loads these values into a new processed CSV with related fieldnames.
    
    Args: base_directory (string): root to directory path
    
    Returns: nothing, only processes data and creates a processed CSV file
    """
    raw_csv = base_directory / "data" / "raw" / "data.csv"
    processed_csv = base_directory / "data" / "processed" / "data.csv"
    df_raw  = pd.read_csv(raw_csv)
    omdb_df = pd.json_normalize(df_raw['omdb_data'].apply(loads))
    box_office_df = df_raw['box_office_data'].apply(loads).apply(__extract_box_office)
    box_office_df = pd.DataFrame(box_office_df.tolist())
    df = pd.concat(
        [omdb_df[__MOVIE_JSON_FIELDNAMES], box_office_df[__BOX_OFFICE_JSON_FIELDNAMES]],
        axis=1
    )
    required_fields = [
        "Title", 
        "Runtime", 
        "Released", 
        "Country", 
        "Director", 
        "productionBudget", 
        "openingWeekendGross"
    ]
    df.replace("N/A", pd.NA, inplace=True)
    df.dropna(subset=required_fields, inplace=True)
    df = __normalize_dataframe(df)
    df.to_csv(processed_csv, index=False)



def __extract_box_office(entry):
    extracted = {}
    for field in __BOX_OFFICE_JSON_FIELDNAMES:
        bo_data = entry.get(field)
        if isinstance(bo_data, dict):
            val = bo_data.get("amount") or bo_data.get("gross", {}).get("amount")
            extracted[field] = val
        else:
            extracted[field] = None
    return extracted



def __normalize_dataframe(df):
    """
    Fixing runtime, date, country, ratings, and director values in typical movie records. Adds
    filler values to domestic or international BO based on: opening weekend x 2 days x 35 days
    for domestic sales and 1.8 x DS (adjusting for volume) for international sales.
    
    Args: df (panda obj - dataframe): un-normalized movie data

    Returns: panda dataframe: contains the normalized data
    """
    df['productionBudget']    = pd.to_numeric(df['productionBudget'], errors='coerce')
    df['openingWeekendGross'] = pd.to_numeric(df['openingWeekendGross'], errors='coerce')
    domestic_profit_normalization = (df['openingWeekendGross'] / 2.0) * 35.0
    intern_profit_normalization   = domestic_profit_normalization * 1.8
    df['domesticGross']  = pd.to_numeric(
        df['domesticGross'],
        errors='coerce'
    ).fillna(domestic_profit_normalization)
    df['worldwideGross'] = pd.to_numeric(
        df['worldwideGross'],
        errors='coerce'
    ).fillna(intern_profit_normalization)
    df['Runtime']  = df['Runtime'].str.split(" ").str[0]
    df['Released'] = pd.to_datetime(
        df['Released'],
        format='%d %b %Y',
        errors='coerce'
    ).dt.strftime('%Y/%m/%d')
    df['Country']  = df['Country'].str.split(",").str[0].str.strip()
    df['Director'] = df['Director'].str.split(",").str[0].str.strip()
    df['Ratings']  = df['Ratings'].apply(__process_ratings_list)
    return df



def __process_ratings_list(ratings):
    if not isinstance(ratings, list) or len(ratings) == 0:
        return "House Rating:8.5"
    processed = []
    for rating in ratings:
        src, val = rating.get("Source"), rating.get("Value", "")
        clean = None
        if src == "Internet Movie Database":
            clean = float(val.split("/")[0])
        elif src == "Rotten Tomatoes":
            clean = float(val.replace("%", "")) / 10
        elif src == "Metacritic":
            clean = float(val.split("/")[0]) / 10
        if clean is not None:
            if clean < 1.0:
                clean *= 10.0
            processed.append(f"{src}:{clean}")
    return ", ".join(processed) if processed else "House Rating:8.5"
