import sys
sys.path.append('.')
from text2vid.text2video import Text2Video

# Example of how to use the VideoGenerator
async def main():
    video_gen = Text2Video()
    result = await video_gen.process_text("Create a video of painting instructions.")
    got_result = False
    while not got_result:
        state, result = await video_gen.get_result(result.id)
        if state is 'completed':
            got_result = True
    print(got_result)


# Running the main function
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())