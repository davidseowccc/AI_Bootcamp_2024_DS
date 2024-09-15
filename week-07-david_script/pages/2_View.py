import os
import json
import pandas as pd

# Load the JSON file
filepath = './data/courses-full.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_courses = json.loads(json_string)

# Create the DataFrame and Transpose Table
df = pd.DataFrame(dict_of_courses).T

# Reset the index to bring the course name as a column
df.reset_index(drop=True, inplace=True)

# Display the DataFrame
df

# import streamlit as st
# st.table(df)
