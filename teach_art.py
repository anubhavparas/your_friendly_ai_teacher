import streamlit as st

from tutorial_widget import render_input_form
from constants import ART_TEACHER


def render_art_teacher():
    """
    Renders a widget corresponding to science teacher.
    """
    render_input_form(teacher_type=ART_TEACHER, sample_question="How to make a scenary with mountains?")

    
