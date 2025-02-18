import pandas as pd
import streamlit as st
from collections import Counter


@st.cache_data()
def load_data(file:str):
    data = pd.read_csv(file)
    return data

def clean_country(df:pd.DataFrame):
    df = df[df["Country"] != "uninformed country"]
    return df

def clean_cast(df:pd.DataFrame):
    df = df[df["cast"] != "uninformed cast"]
    return df

def count_actors(df:pd.DataFrame):
    all_actors = [actor.strip() for sublist in df["cast"].apply(lambda x: x.split(", ")) for actor in sublist]
    actor_counts = Counter(all_actors).most_common(5)
    actors, counts = zip(*actor_counts)
    return actors, counts

def count_countries(df:pd.DataFrame):
    country_counts = Counter(df["Country"]).most_common(5)
    country, country_cnt = zip(*country_counts)
    return country, country_cnt

def add_year(df:pd.DataFrame):
    df["Platform Add Year"] = df["date_added_platform"].str.split(", ").str[-1]
    return df

def convert_channels(df:pd.DataFrame):
    mapping = {"disney-movies-and-tv-shows": "Disney", 
               "hulu-movies-and-tv-shows": "Hulu", "netflix-shows": "Netflix", 
               "amazon-prime-movies-and-tv-shows": "Amazon"}
    df["channel_streaming"] = df["channel_streaming"].apply(lambda x: mapping.get(x, x))
    return df


def filter_dataset(df, selected_page):
    if selected_page != "🏠 Home":
        platform_name = selected_page.split(" ")[1]  # Estrae il nome della piattaforma
        df = df[df['channel_streaming'].str.capitalize() == platform_name]
    return df

def create_table(df):
    st.write(df[['Movie or Serie', 'channel_streaming', 'title', 'cast', 'Country', 'Director', 'Release Year', 'Platform Add Year']])