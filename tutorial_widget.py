import streamlit as st
from typing import List, Optional
import numpy as np
from dataclasses import dataclass

from custom_types import VideoInstructionGeneration
from instruction_generator import InstructionGenerator
from text2vid.instruction2video import Instruction2Video


async def render_input_form(teacher_type: str, sample_question: str) -> None:
     """
     Renders the widget to get the input.
     :param teacher_type: to define the type of AI teacher.
     :param sample_question: samples question/query for the task to be learnt.
     """

     with st.form(f"ai_teacher_form_{teacher_type}"):
        user_query = st.text_input("What do you want to learn today!", sample_question)
        role = teacher_type
        image_inp = None

        submitted = st.form_submit_button("Go!")
        if submitted:
            await render_tutorial_instructions(
            role=role,
            task_query=user_query,
        )


def call_llm(
        gpt_instructions_generator: InstructionGenerator,
        role: str, 
        task_query: str, 
        image_inp: Optional[np.ndarray] = None
    ) -> List[str]:
    return gpt_instructions_generator.get_instructions(task_query=task_query, role=role)
    


async def dummy():
    import time
    return 1; 

async def get_videos_from_instructions(tutorial_instructions: List[str]) -> List[VideoInstructionGeneration]:
    """
    Call Luma AI API to get the generated.
    :param tutorial_instructions: text instructions for the task to be learnt.
    """
    # TODO (sakshi): Integrate the call to get the generated video.
    await dummy()

    video1 = VideoInstructionGeneration(id="1", url="https://storage.cdn-luma.com/lit_lite_inference_v1.6-xl/69cd4891-c936-4033-8e5f-e7a4c7545746/d78f8c03-b476-468f-9d68-c1aff4d6a25b_video0a72d66451a844f93acbaa4754d614899.mp4", tutorial_instruction="Gather all fresh ingredients, check pizza dough's elasticity. for making pizza")
    video2 = VideoInstructionGeneration(id="2", url="https://storage.cdn-luma.com/lit_lite_inference_v1.6-xl/48d84f6a-3991-4288-8ea1-2107c562149b/655dbfbc-d2ac-4d7b-8108-361598315e95_video007579a7c4a2a41a7912b699769690a6f.mp4", tutorial_instruction="Spread tomato sauce wide, ensuring crust freedom. for making pizza")
    video3 = VideoInstructionGeneration(id="3", url="https://storage.cdn-luma.com/lit_lite_inference_v1.6-xl/f15ee156-98fa-400d-a8f4-91d6f9a1b4d0/2516a14b-2e8a-42e0-a13b-16f7328ba297_video003b343294e8846d688434d2599c1e1b4.mp4", tutorial_instruction="Amply distribute cheese and favorite toppings. for making pizza")
    video4 = VideoInstructionGeneration(id="4", url="https://storage.cdn-luma.com/lit_lite_inference_v1.6-xl/414bdc97-8e2c-41c1-8c07-3fb4c5df273c/b460d0aa-d6ad-475a-8753-27597f92d075_video0cc70069731b649788c6fa75610f43cab.mp4", tutorial_instruction="Masterfully slide pizza into preheated oven. for making pizza")
    video5 = VideoInstructionGeneration(id="5", url="https://storage.cdn-luma.com/lit_lite_inference_v1.6-xl/cdafd708-864b-4deb-b8ac-150dd083cd56/30adb6ae-2517-4dea-9b0b-ed4656f604b2_video0299d56758e544c8a9ec67b3a0e1ca665.mp4", tutorial_instruction="Monitor until golden then enjoy your masterpiece. for making pizza")
    
    return [video1, video2, video3, video4, video5]



def get_tutorial_instructions(
        gpt_instructions_generator: InstructionGenerator,
        role: str, 
        task_query: str, 
        image_inp: Optional[np.ndarray] = None
    ) -> List[str]:
    """
    Calls LLM API to get the high level instructions to teach a task.
    """
    return call_llm(gpt_instructions_generator, role, task_query, image_inp)



async def render_tutorial_instructions(
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

    video_instructions = None
    with st.spinner("Hmmm! Let me think how can I help you... :thinking_face:"):
    
        try:
            tutorial_instructions = get_tutorial_instructions(
                gpt_instructions_generator=gpt_instructions_generator,
                role=role, 
                task_query=task_query, 
                image_inp=image_inp
            )
            print(f"Text instructions generated : {len(tutorial_instructions)}!")
            video_instructions = await get_videos_from_instructions(tutorial_instructions)
            print(f"Video instructions generated!")
        except Exception as e:
            st.error(f"Sorry, something went wrong. Please try again. {e}", icon="🚨")

    if video_instructions is not None:
        for step, video_instruction in enumerate(video_instructions):
            st.write(f"{step + 1}. {video_instruction.tutorial_instruction}")
            if video_instruction.url is not None:    
                st.video(video_instruction.url)
            else: 
                st.warning("Can you imagine this instruction? :thinking_face:")


         


