import streamlit as st
import pandas as pd
import numpy as np
from streamlit_gsheets import GSheetsConnection

WORKSHEET_NAME="20240203_utm-io_links_202402031724020"

st.title('The DevRel Digest January 2024 performance')

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

source_click_data = conn.read(
    worksheet=WORKSHEET_NAME,
    header=0,
    ttl="10m",
    usecols=[6, 9],
    nrows=4,
)

st.subheader('Number of clicks to dev.to by source')

source_click_chart_data = pd.DataFrame(
   {
       "Source": source_click_data['utm_source'],
       "Clicks": source_click_data['clicks'],
   }
)

st.bar_chart(source_click_chart_data , x="Source", y="Clicks")

st.subheader('Number of clicks to links included in dev.to')

click_next_data = conn.read(
    worksheet=WORKSHEET_NAME,
    header=0,
    ttl="10m",
    usecols=[4, 6],
    skiprows=[1, 2, 3, 4]
)

print(click_next_data)

click_next_chart_data = pd.DataFrame(
   {
       "Link": click_next_data['url'],
       "Clicks": click_next_data['clicks'],
   }
)

st.bar_chart(click_next_chart_data , x="Link", y="Clicks")
