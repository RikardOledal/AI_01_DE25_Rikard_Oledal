from pydantic import BaseModel, Field
from lancedb.embeddings import get_registry
from lancedb.pydantic import LanceModel, Vector
from aimodules import embedders
from dotenv import load_dotenv

load_dotenv()

embedding_model = get_registry().get("nvidia-nemotron").create()

EMBEDDING_DIM = 2048

class Article(LanceModel):
    doc_id: str
    filepath: str
    filename: str = Field(description="the stem of the file i.e. without the suffix")
    content: str = embedding_model.SourceField()
    embedding: Vector(EMBEDDING_DIM) = embedding_model.VectorField()