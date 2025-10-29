"""
Name: Jose Juan Gonzalez
Library: Altair
URL: https://altair-viz.github.io/
Description:
This app demonstrates the use of the Altair library to visualize air quality data
(AQI) in the United States. We use data from the EPA's Daily AQI by County dataset
to explore pollution levels across states and counties.
"""
#importing what's needed

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import altair as alt
import streamlit as st


# Page setup

st.set_page_config(page_title="U.S. Air Quality Explorer", layout="wide")
st.title("🧭 U.S. Air Quality Explorer – Altair Demo")
st.write(
    "This Streamlit dashboard uses **Altair** to visualize the EPA’s Daily AQI "
    "by County dataset for 2025."
)

# Load data

@st.cache_data
def load_data(path):
    df = pd.read_csv("C:\Users\jjgzz\Desktop\Documents\Babson\Semester 3\Programming\Midterm\Project_Final\daily_aqi_by_county_2025.csv")
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('.', '', regex=False)
    )
    df['date'] = pd.to_datetime(df['date'])
    return df

file_path = "daily_aqi_by_county_2025.csv"
df = load_data(file_path)

# Sidebar filters

st.sidebar.header("Filters")
state_list = sorted(df['state_name'].unique())
selected_state = st.sidebar.selectbox("Select a State", ["All"] + state_list)

if selected_state != "All":
    df = df[df['state_name'] == selected_state]

# Summary metrics

st.subheader("Overview Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(df))
col2.metric("Average AQI", round(df['aqi'].mean(), 2))
col3.metric("Median AQI", round(df['aqi'].median(), 2))

# 1. Average AQI by State

st.subheader("Average AQI by State")
state_aqi = df.groupby('state_name', as_index=False)['aqi'].mean()

bar_chart = (
    alt.Chart(state_aqi)
    .mark_bar()
    .encode(
        x=alt.X('aqi:Q', title='Average AQI'),
        y=alt.Y('state_name:N', sort='-x', title='State'),
        tooltip=['state_name', 'aqi']
    )
    .properties(height=500)
)
st.altair_chart(bar_chart, use_container_width=True)

# 2. Top 15 Most Polluted Counties

st.subheader("Top 15 Most Polluted Counties")
county_aqi = df.groupby(['state_name', 'county_name'], as_index=False)['aqi'].mean()
top15 = county_aqi.nlargest(15, 'aqi')

top_chart = (
    alt.Chart(top15)
    .mark_bar(color='orange')
    .encode(
        x=alt.X('aqi:Q', title='Average AQI'),
        y=alt.Y('county_name:N', sort='-x', title='County'),
        tooltip=['state_name', 'county_name', 'aqi']
    )
    .properties(height=400)
)
st.altair_chart(top_chart, use_container_width=True)

# 3. AQI Distribution

st.subheader("AQI Distribution Histogram")
hist = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X('aqi:Q', bin=alt.Bin(maxbins=30), title='AQI'),
        y='count()',
        tooltip=['count()']
    )
)
st.altair_chart(hist, use_container_width=True)

# 4. Boxplot by Category

st.subheader("AQI by Category")
box = (
    alt.Chart(df)
    .mark_boxplot()
    .encode(
        x=alt.X('category:N', title='AQI Category'),
        y=alt.Y('aqi:Q', title='AQI'),
        color='category:N'
    )
)
st.altair_chart(box, use_container_width=True)

# Footer

st.markdown("---")
st.write(
    "Built with ❤️ using Streamlit and Altair. "
    "Data Source: [EPA Air Quality Data](https://www.epa.gov/outdoor-air-quality-data)."
)
