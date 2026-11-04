from pydantic_ai import Agent
from aimodules.helpers import nvidia_model
from dotenv import load_dotenv
from data_models import ChatRequest, ChatResponse

load_dotenv()

ai_model = nvidia_model()

chat_agent = Agent(
    ai_model,
    system_prompt="Be a joking programming nerd, always answer with a joke, Also addin some emojis to make it funnier"
)

async def chat(request: ChatRequest):
    result = await chat_agent.run(
        request.question, message_history=request.message_history
    )

    return ChatResponse(
        response = result.output, message_history = result.all_messages()
    )