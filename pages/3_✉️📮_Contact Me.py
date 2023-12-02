import streamlit as st
st.set_page_config(page_title="Contact the Coder", page_icon='✉️', layout='wide')
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.colored_header import colored_header
from backend import send_email


st.title("Contact Me:")


colored_header(label='About Me', description="", color_name="orange-70")
st.write("My name is Bryan, a data analyst and AI enthusiast based out of the Tri-State Area.")

st.write('You can reach me at BPMurphy.Data@gmail.com, or by using the form below.')

colored_header(label='Contact Me', description="", color_name="orange-70")

with st.form(key="contact_form"):
    user_email = st.text_input("Enter your e-mail address here:", placeholder="If you don't enter your real e-mail, I won't be able to get back to you...")
    interest = st.selectbox("What topic do you want to discuss?",
                            options=("Questions about this specific model", "Questions about building a chatbot",
                                     "Questions about Pomeranians", "General"))
    user_message = st.text_area("Enter your message to me here:", placeholder="Your message...")
    formatted_message = f"""Subject: {user_email} has reached out to you! \n

     They wrote:\n

     {user_message}
     \n\n
     They said they were interested in:\n
     {interest}.\n
     This message was sent by:\n
     {user_email}."""

    submit_button = st.form_submit_button("Send me your message!")
    if submit_button:
        print("e-mail sent!")
        send_email(formatted_message)
        st.info("Your e-mail was successfully delivered!")

st.divider()
take_me_home = st.button("Take me home!")
if take_me_home:
    switch_page("RecipeGPT")


