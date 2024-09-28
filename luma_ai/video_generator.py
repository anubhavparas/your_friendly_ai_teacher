from operator import ge
import sys
sys.path.append('.')
from custom_types import VideoInstructionGeneration
from lumaai import AsyncLumaAI
import os
import requests

class VideoGenerator:
    def __init__(self) -> None:
        self.client = AsyncLumaAI(auth_token=os.environ.get("LUMAAI_API_KEY"))

    async def process_text(self, text_input : str):
        generation = await self.client.generations.create(prompt=text_input)
        return generation

    async def get_result(self, generation_id : str)->VideoInstructionGeneration:
        generation_updated = await self.client.generations.get(id=generation_id)
        if generation_updated.state == 'completed':
            return VideoInstructionGeneration(id=generation_updated.id, url=generation_updated.assets.video, tutorial_instruction=generation_updated.request.prompt)
        else:
            return False