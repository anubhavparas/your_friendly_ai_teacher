import streamlit as st

from tutorial_widget import render_input_form
from constants import SCIENCE_TEACHER


async def render_science_teacher():
    """
    Renders a widget corresponding to science teacher.
    """
    await render_input_form(teacher_type=SCIENCE_TEACHER, sample_question="How does Acid-Base Titration work?")

    
