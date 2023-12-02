import streamlit as st
st.set_page_config(page_title="RecipeGPT", page_icon='🫕', layout='wide')
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.colored_header import colored_header
from annotated_text import annotated_text as at
from streamlit_extras.colored_header import colored_header
import openai
from backend import get_response_stream
from personas import cuisines, dramatis_personae, all_cuisines, all_audiences


st.title("🥔🥕🍅⇢🤔⇢🤖⇢👩‍🍳👨‍🍳🍳")
st.subheader(" Use ChatGPT as your personal Culinary Developer!")
st.write('Give ChatGPT a list of ingredients and your culinary preferences, get an easy-to-follow recipe for a great dish!')
st.write('*One thing to note... this recipe generator does NOT a memory. Every time send a message to it, it is reacting '
         'as if speaking to you for the first time. If the AI gives you a recipe you would like to tweak, '
         'try copy-pasting the recipe into the actual [OpenAI ChatGPT interface.](https://chat.openai.com/)*')
colored_header(label="", description="", color_name="orange-70")

openai.api_key = st.secrets["OPENAI_API_KEY"]

# st.subheader('Trained on the 2013 Edition.')

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

leftcol, rightcol = st.columns([1,1])

# ### LEFT COLUMN ####
with leftcol:
    cuisine_choice = st.selectbox(label="Choose a style of cuisine for your recipe!",
                                  index=0, options=cuisines, key='selected_cuisine',
                                  help='The AI is most likely to use all and only the ingredients you entered if you select "Anything is fine. "'
                                       "If you select a specific cuisine, the AI will assume you have basic ingredients for that cuisine"
                                       " - for example, if you select Italian the AI will assume you have basil and garlic, and if you select Korean, the AI will assume you have gochujang.")
with rightcol:
    # Call the function at the end of your script
    audience_choice = st.radio(label="Please select a target audience for your recipe!", index=0, options=dramatis_personae,
             key='selected_audience', help="The default 'working professional' is perfect for when you're busy but want something delicious.")

advanced_options = st.expander("Advanced options")

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
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Potatoes, carrots, tomatoes", max_chars=500):
    # Save the message to the chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

# Provide chatbot response
    with st.chat_message('assistant'):
        message_placeholder = st.empty()
        full_response = ''
        for response in get_response_stream(
                ingredients_list=prompt,
                model='gpt-3.5-turbo',
                target_cuisine=all_cuisines[cuisine_choice],
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





# def add_logo():
#     if dessert:
#         st.markdown(
#             """
#             <style>
#                 [data-testid="stSidebarNav"] {
#                     background-image: url(http://placekitten.com/200/200);
#                     background-repeat: no-repeat;
#                     padding-top: 120px;
#                     background-position: 20px 20px;
#                 }
#                 [data-testid="stSidebarNav"]::before {
#                     content: "My Company Name";
#                     margin-left: 20px;
#                     margin-top: 20px;
#                     font-size: 30px;
#                     position: relative;
#                     top: 100px;
#                 }
#             </style>
#             """,
#             unsafe_allow_html=True,
#         )
#
# add_logo()