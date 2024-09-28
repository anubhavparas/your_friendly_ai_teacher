import os
from openai import OpenAI
import ast
from typing import List, Optional

class InstructionGenerator:
    def __init__(self) -> None:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("API key is required and should be set as an environment variable 'OPENAI_API_KEY'")
        self.client = OpenAI(api_key=api_key)


    def get_instructions(self,
                         task_query: Optional[str] = None,
                         role: Optional[str] = None,
                         word_limit: int = 20,
                         model: str = "gpt-4"
                        ) -> Optional[List[str]]:
        # Construct the messages for the chat completion
        content_role = f"You are a {role}"
        content_prompt = f"Return a list of steps on {task_query}, just return the steps in python list with word limit {word_limit}, remove python code block fence, remove variable name, remove list number"

        try:
            # Create a chat completion
            completion = self.client.chat.completions.create(model=model,
            messages=[
                {"role": "system", "content": content_role},
                {"role": "user", "content": content_prompt}
            ])

            # Extract the response content
            response_content = completion.choices[0].message.content

            # Convert the string response to an actual Python list
            python_list = ast.literal_eval(response_content)
            return python_list

        except Exception as e:
            print(f"An error occurred: {e}")
            return None
