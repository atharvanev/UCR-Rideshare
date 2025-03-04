# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import requests
from functions import convert_number

st.set_page_config(layout="wide")

SPREADSHEET_ID = st.secrets["connections"]["gsheets"]["spreadsheet_id"]
API_KEY = st.secrets["connections"]["gsheets"]["api_key"]

url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}?key={API_KEY}"
response = requests.get(url)
sheetdata = response.json()



worksheet_names = [sheet["properties"]["title"] for sheet in sheetdata.get("sheets", [])]

print(worksheet_names)

conn = st.connection("gsheets", type=GSheetsConnection)
#data = conn.read(worksheet="Feb2025",usecols = list(range(15)))
#st.dataframe(data)


st.title("UCR Rideshare 🚕")
col1,col2 = st.columns([2, 4])

with col1:
    option = st.selectbox('Which Month',worksheet_names)
    data = conn.read(worksheet=option,usecols = list(range(15)),ttl=600)
    if "Student's Phone Number" in data.columns:
        data["Student's Phone Number"] = data["Student's Phone Number"].apply(convert_number)
with col2:
    third_column = data.iloc[:, 2]
    third_column= third_column.astype(str)
    st.dataframe(data)