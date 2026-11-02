from pathlib import Path
import duckdb
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
import os 
from dotenv import load_dotenv

load_dotenv()

def nvidia_model(model_name="nvidia/nemotron-3.5-super-vl-120b-a12b") -> OpenAIChatModel:
    return OpenAIChatModel(
        model_name= model_name,
        provider=OpenAIProvider(
            base_url="https://integrate.api.nvidia.com/v1", api_key=os.environ["NVIDIA_API"]
        ),
    )
DATA_PATH = Path(__file__).parent / "data"

def query_duckdb(sql_code: str, parameters = None):
    with duckdb.connect(DATA_PATH / "movies.duckdb") as conn:
        cursor = conn.execute(sql_code, parameters=parameters)

        if sql_code.strip().lower().startswith(("select", "from", "desc", "pragma")):
            return cursor.df()