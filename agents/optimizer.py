class Optimizer:

    @staticmethod
    def refine_prompt(original_prompt: str, issue: str):

        return original_prompt + f"""

IMPORTANT:
Your previous output had this issue: {issue}

Fix the issue.
Ensure STRICT JSON compliance.
"""