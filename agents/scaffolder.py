from pathlib import Path
from task_context.risk_boundaries import RISK_BOUNDARIES


class Scaffolder:

    @staticmethod
    def load_system_role():
        """
        Load the system role definition from system_role.txt
        """
        role_path = Path("task_context/system_role.txt")

        with open(role_path, "r") as file:
            return file.read()

    @staticmethod
    def build_prompt(symptoms: str):

        system_role = Scaffolder.load_system_role()

        prompt = f"""
            {system_role}
            
            --------------------------------------------------
            
            RISK CLASSIFICATION BOUNDARIES:
            
            Low: {RISK_BOUNDARIES['Low']}
            Moderate: {RISK_BOUNDARIES['Moderate']}
            High: {RISK_BOUNDARIES['High']}
            
            --------------------------------------------------
            
            PATIENT SYMPTOMS:
            
            {symptoms}
            
            --------------------------------------------------
            
            INSTRUCTION:
            
            Analyze the symptoms carefully and produce the structured JSON output
            defined in the system role instructions.
            """

        return prompt