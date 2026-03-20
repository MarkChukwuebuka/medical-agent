import json

class Supervisor:

    @staticmethod
    def validate(response: str):
        try:
            data = json.loads(response)
        except:
            return {"valid": False, "issue": "Invalid JSON format"}

        required_keys = [
            "Infection_Probability",
            "Risk_Level",
            "Explanation",
            "Recommended_Action"
        ]

        for key in required_keys:
            if key not in data:
                return {"valid": False, "issue": f"Missing {key}"}

        if data["Risk_Level"] not in ["Low", "Moderate", "High"]:
            return {"valid": False, "issue": "Invalid Risk Level"}

        return {"valid": True}