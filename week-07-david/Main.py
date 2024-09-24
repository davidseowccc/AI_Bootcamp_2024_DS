# run in windows command prompt: python -m streamlit run Start.py

import streamlit as st

####

# from helper_functions.utility import check_password  
# if not check_password():  
#     st.stop()
    
#####

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
    
    #### Main   - chatbot
    #### Intro  - current page
    #### View   - view all courses
    #### About  - about this App
    """
)
