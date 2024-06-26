import smtplib
import litellm
import openai
from personas import generate_prompt, all_cuisines, all_audiences, all_restrictions
import re
import os
# import shutil
import base64
import requests
from litellm import completion
# from tenacity import retry, wait_random_exponential, stop_after_attempt
import streamlit as st
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from io import BytesIO

litellm.set_verbose=True



# @retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
def get_response_stream(ingredients_list, model='gpt-3.5-turbo', temperature=0.7, tokens=3000, target_audience=all_audiences['A working professional.'],
                 target_cuisine=all_cuisines["Nothing in particular"], model_to_use="gpt-3.5-turbo",
                        must_nots="", sweets=False, restrictions=[]):
    try:
        # Initialize must_not_text
        must_not_text = ""

        # Include must_not_text if it's provided
        if must_nots:
            must_not_text = (f"In addition, it is VERY IMPORTANT that the recipe you create does NOT include any of the following: {must_nots}. "
                             f"In your response, mention that you are aware of these restrictions and took them into account.")

        response = completion(
            model=model_to_use,
            messages=[{"content": generate_prompt(target_audience, target_cuisine, dessert=sweets, dietary_restrictions=restrictions), "role": "system"},
                      {"content": f'The ingredients list is: """{ingredients_list}.""" If the ingredients list directly above is empty or contains no food items, or is a phrase such as I am sorry, I cannot help with that request", DO NOT generate a recipe. Please reply that you are sorry, but you can only generate a recipe if given ingredients in the first place.'                                                                                                                                                                                                                                                                                                         
                                  'If the ingredients list is long, indicating perhaps everything the user has in their '
                                  'fridge or bought while grocery shopping, simply choose a few ingredients that you think would make the best dish and use those. '
                                  'Before you begin generating your recipe, double check the ingredients list to make sure '
                                  'you understood the ingredients properly. For example, chicken or beef broth is a liquid, not the meat itself. If you have only broth, you cannot make a meat dish. '
                                  f'{must_not_text}'
                                  f'Introduce yourself and the dish to your fellow foodies first, but when you get to the recipe itself, assign a title to the recipe beginning with'
                                  f'the exact string "Recipe Title: " to the recipe.', "role": "user"}],
        max_tokens = tokens,
        temperature = temperature,
        stream = True,
        num_retries=3
        )
        print()
        for chunk in response:
            yield (chunk['choices'][0].delta.content or '')
    except openai.APITimeoutError as e:
        print(f"Exception {e} raised, retrying....")

def get_response(ingredients_list, model='gpt-3.5-turbo', temperature=0.7, tokens=2000, target_audience=all_audiences['A working professional.'],
                 target_cuisine=all_cuisines["Nothing in particular"], model_to_use="gpt-3.5-turbo"):
    response = completion(
        model=model_to_use,
        messages=[{"content": generate_prompt(target_audience, target_cuisine), "role": "system"},
                  {"content": f'The ingredients list is: """{ingredients_list}"""'
                              "If the ingredients list is empty or contains no food items, or is a phrase such as 'I'm sorry, I can't help with that request', please reply that you are sorry, but you can only generate a recipe if given ingredients in the first place."
                              'If the ingredients list is long, indicating perhaps everything the user has in their '
                              'fridge or bought while grocery shopping, simply choose a few ingredients that you think would make the best dish and use those. '
                              'Before you begin generating your recipe, double check the ingredients list to make sure '
                              'you understood the ingredients properly. For example, chicken or beef broth is a liquid, not the meat itself. If you have only broth, you cannot make a meat dish. '
                              f' Introduce yourself and the dish to your fellow foodies first, but when you get to the recipe itself, assign a title to the recipe beginning with'
                              f'the exact string "Recipe Title: " to the recipe.', "role": "user"}],
    max_tokens = tokens,
    temperature = temperature,
    stream = False,
    )
    return response.choices[0].message.content


def extract_title(recipe_text):
    output = re.findall('^.*Recipe Title:.*$', recipe_text, re.MULTILINE)[0].strip().split('Recipe Title:')
    title = output[1]
    return title

def store_recipe(recipe, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(recipe)

def save_stabilityai_image(recipe_title):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-512-v2-1/text-to-image"

    body = {
        "steps": 15,
        "width": 512,
        "height": 512,
        "cfg_scale": 7,
        "samples": 1,
        "style_preset": "photographic",
        "text_prompts": [
            {
                "text": f"Crystal clear, high clarity award-winning cookbook "
                        f"cover photograph of a tantalizing dish of {recipe_title}, "
                        f"alone on a rustic wooden table, close-up photograph, outdoors "
                        f"in Tuscany on a cloudy day.",
                "weight": 1
            }
            , {
                "text": "Multiple dishes, empty table, zoomed out, blurry, out of focus",
                "weight": -1
            }
        ],
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('STABILITY_KEY')}",
    }

    response = requests.post(
        url,
        headers=headers,
        json=body,
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    for i, image in enumerate(data["artifacts"]):
        with open(f'./out/{recipe_title}_{image["seed"]}.png', "wb") as f:
            f.write(base64.b64decode(image["base64"]))
    return data

def generate_stabilityxl_image(recipe_title):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
    body = {
      "steps": 20,
      "width": 1024,
      "height": 1024,
      "seed": 0,
      "cfg_scale": 5,
      "samples": 1,
      "style_preset": "photographic",
      "text_prompts": [
        {
          "text": "Crystal clear, high clarity award-winning cookbook cover photograph of a tantalizing dish of Spicy Korean Tilapia with Kimchi Fried Rice!, alone on a rustic wooden table, close-up photograph, outdoors in Tuscany on a cloudy day.\n",
          "weight": 1
        },
        {
          "text": "Multiple dishes, empty table, zoomed out, blurry, out of focus",
          "weight": -1
        }
      ],
    }

    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json",
      "Authorization": "Bearer YOUR_API_KEY",
    }

    response = requests.post(
      url,
      headers=headers,
      json=body,
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    # make sure the out directory exists
    if not os.path.exists("./out"):
        os.makedirs("./out")

    for i, image in enumerate(data["artifacts"]):
        with open(f'./out/txt2img_{image["seed"]}.png', "wb") as f:
            f.write(base64.b64decode(image["base64"]))

    return data


"""Alternate prompts:

+
Crystal clear, high clarity award-winning modernist cookbook cover photograph of a tantalizing dish of Spicy Korean Tilapia with Kimchi Fried Rice!, top down photograph, plate on top of plain metal background

OR

High clarity, modernist cookbook cover photograph of a spicy Korean Tilapia dish with Kimchi Fried Rice. The image is a top-down photograph showcasing the dish on a plate, placed on a plain metal background, highlighting the vibrant colors and textures of the food.

OR
High clarity, modernist cookbook cover photograph of a spicy Korean Tilapia dish with Kimchi Fried Rice. Top-down photograph showcasing the dish on a plate, placed on a plain metal background, highlighting the vibrant colors and textures of the food.

OR
Vibrant, delicious, high clarity, modernist cookbook cover photograph of a spicy Korean Tilapia dish with Kimchi Fried Rice. Top-down photograph showcasing the dish on a plate, placed on a plain metal background, highlighting the vibrant colors and textures of the food.

-
Multiple dishes, empty table, zoomed out, blurry, out of focus, silverware, knife, fork, spoon
"""
def send_email(message=""):
    host = "smtp.gmail.com"
    port = 465
    sender_username = "bryan.patrick.a.murphy@gmail.com"
    # password = os.getenv("WebPortfolio_Password")
    password = st.secrets["GMAIL_SEND_KEY"]

    recipient = "bryan.patrick.a.murphy@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_username, password)
        server.sendmail(sender_username, recipient, message)

def send_email_html(subject, recipe_recipient, message="", image=None):
    host = "smtp.gmail.com"
    port = 465
    sender_username = "bryan.patrick.a.murphy@gmail.com"
    password = st.secrets["GMAIL_SEND_KEY"]

    recipient = recipe_recipient

    context = ssl.create_default_context()

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender_username
    msg["To"] = recipient

    html = MIMEText(message, "html")

    msg.attach(html)

    # Everything below is new for the image attachment process
    # Attach the image if provided
    if image is not None:
        # Convert the PIL image to a byte stream
        img_byte_arr = BytesIO()
        image.save(img_byte_arr, format=image.format)
        img_byte_arr = img_byte_arr.getvalue()

        # Create a MIMEImage object and attach it to the email
        img_attachment = MIMEImage(img_byte_arr, name='Recipe.png')
        msg.attach(img_attachment)
    # Everything above is new for the image attachment process

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_username, password)
        server.sendmail(sender_username, recipient, msg.as_string())


def look_at_pix(base64_image):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {st.secrets['OPENAI_API_KEY']}"
    }
    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        # "text": "What’s in this image?"
                        "text": """You are being tasked with helping a recipe-creation LLM to create recipes based on the ingredients seen in a photograph. You are looking at a picture of food items on a table.  You are going to list only the items you see, without commentary. For example, a good response would be:
  "Milk, carrots, eggs, bell peppers, mushrooms."
  A bad response would be:
  "A carton of eggs, which can be used in multiple recipes, from omelets to baked dishes.
  A bottle of milk, a staple for many recipes including sauces, batters, and baked goods.
  Fresh vegetables, including carrots, bell peppers, mushrooms, tomatoes, and broccoli, suitable for salads, stir-fries, or roasting.
  Fruits such as apples and lemons, which could be used for desserts, juices, or flavoring dishes.
  A loaf of bread, likely a baguette, which can be served as a side or used in sandwiches and bread puddings.
  Various herbs and spices in jars, which are essential for flavoring any dish."
  What food items or potential recipe ingredients do you see in this photo?
  """
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()['choices'][0]['message']['content']
    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()  # Check if the request was successful
        response_data = response.json()
        if 'choices' in response_data:
            return response_data['choices'][0]['message']['content']
        else:
            print("Response does not contain 'choices' key")
            return "An unexpected response was received from the API."
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return "An error occurred while processing the image."
    except ValueError as e:
        print(f"Invalid response: {e}")
        return "An unexpected response was received from the API."

def encode_image_from_bytes(bytes_data):
    # Directly encode the bytes in base64
    return base64.b64encode(bytes_data).decode('utf-8')
