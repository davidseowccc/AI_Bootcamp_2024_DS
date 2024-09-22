# run in windows command prompt: python -m streamlit run Start.py

import streamlit as st
from groq import Groq

####

from helper_functions.utility import check_password  

#####
# Demo password or no password required
pw = st.text_input('Select "1" to BYPASS password.')

while True:
    if (pw == "1"):
        break

    else: 
        # Check if the password is correct.  
        check_password()
            if not check_password():  
                st.stop()

#####

client = Groq(
    api_key=st.secrets["GROQ_KEY"],)

st.set_page_config(
    page_title="Course Query Chatbot",
    page_icon="👋",
)

st.write("# Welcome to Course Query Chatbot! 👋")
st.text("by David Seow 15 Sep 2024")

# st.sidebar.success("Select a demo above.")

st.markdown(
    """
    This chatbot app deploys Streamlit as the web framework deploying Llama3.1 as LLM.
     It details a chatbot for a sample suite of courses that could be found in the 'View all courses' tab.

    **👈 Select a page from the sidebar** for all this app can do!
    
    #### Start  - current page
    #### Main   - chatbot
    #### View   - view all courses
    #### About  - about this App
    """
)
