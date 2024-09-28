from re import I
import sys
sys.path.append('.')
from text2vid.instruction2video import Instruction2Video

# Example of how to use the VideoGenerator
async def main():
    video_gen = Instruction2Video()
    instruction_list = ['Drip juice on litmus paper for litmus test', 
                        'Ensure safety: Wear lab coat, gloves for litmus test']
    await video_gen.process_instructions(instruction_list)
    await video_gen.aggregate_result()
    generations = video_gen.all_generations
    video_gen.download_videos()


# Running the main function
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())