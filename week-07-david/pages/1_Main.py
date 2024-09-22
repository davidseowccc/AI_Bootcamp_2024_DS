# run in windows command prompt: python -m streamlit run main.py

# Set up and run this Streamlit App
import streamlit as st
import pandas as pd

#####
# Check if the password is correct.  
from helper_functions.utility import check_password  

if check_password() == False:  
    st.stop()
#####

# from helper_functions import llm  # Not needed anymore. 
# The helper function is now directly called by 'customer_query_handler'
from logics.customer_query_handler import process_user_message

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Course Query Demo - DS20240915"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Course Query Chatbot")
st.text("David Seow, 15 Sep 2024")

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt/query here", height=200)

if form.form_submit_button("Submit"):
    
    st.toast(f"User Input Submitted - {user_prompt}")

    st.divider()

    response, course_details = process_user_message(user_prompt)
    st.write(response)

    st.divider()

    print(course_details)
    df = pd.DataFrame(course_details)
    df 
