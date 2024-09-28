import sys
sys.path.append('.')
from luma_ai.video_generator import VideoGenerator

# Example of how to use the VideoGenerator
async def main():
    video_gen = VideoGenerator()
    result = await video_gen.process_text("Create a video of a sunset over the ocean.")
    got_result = False
    while not got_result:
        got_result = await video_gen.get_result(result.id)
    print(got_result)


# Running the main function
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())