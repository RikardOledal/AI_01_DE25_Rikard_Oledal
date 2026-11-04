from pathlib import Path
import duckdb
from dotenv import load_dotenv

load_dotenv()

DATA_PATH = Path(__file__).parent / "data"
DATA_PATH.mkdir(exist_ok=True)

def query_duckdb(sql_code: str, parameters = None):
    with duckdb.connect(DATA_PATH / "movies.duckdb") as conn:
        cursor = conn.execute(sql_code, parameters=parameters)

        if sql_code.strip().casefold().startswith(("select", "from", "desc", "pragma")):
            return cursor.df()

if __name__ == "__main__":
    query_duckdb("""
        CREATE TABLE IF NOT EXISTS movies (
            title TEXT,
            year INTEGER,
            genre TEXT,
            rating TINYINT,
            summary TEXT
        );
    """)