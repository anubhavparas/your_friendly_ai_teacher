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
                         word_limit: int = 40,
                         model: str = "gpt-4",
                         n_steps: int = 5
                        ) -> Optional[List[str]]:
        # add prompts suggestions
        code_suggestions = ", just return the steps in python list" + ", remove python code block fence" + ", remove variable name" + ", remove list number" + ", reduce the size of list as much as possible"

        query_suggestions = ", use entire word limit" + ", be as descriptive as possible related to the task"
        
        import random
        tone = random.choice(['encouraging', 'patient', 'humorous', 'sarcastic', 'academic', 'friendly', 'authoritative', 'motivational', 'technical', 'conversational'])

        # Construct the messages for the chat completion
        content_role = f"You are a {role}"
        content_prompt = f"Return a list of {n_steps} steps for task: {task_query}, in {tone}, with word limit {word_limit} for each step" + code_suggestions + query_suggestions
        print ("content_prompt: ", content_prompt)

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

             # Append the task query (prompt) to each list item
            modified_list = [f"{item} for {task_query}" for item in python_list]
            return modified_list

        except Exception as e:
            print(f"An error occurred: {e}")
            return None
