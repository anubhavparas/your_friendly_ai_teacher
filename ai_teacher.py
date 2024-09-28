import streamlit as st
import time
from teach_science import render_science_teacher
from teach_art import render_art_teacher
from teach_cooking import render_cooking_teacher
import asyncio


from constants import (
    SCIENCE_TEACHER,
    ART_TEACHER,
    COOKING_TEACHER
)

def typewriter(text: str, speed: int = 5):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.markdown(curr_full_text)
        time.sleep(1 / speed)

    

TEACHERS = {
    SCIENCE_TEACHER: render_science_teacher,
    ART_TEACHER: render_art_teacher,
    COOKING_TEACHER: render_cooking_teacher,
}

async def run_app() -> None:
    """
    Launches the app.
    """

    st.header(":raising_hand: Meet Your Friendly AI Teacher! :teacher:")
    intro_text = "Learn something new today! :pencil:"
    typewriter(text=intro_text)

    science_teacher, art_teacher, cooking_teacher = st.tabs(
        [SCIENCE_TEACHER, ART_TEACHER, COOKING_TEACHER]
    )

    with science_teacher:
        await render_science_teacher()
    
    with art_teacher:
        await render_art_teacher()
    
    with cooking_teacher:
        await render_cooking_teacher()



# Running the main function
if __name__ == "__main__":
    asyncio.run(run_app()
)