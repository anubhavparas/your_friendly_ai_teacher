import requests
import time
from lumaai import LumaAI

client = LumaAI()

# prompts = ['Preheat your oven to 475F for making pizza', 'Prepare all the needed ingredients for making pizza', 'Mix yeast, sugar and warm water for making pizza', 'After 10 minutes, add flour, salt for making pizza', 'Knead dough until smooth, elastic for making pizza', 'Let dough rest until doubled for making pizza', 'Roll dough into pizza shape for making pizza', 'Spread tomato sauce on dough for making pizza', 'Sprinkle cheese, add toppings for making pizza', 'Bake until golden and crispy for making pizza']

prompts = ['Gather your ingredients: dough, sauce, cheese, toppings. for making pizza', 'Pre-heat your oven to about 475 degrees F. for making pizza', 'Prepare your workspace, sprinkle some flour to avoid sticking. for making pizza', 'Take your dough and begin to flatten and shape it. for making pizza', 'Shape dough into your desired pizza shape and size. for making pizza', 'Coat the surface of your dough with a thin layer of olive oil. for making pizza', 'Spread the pizza sauce evenly over the dough surface. for making pizza', 'Sprinkle the shredded cheese uniformly over the sauce. for making pizza', 'Add your chosen toppings— veggies, meats, etc., evenly. for making pizza', 'Delicately transfer uncooked pizza onto a baking sheet. for making pizza', 'Place the baking sheet in the preheated oven. for making pizza', 'Bake the pizza for 15-20 minutes until crispy and golden. for making pizza', 'Allow the pizza to cool slightly after removing from oven. for making pizza', 'Slice the pizza into even pieces using a pizza cutter. for making pizza', 'Plate up the pizza slices and serve while still hot. for making pizza', 'Enjoy the delicious homemade pizza with friends or family. for making pizza']

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

# prompts = ["Preheat the oven for making the pizza", "Create pizza dough by mixing for making pizza"]

# generations = [generation0, generation1]

# print(generations)
# generations = [client.generations.create(prompt=prompt) for prompt in prompts]

completed = False
count = 0

prev_generation = None
for index, prompt in enumerate(prompts):
    # Get generation for tasks 0
    print(prompts[index])
    if prev_generation==None:
        generation = client.generations.create(prompt=prompts[index])
    else:
        frame = "frame" + str(index-1)
        generation = client.generations.create(prompt=prompts[index],
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



