import streamlit as st
import pandas as pd
import numpy as np
from streamlit_gsheets import GSheetsConnection

WORKSHEET_NAME='202408_devrel-data-ytd'

st.title('The DevRel Digest utm metrics')

# Create a connection object.
CONN = st.connection("gsheets", type=GSheetsConnection)

COLUMNS = ['created_at', 'url', 'clicks', 'utm_source', 'utm_campaign']

# Get the data
def sheet_data(): 
    data = CONN.read(
        worksheet=WORKSHEET_NAME,
        header=0,
        ttl="10m",
        usecols=COLUMNS,
        skip_blank_lines=True,
    )
    print(data)
    return data['utm_source']

# st.subheader('Number of clicks to dev.to by source')

# source_click_chart_data = pd.DataFrame(
#    {
#        "Source": source_click_data['utm_source'],
#        "Clicks": source_click_data['clicks'],
#    }
# )

# st.bar_chart(source_click_chart_data , x="Source", y="Clicks")

# st.subheader('Number of clicks to links included in dev.to')

# click_next_data = conn.read(
#     worksheet=WORKSHEET_NAME,
#     header=0,
#     ttl="10m",
#     usecols=[4, 6],
#     skiprows=[1, 2, 3, 4]
# )

# print(click_next_data)

# click_next_chart_data = pd.DataFrame(
#    {
#        "Link": click_next_data['url'],
#        "Clicks": click_next_data['clicks'],
#    }
# )

# st.bar_chart(click_next_chart_data , x="Link", y="Clicks")
