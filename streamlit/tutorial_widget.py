import streamlit as st
from typing import List, Optional
import numpy as np
from dataclasses import dataclass

from your_friendly_ai_teacher.types import VideoInstructionGeneration




def call_llm(
        role: str, 
        task_query: str, 
        image_inp: Optional[np.ndarray] = None
    ) -> List[str]:
    # TODO (sapan): Integrate the call to LLM/VLM function and remove the dummy return.
    return ["Do 1, Do 2, Do 3"]
    

def get_videos_from_instructions(tutorial_instructions: List[str]) -> List[VideoInstructionGeneration]:
    """
    Call Luma AI API to get the generated.
    """
    # TODO (sakshi): Integrate the call to get the generated video.
    return [VideoInstructionGeneration()]



def get_tutorial_instructions(
        role: str, 
        task_query: str, 
        image_inp: Optional[np.ndarray] = None
    ) -> List[str]:
    """
    Calls LLM API to get the high level instructions to teach a task.
    """
    return call_llm(role, task_query, image_inp)








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

    tutorial_instructions = get_tutorial_instructions(
        role=role, task_query=task_query, image_inp=image_inp
    )
    video_instructions = get_videos_from_instructions(tutorial_instructions)

    for video_instruction in video_instructions:
        pass 


