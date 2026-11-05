from pydantic import BaseModel, Field
from pydantic_ai import ModelMessage

class ChatRequest(BaseModel):
    question: str = Field(description="users message or question to RenaissanceBot")

    message_history: list[ModelMessage] = []

    model_config = {
        "json_schema_extra": {"example": {"question": "Tell me a joke dear RenaissanceBot"}}
    }

class ChatResponse(BaseModel):
    response: str = Field(
        description="RenaissanceBots response including a renaissance joke and emojis")

    message_history: list[ModelMessage] = []