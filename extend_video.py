import requests
import time
from lumaai import LumaAI

client = LumaAI()

steps = ['Preheat your oven to 475F for making pizza', 'Prepare all the needed ingredients for making pizza', 'Mix yeast, sugar and warm water for making pizza', 'After 10 minutes, add flour, salt for making pizza', 'Knead dough until smooth, elastic for making pizza', 'Let dough rest until doubled for making pizza', 'Roll dough into pizza shape for making pizza', 'Spread tomato sauce on dough for making pizza', 'Sprinkle cheese, add toppings for making pizza', 'Bake until golden and crispy for making pizza']

# generation0 = client.generations.create(
#     prompt="Preheat the oven for making the pizza"
# )

# generation1 = client.generations.create(
#     prompt="Create pizza dough by mixing for making pizza"
# )

# generation1 = client.generations.create(
#     prompt="Create pizza dough by mixing for making pizza",
#     keyframes={
#       "frame0": {
#         "type": "generation",
#         "id": generation0.id
#       }
#     }
# )  

prompts = ["Preheat the oven for making the pizza", "Create pizza dough by mixing for making pizza"]

# generations = [generation0, generation1]

# print(generations)
# generations = [client.generations.create(prompt=prompt) for prompt in steps]

completed = False
count = 0

prev_generation = None
for index, prompt in enumerate(prompts):
    # Get generation for tasks 0
    print(steps[index])
    if prev_generation==None:
        generation = client.generations.create(prompt=steps[index])
    else:
        frame = "frame" + str(index-1)
        generation = client.generations.create(prompt=steps[index],
                            keyframes={
                                frame: {
                                    "type": "generation",
                                    "id": prev_generation.id
                                }
                            }
        )
    
    video_generated = False
    while not video_generated:
        generation = client.generations.get(id=generation.id)

        if generation.state == "completed":
            count = count + 1
            video_url = generation.assets.video

            # download the video
            response = requests.get(video_url, stream=True)
            with open(f'{index}.mp4', 'wb') as file:
                file.write(response.content)
            print(f"File downloaded as {index}.mp4")
            video_generated = True

        elif generation.state == "failed":
            print("generation index: ", index)
            raise RuntimeError(f"Generation failed: {generation.failure_reason}")

        print("Dreaming index: ", index)
        time.sleep(3)
    
    prev_generation = generation



