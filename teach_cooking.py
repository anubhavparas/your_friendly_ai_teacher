import streamlit as st

from tutorial_widget import render_input_form
from constants import COOKING_TEACHER


async def render_cooking_teacher():
    """
    Renders a widget corresponding to science teacher.
    """
    await render_input_form(teacher_type=COOKING_TEACHER, sample_question="How to make a cheese pizza?")

    
