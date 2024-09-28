# Import the InstructionGenerator class from the file
from instruction_generator import InstructionGenerator

# Initialize the InstructionGenerator (no need to pass the API key explicitly)
instruction_generator = InstructionGenerator()

# Generate instructions with a task_query
task_query = "litmus test on lemon juice"
role = "science tutor"
instructions = instruction_generator.get_instructions(task_query=task_query, role=role, word_limit=10)

# Display the result
print("\n", instructions)