from agents import coach_agent, ClientDeps
from pydantic_evals.evaluators import LLMJudge, Evaluator, EvaluatorContext
from dataclasses import dataclass
from pydantic_evals import Dataset, Case
from aimodules.helpers import nvidia_model

# 2 types of evals
# -Deterministic
# -LLM Judge

model = nvidia_model()

# deterministic
@dataclass
class WordCountLimit(Evaluator):
    limit: int

    def evaluate(self, ctx: EvaluatorContext[str, str]) -> bool:
        return len(ctx.output.split()) < self.limit


