import logfire
from logfire import VariablesOptions
from dotenv import load_dotenv

load_dotenv()

logfire.configure(variables=VariablesOptions)

def get_prompt(name: str, default: str = "You are a jokey assistant", lable: str = "latest"):
    prompt = logfire.var(name=f"prompt__{name}", type=str, default=default)
    prompt.refresh_sync(force=True)
    resolved = prompt.get(label=lable)
    return resolved.value

if __name__ == "__main__":
    prompt = get_prompt("career_agent_instructions", lable="Staging")
    print(prompt)