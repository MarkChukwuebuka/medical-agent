from pathlib import Path

from services.pubmed import fetch_pubmed_context
from task_context.risk_boundaries import RISK_BOUNDARIES


class Scaffolder:

    @staticmethod
    def load_system_role():
        with open("task_context/system_role.txt", "r") as file:
            return file.read()

    @staticmethod
    def build_prompt(symptoms: str):

        system_role = Scaffolder.load_system_role()

        # 🔥 NEW: fetch PubMed context
        pubmed_context = fetch_pubmed_context(symptoms)

        prompt = f"""
            {system_role}
            
            --------------------------------------------------
            
            RISK CLASSIFICATION BOUNDARIES:
            
            Low: {RISK_BOUNDARIES['Low']}
            Moderate: {RISK_BOUNDARIES['Moderate']}
            High: {RISK_BOUNDARIES['High']}
            
            --------------------------------------------------
            
            EXTERNAL MEDICAL CONTEXT (PubMed):
            
            {pubmed_context}
            
            --------------------------------------------------
            
            PATIENT SYMPTOMS:
            
            {symptoms}
            
            --------------------------------------------------
            
            IMPORTANT INSTRUCTION:
            
            Based on the symptoms AND the external medical context:
            
            1. Estimate infection probability
            2. Classify risk level
            3. Suggest MOST LIKELY SUSPECTED INFECTION (non-diagnostic)
            4. Provide explanation
            5. Recommend next steps
            
            STRICT RULE:
            - The suspected infection must be expressed as "Possible infection"
            - Do NOT present it as confirmed diagnosis
            
            --------------------------------------------------
            
            OUTPUT FORMAT:
            
            {{
              "Infection_Probability": "percentage",
              "Risk_Level": "Low | Moderate | High",
              "Suspected_Infection": "possible infection name",
              "Explanation": "reasoning using symptoms + context",
              "Recommended_Action": "next step"
            }}
            """

        return prompt