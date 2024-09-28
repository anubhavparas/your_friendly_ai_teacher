import streamlit as st
from typing import List, Optional
import numpy as np
from dataclasses import dataclass

from your_friendly_ai_teacher.custom_types import VideoInstructionGeneration
from instruction_generator import InstructionGenerator




def call_llm(gpt_instructions_generator: InstructionGenerator,
        role: str, 
        task_query: str, 
        image_inp: Optional[np.ndarray] = None
    ) -> List[str]:   
    
    return gpt_instructions_generator.get_instructions(task_query=task_query, role=role)
    

def get_videos_from_instructions(tutorial_instructions: List[str]) -> List[VideoInstructionGeneration]:
    """
    Call Luma AI API to get the generated.
    """
    # TODO (sakshi): Integrate the call to get the generated video.
    dummy_instruction = VideoInstructionGeneration(id="1", url="https://storage.cdn-luma.com/lit_lite_inference_v1.6-xl/f3e0893e-9f22-42bb-87ef-30f0a78642f1/46f24df2-c6e8-42df-aead-9a4058e406df_video0d8e5285574c94fcc88e8c929964805de.mp4", tutorial_instruction="A teddy bear in sunglasses playing electric guitar and dancing")
    
    return [dummy_instruction, dummy_instruction, dummy_instruction]



def get_tutorial_instructions(gpt_instructions_generator: InstructionGenerator, 
        role: str, 
        task_query: str, 
        image_inp: Optional[np.ndarray] = None
    ) -> List[str]:
    """
    Calls LLM API to get the high level instructions to teach a task.
    """
    return call_llm(gpt_instructions_generator, role, task_query, image_inp)








def render_tutorial_instructions(
        role: str, 
        task_query: str, 
        image_inp: Optional[np.ndarray] = None
    ) -> List[str]:
    """
    Renders the widget with the tutorial instructions.
    :param role: role the AI teacher will take.
    :param task_query: task that the user wants to learn.
    :param image_inp: image-based user input.
    """
    gpt_instructions_generator = InstructionGenerator()

    tutorial_instructions = get_tutorial_instructions(gpt_instructions_generator=gpt_instructions_generator,
        role=role, task_query=task_query, image_inp=image_inp
    )
    video_instructions = get_videos_from_instructions(tutorial_instructions)

    for video_instruction in video_instructions:
        st.write(video_instruction.tutorial_instruction)
        st.video(video_instruction.url)

         


