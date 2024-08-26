import streamlit as st
import pandas as pd
import altair as alt
from streamlit_gsheets import GSheetsConnection

WORKSHEET_NAME='202408_devrel-data-ytd'

st.title('The DevRel Digest utm insights')

# Create a connection object.
CONN = st.connection("gsheets", type=GSheetsConnection)

COLUMNS = ['created_at', 'url', 'clicks', 'utm_source', 'utm_campaign']

UTM_SOURCE = 'dev-to'

# Get the data and use caching
@st.cache_data
def sheet_data(): 
    
    data = CONN.read(
        worksheet=WORKSHEET_NAME,
        header=0,
        ttl="10m",
        usecols=COLUMNS,
        skip_blank_lines=True,
    )

    # Convert the `created_at` column to a datetime dtype
    # Then convert that to just a month (1-12)
    data['created_at'] = pd.to_datetime(data['created_at']).dt.month_name()
    
    # Drop any rows where the `utm_source` is not `dev-to`
    index_utm_source = data[(data['utm_source'] != UTM_SOURCE)].index
    data.drop(index_utm_source, inplace=True)
    
    return data

def selection_list():
    selection_list = list(app_data.created_at.unique())[::-1]
    selection_list.append("All time")
    return selection_list

def display_chart(app_data, selected_month):
    
    if selected_month and selected_month != "All time":
        display_data = app_data[app_data.created_at == selected_month]
    elif selected_month == "All time":
        display_data = app_data
    else:
       display_data = app_data 

    bar_chart = (
        alt.Chart(display_data)
        .mark_bar()
        .encode(y='clicks:Q',
                x=alt.X('url:N', axis=alt.Axis(labelAngle=-45)).sort('-y'),
                href='url:N'))

    st.altair_chart(bar_chart, use_container_width=True)

with st.sidebar:
    st.page_link("https://dev.to/lizzzzz/series/25904", label="The DevRel Digest")

app_data = sheet_data()

selected_month = st.selectbox("Select a month",
                             selection_list(),
                             index=None,
                             placeholder="Select a month")

display_chart(app_data, selected_month)




