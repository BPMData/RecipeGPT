import streamlit as st
st.set_page_config(page_title="RecipeGPT", page_icon='🫕', layout='wide')
from streamlit_extras.colored_header import colored_header
import openai
from backend import get_response_stream, look_at_pix, encode_image_from_bytes
from personas import cuisines, dramatis_personae, all_cuisines, all_audiences
from image_backend_2 import get_stabilityai_image, extract_title
import random
from streamlit_extras.switch_page_button import switch_page
from backend import send_email_html
import markdown2



st.write('''<style>
[data-testid="column"] {
    width: calc(33.3333% - 1rem) !important;
    flex: 1 1 calc(33.3333% - 1rem) !important;
    min-width: calc(33% - 1rem) !important;
}
</style>''', unsafe_allow_html=True)

st.title("🥔🥕🍅🤔⇢🤖⇢👩‍🍳👨‍🍳🍳")
st.subheader(" Use ChatGPT as your personal Culinary Developer!")



# head1, head2, head3 = st.columns([2,1,1])
# with head1:
#     st.write('Give ChatGPT a list of ingredients and your culinary preferences, get an easy-to-follow recipe for a great dish!')
# with head2:
#     contact_me = st.button("Contact me!")
#     if contact_me:
#         switch_page("📮 contact me")
# with head3:
#     check_me_out = st.button("Other stuff I've made!")
#     if check_me_out:
#         switch_page("👀 other things i've made")
st.write(
    'Give ChatGPT a list of ingredients and your culinary preferences, get an easy-to-follow recipe for a great dish!')

head1, head2 = st.columns([1,1])
with head1:
    contact_me = st.button("Contact me or report a bug!")
    if contact_me:
        switch_page("📮 contact me")
with head2:
        check_me_out = st.button("Other stuff I've made!")
        if check_me_out:
            switch_page("👀 other things i've made")

colored_header(label="", description="", color_name="orange-70")

openai.api_key = st.secrets["OPENAI_API_KEY"]
recipe_provided = False
# st.subheader('Trained on the 2013 Edition.')

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

def suprise_me_clicked():
    st.session_state.suprise_me_selected = True

def intentional_cuisine_choice():
    st.session_state.suprise_me_selected = None

leftcol, rightcol = st.columns([1,1])

# ### LEFT COLUMN ####
with leftcol:
    cuisine_choice = st.radio(label="Choose a style of cuisine for your recipe!",
                                  index=0, options=cuisines, key='selected_cuisine',
                                  help='The AI is most likely to use all and only the ingredients you entered if you select "Nothing in particular. "'
                                       "If you select a specific cuisine, the AI will assume you have basic ingredients for that cuisine"
                                       " - for example, if you select Italian the AI will assume you have basil and garlic, and if you select Korean, the AI will assume you have gochujang.",
                                  on_change=intentional_cuisine_choice)
    suprise_me = st.button(label="Surprise me!", on_click=suprise_me_clicked)

    if not st.session_state.get("suprise_me_selected", None):
        cuisine_to_use = all_cuisines[cuisine_choice]
    if st.session_state.get("suprise_me_selected", None):
        random_cuisine = random.choice(cuisines)
        cuisine_to_use = all_cuisines[random_cuisine]
        st.warning("The recipe generated will be in the style of a randomly selected cuisine!")

with rightcol:
    # Call the function at the end of your script
    audience_choice = st.radio(label="Please select a target audience for your recipe!", index=0, options=dramatis_personae,
             key='selected_audience', help="The default 'working professional' is perfect for when you're busy but want something delicious.")

advanced_options = st.expander("Advanced options (Optional)")

dessert = advanced_options.toggle("Dessert?", key='sweets')
if dessert is True:
    advanced_options.write("The AI will try to make a dessert using the ingredients provided.")
if dessert is False:
    advanced_options.write("The AI will try to make an entree using the ingredients provided.")


dietary_needs = advanced_options.multiselect("Dietary restrictions?", help="Note that the AI is NOT a dietician, a nutritionists, or indeed, a human being. Do NOT rely on AI in the case of life-threatening allergies!",
                                             default=None, options=["Kosher", "Halal", "Gluten-free", "Keto", "Vegetarian",
                                                                    "Vegan", "Free of major food allergens", "Low calorie", "Diabetic"],
                                             placeholder = "Choose up to three options", max_selections=3,
                                             key='dietary_restrictions')
if dietary_needs:
    advanced_options.warning("Please note that the AI can struggle with fulfilling dietary restrictions; use caution and common sense. ChatGPT is NOT medical advice.")

must_not_include = advanced_options.text_input(value=None, label="Enter a list of ingredients that should NOT be used in the dish. Please hit enter when finished typing or the AI will disregard this input.", max_chars=200, key='must_not',
                                               placeholder="For example: peanuts, shellfish", help="Note that the AI is NOT a dietician, a nutritionists, or indeed, a human being. Do NOT rely on AI in the case of life-threatening allergies!")
if must_not_include:
    advanced_options.warning("Please double-check the recipe generated to make sure it omits the unwanted ingredients. THE AI CAN AND WILL MAKE MISTAKES.")

slider_temperature = advanced_options.slider(label="Change the temperature ('creativity') of the AI from the default of 0.7. At 0.00, you should get the exact same recipe every time for the same selections.",
                                      help="Temperature can actually go up to 2.0, but above 1.4 things break down frequently. Even at 1.4 things break down frequently.",
                                      min_value=0.0, max_value = 1.4, value=0.7, step=0.05)
advanced_options.warning("If you're looking here in the first place, you might like to know that you can also try to guide the AI to create a specific dish by listing the type of dish you want as an ingredient in the chatbox. For example, if you have chicken, spinach and walnuts and want a salad, enter 'salad, chicken, spinach, walnuts'. If you want a stir fry, enter 'stir-fry, chicken, spinach, walnuts.'")

pix_interface = st.expander("Try taking a picture of your fridge, pantry or groceries instead!")

def clicked():
    st.session_state.you_clicked_it = True
    st.session_state.image_used = False

pix = pix_interface.camera_input(label="Make sure you've selected  your desired target cuisine and audience before taking a picture.",
                help="Uses your phone camera (mobile) or webcam (desktop).", key="photo_data", on_change=clicked)

if pix is not None:
    st.warning("To take another photo, press 'Clear photo' above.")

if st.session_state.get("photo_data", None) is None:
    st.session_state.vision_used = False

gpt_vision = None
bytes_data = ""
if pix is not None and st.session_state.get("vision_used", False) is False:
    # To read image file buffer as bytes:
    bytes_data = pix.getvalue()
    base64_image = encode_image_from_bytes(bytes_data)

    if base64_image:
        gpt_vision = look_at_pix(base64_image)
        st.session_state.vision_used = True

st.info('*One thing to note... this recipe generator does NOT have a memory. To tweak a recipe, '
         "try copy-pasting the recipe to [OpenAI's ChatGPT interface.](https://chat.openai.com/)*")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = ""

# Only show chat input if gpt_vision is not available
if gpt_vision is None or st.session_state.get("you_clicked_it", False) is False:
    prompt = st.chat_input("Potatoes, carrots, tomatoes", max_chars=500, key="if_chatbox")
if st.session_state.get("vision_used", False) and st.session_state.get("image_used", False) is False:
    # If gpt_vision is available, use it as the prompt
    prompt = gpt_vision

# Ensure prompt is not empty
if prompt:
    # Save the message to the chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.image_used = True


# Provide chatbot response
    with st.chat_message('assistant'):
        message_placeholder = st.empty()
        full_response = ''
        for response in get_response_stream(
                ingredients_list=prompt,
                model='gpt-3.5-turbo',
                target_cuisine=cuisine_to_use,
                target_audience=all_audiences[audience_choice],
                must_nots=must_not_include,
                sweets=dessert,
                restrictions=dietary_needs,
                temperature = slider_temperature
        ):
            full_response += response
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    st.session_state.last_recipe = full_response  # Save the most recent recipe to this session key, and overwrite it every time.
    st.session_state.last_ingredients = prompt
    recipe_provided = True
    gpt_vision = None
    st.session_state.you_clicked_it = False
    st.session_state.generated_image = None
    st.session_state.you_clicked_it = None
    st.session_state.you_clicked_it_image = None
    st.session_state.suprise_me_selected = False



# Extract recipe title
recipe_title = False
if recipe_provided:
    try:
        recipe_title = extract_title(full_response)
        st.write(f"Recipe Title: {recipe_title}")
        st.session_state.recipe_title = recipe_title
    except IndexError:
        st.write("No recipe title found.")


def clicked2():
    st.session_state.you_clicked_it_image = True


if st.session_state.get("recipe_title", None):
    if st.session_state.get("generated_image", None) is None and not st.session_state.get("you_clicked_it_image", False):
        image_button = st.button("Click here to generate an image of your recipe!", key="stability_button", on_click=clicked2)

if st.session_state.get("you_clicked_it_image", None) and st.session_state.get("generated_image") is None:
    st.header(f"{st.session_state.recipe_title}")
    image = get_stabilityai_image(st.session_state.recipe_title)
    st.session_state.image_data = image
    st.session_state.generated_image = st.session_state.recipe_title
    st.session_state.you_clicked_it_image = None

if st.session_state.get("generated_image", False):
    st.image(st.session_state.image_data, caption=f"Generated Image for {st.session_state.recipe_title}")


st.divider()

if st.session_state.get("recipe_title", None):
    with st.form(key="sendmerecipe_form"):
        colored_header(label='I love it - E-mail myself this recipe/dish!', description="", color_name="orange-70")

        user_email = st.text_input("Enter your e-mail address here:", placeholder="The recipe and image, if any, will be sent to this address")

        email_subject = f"{user_email} has sent you a recipe for {st.session_state.recipe_title }"


        html2send = markdown2.markdown(st.session_state.last_recipe)
        st.session_state.recipe_converted_to_html = html2send

        formatted_message = f"""
        <html>
            <body>
                <p>Using the ingredients {st.session_state.last_ingredients}, <a href="https://recipesbygpt.streamlit.app">Recipes by GPT</a> created the following recipe for you!</p>
                <h2 style="font-weight: bold;">{st.session_state.recipe_title}</h2>

                <p>{html2send}</p>
                <p><b>Bon Appétit!</b></p>
                <p><i>This message was created by using <a href="https://recipesbygpt.streamlit.app">Recipes by GPT</a>. Please double-check the recipe before using it and use common sense. This recipe was created with generative AI and may be inaccurate or even unsafe.</i></p>
            </body>
        </html>
        """

        submit_button = st.form_submit_button("E-mail me this recipe!")
        if submit_button:
            image_to_attach = None
            if st.session_state.get("image_data", None):
                image_to_attach = st.session_state.image_data
            print("E-mail sent!")
            send_email_html(email_subject, user_email, formatted_message, image_to_attach)
            st.info(f"Your recipe for {st.session_state.recipe_title} was successfully e-mailed to {user_email}!")


# def display_session_state():
#     st.write("### Session State")
#     for key, value in st.session_state.items():
#         st.write(f"{key}: {value}")

# display_session_state()
