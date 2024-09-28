# Import the InstructionGenerator class from the file
from instruction_generator import InstructionGenerator

# Initialize the InstructionGenerator (no need to pass the API key explicitly)
instruction_generator = InstructionGenerator()

# Generate instructions with a prompt
prompt = "how to conduct a litmus test on lemon juice"
role = "science tutor"
instructions = instruction_generator.get_instructions(prompt=prompt, role=role, word_limit=10)

# Display the result
print(instructions)