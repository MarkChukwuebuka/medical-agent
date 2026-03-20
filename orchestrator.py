from agents.scaffolder import Scaffolder
from agents.supervisor import Supervisor
from agents.optimizer import Optimizer
from agents.documenter import Documenter
from llm import call_llm

class InfectAI:

    @staticmethod
    def assess(symptoms: str):

        prompt = Scaffolder.build_prompt(symptoms)

        response = call_llm(prompt)

        validation = Supervisor.validate(response)

        if not validation["valid"]:
            prompt = Optimizer.refine_prompt(prompt, validation["issue"])
            response = call_llm(prompt)

        Documenter.log(prompt, response)

        return response