import streamlit as st
import requests

api_key = "vGs5oLpS6lnzL3ehHyB7Y9xr0wdz7ABx4vJaBsUa"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

request = requests.get(url)
content = request.json()

st.set_page_config(layout="wide")
st.title(content["title"])
st.image(content["hdurl"])
st.write(content["explanation"])