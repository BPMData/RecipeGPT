import streamlit as st
st.set_page_config(page_title="📊👀 Other Things I've Made", page_icon='🆒️', layout='wide')
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.colored_header import colored_header

st.title("Other Things I've Made:")

colored_header(label='About Me', description="", color_name="orange-70")
st.write("My name is Bryan, a data analyst and AI enthusiast based out of the Tri-State Area. Here are some of the other projects I've worked on for fun and to enhance my skills!")
st.divider()

colored_header(label='🤖⇢📚Ψ⇢💬: [Chat "with" The Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition](https://chatwithdsm5.streamlit.app)', description="", color_name="orange-70")
dsmv1, dsmv2 = st.columns([1,2])
with dsmv1:
    st.markdown("""
        <a href="https://chatwithdsm5.streamlit.app" target="_blank">
            <img src="https://drive.google.com/uc?export=download&id=1enrIZpZjbefdPpHbVcjaptyWP31i6QVV" 
                 style="width:100%; height:auto;">
        </a>
        """, unsafe_allow_html=True)


with dsmv2:
    st.write("Noticing that one thing people like to do with ChatGPT is to get it to provide medical or mental health advice, "
         "I thought to [try making a chatbot that would be able to answer questions about psychology with greater technical fidelity "
         "by making use of the DSM-5 (Fifth edition)](https://chatwithdsm5.streamlit.app). "
         "\n"
         "This was my first experiement with using Retrieval-Augmented Generation (RAG) in developing an AI chatbot. "
         "This was actually (briefly) demoed at the 2023 American Psychological Association convention in Washington, D.C. "
         "in a presentation on AI's use in the mental health field!")
st.divider()

colored_header(label='[Bible Searcher - Search the New Testament Bible and see your results!](https://biblesearcher.streamlit.app/)', description="", color_name="orange-70")
bible1, bible2 = st.columns([1,2])
with bible1:
    st.markdown("""
        <a href="https://biblesearcher.streamlit.app/" target="_blank">
            <img src="https://drive.google.com/uc?export=download&id=1GecCdjPsGEWAr8M74SzrKHnvR5fWUIPL" 
                 style="width:100%; height:auto;">
        </a>
        """, unsafe_allow_html=True)

with bible2:
    st.write("An experiment in interactive data visualization using large amounts of text data, as well as a little bit of NLP (Natural Language Processing) "
             "and RegEx (Regular Expressions), this streamlit app allows you to enter one or more names, words or phrases "
             "you'd like to search for in the King James New Testament Bible, and see them all displayed on an interactive "
             "timeline with a point for each apperance of the entered term. I attempted to try and compensate for the fact "
             "that some people in Bible go by more than one name (like Simon becoming Peter), or that, for example, "
             "there's both THE Judas as well as another, totally normal apostle also named Judas. Hovering over an "
             "individual data point will display the entire paragraph containing the mention associated with that point. "
             "Works MUCH better on a desktop or tablet than on a phone. "
             "\n \n"
             "To-Do Item: Leverage my experience creating this into making an interactive Kaggle notebook to allow people"
             "to create an interactive timeline of this nature for any book they have in .txt or DRM-free .pdf or .epub format.")
st.divider()

colored_header(label='[Rudimentary Custom Weather Forestcaster Using Basic Weather API](https://weatherforecaster.streamlit.app/)', description="", color_name="orange-70")
weather1, weather2 = st.columns([1,2])
with weather1:
    st.markdown("""
        <a href="https://weatherforecaster.streamlit.app/" target="_blank">
            <img src="https://drive.google.com/uc?export=download&id=1hlIvPLoeFAOVwMKf183_T7qsHbxCGLxx" 
                 style="width:100%; height:auto;">
        </a>
        """, unsafe_allow_html=True)

with weather2:
    st.write("An honestly not especially good weather forecasting app. However, "
             "the experience with error handling, API calls and UI design gained creating this app proved invaluable in making RecipeGPT!")
st.divider()

colored_header(label='[Analysis of Which American Weather Events Cause the Most Damages to Human Life and Private Property, 1950 - 2011](https://rpubs.com/BPMData/Project2_WeatherAnalysis)', description="", color_name="orange-70")
rpub1, rpub2 = st.columns([1,2])
with rpub1:
    st.markdown("""
        <a href="https://rpubs.com/BPMData/Project2_WeatherAnalysis" target="_blank">
            <img src="https://drive.google.com/uc?export=download&id=1OktEdwJt-Px6UTtk_oH7UPYZRuUpfJeL" 
                 style="width:100%; height:auto;">
        </a>
        """, unsafe_allow_html=True)
    st.markdown("""
        <a href="https://rpubs.com/BPMData/Project2_WeatherAnalysis" target="_blank">
            <img src="https://drive.google.com/uc?export=download&id=1PD3aiww3-VbzzWQDX0VDW_EHSd8W3Xby" 
                 style="width:100%; height:auto;">
        </a>
        """, unsafe_allow_html=True)

with rpub2:
    st.write("An interesting experiment in cleaning and presenting the suprisingly noisy NOAA historical weather damage data, as well as using NLP to "
             "accomodate both the fact that the NOAA has changed the terminology by which it categorizes weather events over time, as well as the fact that their historical"
             " data was entered by hand (with all the typos, random abbreviations and other inconsistencies that entails).")
    st.markdown('Also a good demonstration that, :green[**Hey, I also know R** *(and Markdown)*!]')
st.divider()

colored_header(label="[A business case study and statistical quasi-experimental analysis of the effect of K-pop on interest in Korean cuisine in the United States](https://koreanfood.shorthandstories.com/casestudy/)", description="", color_name="red-70")
kfood1, kfood2 = st.columns([1,2])
with kfood1:
    st.markdown("""
        <a href="https://koreanfood.shorthandstories.com/casestudy/" target="_blank">
            <img src="https://drive.google.com/uc?export=download&id=1DtbWsg3Lkhegz1vXXInnOAvMEuZWiks-" 
                 style="width:100%; height:auto;">
        </a>
        """, unsafe_allow_html=True)
    st.markdown("""
        <a href="https://koreanfood.shorthandstories.com/casestudy/" target="_blank">
            <img src="https://drive.google.com/uc?export=download&id=1oROWz2I6PgzVIS0hd5PnwsQqhglgh78q" 
                 style="width:100%; height:auto;">
        </a>
        """, unsafe_allow_html=True)

with kfood2:
    st.markdown(":orange[Easily my favorite thing I've made other than RecipeGPT itself], this was the [summative final project for my Google Data Analytics Certificate](https://koreanfood.shorthandstories.com/casestudy/). "
             "This was my first experience makign a 'scrollytelling' digital article, performing a more in-depth time series analysis, and optimizing a web page for both desktop and mobile.")
    st.write("When told I could do a case study on ANYTHING I wanted, I decided to invest in learning how to make a "
             "'scrollytelling' interactive web article, discovering [the excellent web service Shorthand](https://shorthand.com/) that makes doing just relatively simple (albeit with a heavy emphasis on the 'relatively').")

    st.write("I then decided combining my passion for statistical experiments and food by analyzing whether the explosive growth in the popularity of K-Pop in the US had a statistically significant effect"
             " on promoting interest in Korean food among American consumers, and what, if any takeaways could be learned from this analysis for the sake of "
             "those interested in promoting the consumption of Korean food, particularly the South Korean government itself, which I learned had started an ongoing official campaign in 2009 to bring 'Korean Food to the World'.")
    st.write("I highly encourage you to [check it out](https://koreanfood.shorthandstories.com/casestudy/) if you're a fan of Korean food, or K-pop, or unnecessarily complicated statistics, or simply bored!")

st.divider()
take_me_home = st.button("Take me home!")
if take_me_home:
    switch_page("RecipeGPT")