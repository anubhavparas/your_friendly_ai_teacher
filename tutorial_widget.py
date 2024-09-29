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
    



async def get_videos_from_instructions(tutorial_instructions: List[str]) -> List[VideoInstructionGeneration]:
    """
    Call Luma AI API to get the generated.
    :param tutorial_instructions: text instructions for the task to be learnt.
    """
    # TODO (sakshi): Integrate the call to get the generated video.
    video_gen = Instruction2Video()
    await video_gen.process_instructions(tutorial_instructions)
    await video_gen.aggregate_result()
    generations = video_gen.all_generations    
    return generations



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


         


