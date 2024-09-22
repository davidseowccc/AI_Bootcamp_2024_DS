# run in windows command prompt: python -m streamlit run Start.py

import streamlit as st
from groq import Groq

####

from helper_functions.utility import check_password  

#####
# Demo password or no password required
# while True:
#     pw = st.text_input('Select "1" to BYPASS password.')
    
#     if (pw == "1"):
#         break

#     else:
#         # Check if the password is correct.  
#         if check_password() == False:  
#             st.stop()

# Set an initial state for bypass if it doesn't exist yet
if 'bypass' not in st.session_state:
    st.session_state.bypass = False

# If the bypass is not activated, show the password input
if not st.session_state.bypass:
    pw = st.text_input('Enter "1" to BYPASS the password.')

    # Check if the user enters "1" to bypass the password check
    if pw == "1":
        st.session_state.bypass = True
        st.success("Password bypassed!")
    
    else:
        # Here you can check the password using your `check_password()` function
        if st.button("Submit Password"):
            if check_password() == False:
                st.error("Incorrect password. Please try again.")
                st.stop()
            else:
                st.success("Correct password!")

# If bypass is activated, proceed without asking for a password
else:
    st.write("Password bypassed! Proceeding without password.")
    # Your application logic goes here

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
