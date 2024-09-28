from re import I
import sys
sys.path.append('.')
from text2vid.instruction2video import Instruction2Video

# Example of how to use the VideoGenerator
async def main():
    video_gen = Instruction2Video()
    instruction_list = ['Gather required cooking ingredients for making pizza', 'Create pizza dough by mixing for making pizza', 'Knead dough until smooth for making pizza', 'Let dough rest and rise for making pizza', 'Preheat the oven to 475F for making pizza', 'Roll dough into desired shape for making pizza', 'Spread pizza sauce evenly on dough for making pizza', 'Sprinkle cheese on top of sauce for making pizza', 'Add toppings of your choice for making pizza', 'Drizzle olive oil on pizza for making pizza', 'Bake in the preheated oven for making pizza', 'Check pizza regularly while baking for making pizza', 'Cook until crust is golden for making pizza', 'Remove pizza from oven for making pizza', 'Cut the pizza into slices for making pizza']
    await video_gen.process_instructions(instruction_list)
    await video_gen.aggregate_result()
    generations = video_gen.all_generations
    video_gen.download_videos()


# Running the main function
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())