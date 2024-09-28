from os import lseek
from typing import List
from xml.sax.handler import all_properties
from custom_types import VideoInstructionGeneration
from luma_ai.video_generator import VideoGenerator

class InstructionGeneration:
    def __init__(self) -> None:
        self.vid_gen = VideoGenerator()
        self.all_generations = []

    async def process_instructions(self, text_instructions:List[str]) -> None:
        for text_instruction in text_instructions:
            video_generation = await self.vid_gen.process_text(text_instructions)
            self.all_generations.append(VideoInstructionGeneration(id=video_generation.id, url=None, tutorial_instruction=text_instruction))
    
    def aggregate_result(self):
        all_processed = False
        while not all_processed:
            check = True
            for i, generations in enumerate(self.all_generations):
                id = generations.id
                status = self.vid_gen.get_result(generation_id=id)
                if status.url is not None:
                    self.all_generations[i] = status
                    check = True
                else:
                    check = False
            all_processed = check
        print("Got results for all instructions...")
        




