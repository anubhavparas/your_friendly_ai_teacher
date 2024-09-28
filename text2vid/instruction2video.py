from os import lseek
from typing import List
from xml.sax.handler import all_properties
from custom_types import VideoInstructionGeneration
from text2vid.text2video import Text2Video

class Instruction2Video:
    def __init__(self) -> None:
        self.vid_gen = Text2Video()
        self.all_generations = []
    
    def download_videos(self):
        for i, gens in enumerate(self.all_generations):
            url = gens.url
            save_name = f"{i}.mp4"
            self.vid_gen.download_video(url, save_name)

    async def process_instructions(self, text_instructions:List[str]) -> None:
        for text_instruction in text_instructions:
            video_generation = await self.vid_gen.process_text(text_instruction)
            self.all_generations.append(VideoInstructionGeneration(id=video_generation.id, url=None, tutorial_instruction=text_instruction))
    
    async def aggregate_result(self):
        all_processed = False
        self.url_results = []

        while not all_processed:
            all_processed = True  # Assume all are processed unless proven otherwise
            to_remove = []  # List to keep track of indices to remove

            for i, generation in enumerate(self.all_generations):
                generation_id = generation.id
                status, result = await self.vid_gen.get_result(generation_id=generation_id)

                if status == 'completed':
                    print(f"Generated for {result.tutorial_instruction}")
                    self.url_results.append(result)
                    to_remove.append(i)  # Mark index for removal
                else:
                    all_processed = False  # Set to False if any are not completed

            # Remove completed generations after processing the current batch
            for index in reversed(to_remove):  # Remove in reverse to avoid index shifting
                del self.all_generations[index]

        self.all_generations = self.url_results
        print("Got results for all instructions...")
        




