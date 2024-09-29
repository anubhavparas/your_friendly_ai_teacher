import requests
import time
from lumaai import LumaAI

client = LumaAI()

generation = client.generations.create(
  prompt="Monitor until golden then enjoy your masterpiece. for making pizza",
)
completed = False
while not completed:
  generation = client.generations.get(id=generation.id)
  if generation.state == "completed":
    completed = True
    print(generation.assets.video)
  elif generation.state == "failed":
    raise RuntimeError(f"Generation failed: {generation.failure_reason}")
#   print("Dreaming")
  time.sleep(3)

video_url = generation.assets.video

# download the video
response = requests.get(video_url, stream=True)
with open(f'{generation.id}.mp4', 'wb') as file:
    file.write(response.content)
print(f"File downloaded as {generation.id}.mp4")