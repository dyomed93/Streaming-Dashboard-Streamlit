import streamlit as st
import plotly.express as px
from utils import load_data, count_actors, count_countries, clean_cast, clean_country



def show():
    st.title("Streaming Data Analysis")


def metrics(global_df):
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.metric(label="Total Movies", value=len(global_df[global_df["Movie or Serie"] == "Movie"]))
    with col2:
        st.metric(label="Total Series", value=len(global_df[global_df["Movie or Serie"] != "Movie"]))
    with col3:
        st.metric(label="Total Actors", value=global_df["cast"].apply(lambda x: len(x.split(", "))).count())

def graphs_hp(global_df):
    col1, col2 = st.columns([1, 1])
    with col1:
        fig = px.pie(global_df, names="Movie or Serie", title="% Movies & Series", template="seaborn")
        st.plotly_chart(fig, use_container_width=True)
        fig2 = px.pie(global_df, names="channel_streaming", title="% Streaming Channels", template="seaborn")
        st.plotly_chart(fig2, use_container_width=True)
    with col2:
        global_df = clean_cast(global_df)
        global_df = clean_country(global_df)
        actors, counts = count_actors(global_df)
        fig = px.bar(x=actors, y=counts, title="Top 5 Actors by Appearances", labels={'x': 'Actors', 'y': 'Appearances'}, template="seaborn",
              color=counts, color_continuous_scale='Blues')
        st.plotly_chart(fig, use_container_width=True)
        country, country_cnt = count_countries(global_df)
        fig2 = px.bar(x=country, y=country_cnt, title="Top 5 Movies & Series by Country", labels={'x': 'Country', 'y': 'N. Productions'},
                    template="seaborn", color=country_cnt, color_continuous_scale='Blues')
        st.plotly_chart(fig2, use_container_width=True)

def create_table(global_df):
    st.write("**All Channels Data**")
    st.write(global_df[['Movie or Serie', 'channel_streaming', 'title', 'cast', 'Country', 'Director', 'Release Year', 'Platform Add Year']])