import os
import requests
import base64
from PIL import Image
from io import BytesIO
import re

def extract_title(recipe_text):
    output = re.findall('^.*Recipe Title:.*$', recipe_text, re.MULTILINE)[0].strip().split('Recipe Title:')
    title = output[1]
    return title

"""Here's two styles of image generation - Barefoot Contessa, or modern social media. 
Comment out the one you don't want to use."""

# # Barefoot contessa style:
# def get_stabilityai_image(recipe_title):
#     url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
#
#     # Updated request body with new parameters
#     body = {
#         "steps": 20,
#         "width": 512,
#         "height": 512,
#         "seed": 0,  # You can randomize this if you want different results each time
#         "cfg_scale": 5,
#         "samples": 1,
#         "style_preset": "photographic",
#         "text_prompts": [
#             {
#                 "text": f"Crystal clear, high clarity award-winning cookbook cover photograph of a tantalizing dish of {recipe_title}, "
#                         f"alone on a rustic wooden table, close-up photograph, outdoors in Tuscany on a cloudy day.",
#                 "weight": 1
#             },
#             {
#                 "text": "Multiple dishes, empty table, zoomed out, blurry, out of focus",
#                 "weight": -1
#             }
#         ],
#     }
#
#     # Updated headers with the API key
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {os.getenv('STABILITY_KEY')}",
#     }
#
#     # Check for non-200 response
#     response = requests.post(url, headers=headers, json=body)
#
#     if response.status_code != 200:
#         raise Exception("Non-200 response: " + str(response.text))
#
#     data = response.json()
#
#     # Assuming you want only the first generated image
#     image_data = data["artifacts"][0]["base64"]
#     image = Image.open(BytesIO(base64.b64decode(image_data)))
#
#     return image
#

# Modernist bon appetit style:
def get_stabilityai_image(recipe_title):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

    # Updated request body with new parameters
    body = {
        "steps": 20,
        "width": 1024,
        "height": 1024,
        "seed": 0,  # You can randomize this if you want different results each time
        "cfg_scale": 5,
        "samples": 1,
        "style_preset": "photographic",
        "text_prompts": [
            {
                "text": f"High clarity, modernist cookbook cover photograph of {recipe_title}. Top-down photograph "
                        f"showcasing the dish on a plate, placed on a plain metal background, highlighting the vibrant colors and textures of the food.",
                "weight": 1
            },
            {
                "text": "Multiple dishes, empty table, zoomed out, blurry, out of focus",
                "weight": -1
            }
        ],
    }

    # Updated headers with the API key
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('STABILITY_KEY')}",
    }

    # Check for non-200 response
    response = requests.post(url, headers=headers, json=body)

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    # Assuming you want only the first generated image
    image_data = data["artifacts"][0]["base64"]
    image = Image.open(BytesIO(base64.b64decode(image_data)))

    return image

