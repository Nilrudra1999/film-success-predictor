"""------------------------------------------------------------------------------------------------
    Loader File - Loads processed CSV data into local Microsoft express server based database
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
    --------------------------------------------------------------------------------------------
    ETL pipeline relies on local Microsoft SQL express server for data warehousing, and fetches
    data from all used APIs based on IMDb IDs, extracted from IMDb public dataset tsv file.
------------------------------------------------------------------------------------------------"""
import re
import pandas as pd
import pyodbc

__CONNECTION_STRING = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=ADMINISTRATOR\\SQLEXPRESS;"
    "Database=imdb_analytics_database;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)


def store_processed_movie_data(base_directory):
    """
    Opens the processed CSV file with fieldname partitioned data and uses the fields to load
    records into the local database. Looping through each record after opening a odbc conn.
    Outputs the total number of records loaded into the database after completion.
    
    Args: base_directory (string): root to directory path
    
    Returns: nothing, only loads data into local database
    """
    processed_csv = base_directory / "data" / "processed" / "data.csv"
    df = pd.read_csv(processed_csv, keep_default_na=False)
    records, record_cnt = df.to_dict('records'), 0
    # pylint: disable=c-extension-no-member
    connection = pyodbc.connect(__CONNECTION_STRING, autocommit=True)
    cursor = connection.cursor()
    try:
        for record in records:
            movie_data = __get_database_data(record)
            dir_id   = __insert_into_directors(movie_data, cursor)
            movie_id = __insert_into_movies(movie_data, dir_id, cursor)
            __insert_into_revenues(movie_data, movie_id, cursor)
            __insert_into_awards(movie_data, movie_id, cursor)
            __insert_into_ratings(movie_data, movie_id, cursor)
            __insert_into_genres(movie_data, movie_id, cursor)
            __insert_into_writers(movie_data, movie_id, cursor)
            __insert_into_actors(movie_data, movie_id, cursor)
            record_cnt += 1
    finally:
        cursor.close()
        connection.close()
    print(f"Added {record_cnt} records to the database.")



def __get_database_data(record):
    wins = nominations = None
    movie_dict = {
        "director_name": record.get("Director"),
        "title": record.get("Title"),
        "runtime": record.get("Runtime"),
        "release": record.get("Released"),
        "country": record.get("Country"),
        "writers": [w.strip() for w in str(record.get("Writer", "")).split(",")],
        "actors":  [a.strip() for a in str(record.get("Actors", "")).split(",")],
        "genres":  [g.strip() for g in str(record.get("Genre", "")).split(",")],
        "ratings": [r.strip() for r in str(record.get("Ratings", "")).split(",")],
        "prod_bg": float(record.get("productionBudget")),
        "dome_gr": float(record.get("domesticGross")),
        "intr_gr": float(record.get("worldwideGross")),
        "op_w_gr": float(record.get("openingWeekendGross"))
    }
    raw_awards = str(record.get("Awards", ""))
    if raw_awards and raw_awards != "N/A":
        win_match = re.search(r'(\d+)\s+win', raw_awards, re.IGNORECASE)
        nom_match = re.search(r'(\d+)\s+nomination', raw_awards, re.IGNORECASE)
        if win_match:
            wins = win_match.group(1)
        if nom_match:
            nominations = nom_match.group(1)
    movie_dict["awards"] = [wins, nominations]
    return movie_dict



def __insert_into_directors(movie_data, cursor):
    max_id = 0
    name = movie_data["director_name"]
    cursor.execute(
        "select director_id from directors where director_name = ?",
        (name,)
    )
    result = cursor.fetchone()
    if result:
        max_id = result[0]
    else:
        max_id = __get_max_id("select max(director_id) from directors", cursor)
        cursor.execute("insert into directors values (?, ?)", (max_id, name,))
    return max_id



def __insert_into_genres(movie_data, movie_id, cursor):
    max_id = __get_max_id("select max(genre_id) from genres", cursor)
    if movie_data["genres"] == "N/A":
        return
    for genre in movie_data["genres"]:
        cursor.execute("select genre_id from genres where genre_name = ?", (genre,))
        result = cursor.fetchone()
        if result:
            cursor.execute(
                "insert into associated_genres values (?, ?)",
                (movie_id, result[0])
            )
        else:
            cursor.execute("insert into genres values (?, ?)", (max_id, genre))
            cursor.execute(
                "insert into associated_genres values (?, ?)",
                (movie_id, max_id)
            )
            max_id = max_id + 1



def __insert_into_writers(movie_data, movie_id, cursor):
    max_id = __get_max_id("select max(writer_id) from writers", cursor)
    if movie_data["writers"] == "N/A":
        return
    for writer in movie_data["writers"]:
        cursor.execute(
            "select writer_id from writers where writer_name = ?",
            (writer,)
        )
        result = cursor.fetchone()
        if result:
            cursor.execute(
                "insert into associated_writers values (?, ?)",
                (movie_id, result[0])
            )
        else:
            cursor.execute("insert into writers values (?, ?)", (max_id, writer))
            cursor.execute(
                "insert into associated_writers values (?, ?)",
                (movie_id, max_id)
            )
            max_id = max_id + 1



def __insert_into_actors(movie_data, movie_id, cursor):
    max_id = __get_max_id("select max(actor_id) from actors", cursor)
    if movie_data["actors"] == "N/A":
        return
    for actor in movie_data["actors"]:
        cursor.execute(
            "select actor_id from actors where actor_name = ?",
            (actor,)
        )
        result = cursor.fetchone()
        if result:
            cursor.execute(
                "insert into associated_actors values (?, ?)",
                (movie_id, result[0])
            )
        else:
            cursor.execute("insert into actors values (?, ?)", (max_id, actor))
            cursor.execute(
                "insert into associated_actors values (?, ?)",
                (movie_id, max_id)
            )
            max_id = max_id + 1



def __insert_into_movies(movie_data, dir_id, cursor):
    title   = movie_data["title"]
    runtime = movie_data["runtime"]
    release = movie_data["release"]
    country = movie_data["country"]
    max_id = __get_max_id("select max(movie_id) from movies", cursor)
    cursor.execute(
        "insert into movies values (?, ?, ?, ?, ?, ?)",
        (max_id, title, release, runtime, country, dir_id)
    )
    return max_id



def __insert_into_revenues(movie_data, movie_id, cursor):
    prod_budget = movie_data["prod_bg"]
    domestic_gr = movie_data["dome_gr"]
    interntl_gr = movie_data["intr_gr"]
    opening_wkd = movie_data["op_w_gr"]
    max_id = __get_max_id("select max(revenue_id) from revenues", cursor)
    cursor.execute(
        "insert into revenues values (?, ?, ?, ?, ?, ?)",
        (max_id, movie_id, prod_budget, domestic_gr, interntl_gr, opening_wkd)
    )



def __insert_into_ratings(movie_data, movie_id, cursor):
    max_id = __get_max_id(
        "select max(rating_id) from ratings",
        cursor
    )
    for rating in movie_data["ratings"]:
        ptrs = rating.split(":", 1)
        src  = ptrs[0].strip()
        val  = int(float(ptrs[1].strip()))
        cursor.execute(
            "insert into ratings values (?, ?, ?, ?)",
            (max_id, movie_id, src, val)
        )
        max_id = max_id + 1



def __insert_into_awards(movie_data, movie_id, cursor):
    wins = movie_data["awards"][0]
    nominations = movie_data["awards"][1]
    cursor.execute(
        "insert into awards values (?, ?, ?)",
        (movie_id, wins, nominations)
    )



def __get_max_id(stmt: str, cursor):
    cursor.execute(stmt)
    id_result = cursor.fetchone()
    if id_result[0] is not None:
        curr_max = id_result[0]
    else:
        curr_max = 0
    return curr_max + 1
