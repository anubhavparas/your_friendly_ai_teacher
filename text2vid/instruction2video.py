from os import lseek
from typing import List
from xml.sax.handler import all_properties
from custom_types import VideoInstructionGeneration
from text2vid.text2video import Text2Video
import copy
import time

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
        start_t = time.time()
        while not all_processed:
            processed_idx = []
            for i, _ in enumerate(self.all_generations):
                generation_id = self.all_generations[i].id
                status, result = await self.vid_gen.get_result(generation_id=generation_id)
                if status == 'completed':
                    print(f"Generated for {result.tutorial_instruction}")
                    self.all_generations[i] = result  # Store completed results
                    processed_idx.append(i)

                if len(processed_idx) == len(self.all_generations):
                    all_processed = True
            current_t = time.time()
            elapsed_time = current_t - start_t 
            if elapsed_time > 3 * 60:
                print(elapsed_time)
                break
        print("Got results for all instructions...")

        




