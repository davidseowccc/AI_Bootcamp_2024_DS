import os
import json
import pandas as pd

# # Load the JSON file
# filepath = './data/courses-full.json'
# with open(filepath, 'r') as file:
#     json_string = file.read()
#     dict_of_courses = json.loads(json_string)

import json
import requests

# URL of the raw JSON file on GitHub
# url = 'https://raw.githubusercontent.com/your-username/your-repository/main/data/courses-full.json'
# url = 'https://github.com/davidseowccc/AI_Bootcamp_2024_DS/blob/main/week-07-david/data/courses-full.json'
url = 'https://raw.githubusercontent.com/davidseowccc/AI_Bootcamp_2024_DS/main/week-07-david/data/courses-full.json'

# Fetch the JSON file from GitHub
response = requests.get(url)
json_string = response.text

# Parse the JSON string into a Python dictionary
dict_of_courses = json.loads(json_string)

# Create the DataFrame and Transpose Table
df = pd.DataFrame(dict_of_courses).T

# Reset the index to bring the course name as a column
df.reset_index(drop=True, inplace=True)

# Display the DataFrame
df

# import streamlit as st
# st.table(df)
