This is for streamlit. 
Operational now!

---

## 🔬 Adjustments Needed

#### 1. Script to parse data from Github JSON file 
```bash
# URL of the raw JSON file on GitHub
url = 'https://raw.githubusercontent.com/davidseowccc/AI_Bootcamp_2024_DS/main/week-07-david/data/courses-full.json'

# Fetch the JSON file from GitHub
response = requests.get(url)
json_string = response.text

# Parse the JSON string into a Python dictionary
dict_of_courses = json.loads(json_string)
```
#### 2. To insert secret API key for Streamlit
```bash
# for streamlit
client = Groq(
    api_key=st.secrets["GROQ_KEY"],)
```

