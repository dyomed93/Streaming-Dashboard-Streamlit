import pandas as pd
import streamlit as st
import numpy as np
import importlib
from streamlit_dynamic_filters import DynamicFilters
from utils import load_data, clean_cast, clean_country, add_year, convert_channels, filter_dataset



st.set_page_config(
    page_title="Streaming Data Analysis",
    page_icon="🎬",
    layout="wide",
    )

global_df = load_data("all_streaming.csv")
global_df = add_year(global_df)
global_df = convert_channels(global_df)
global_df = global_df.rename(columns={"movie_or_serie": "Movie or Serie"
                                      , "country": "Country"
                                      , "director": "Director"
                                      , "release_year": "Release Year"})
global_df["Release Year"] = global_df["Release Year"].astype(str)


pages = {
    "🏠 Home": "my_pages.home_page",
    "🎬 Amazon": "my_pages.amazon",
    "🎬 Netflix": "my_pages.netflix",
    "🎬 Disney": "my_pages.disney",
    "🎬 Hulu": "my_pages.hulu"
}


if __name__ == "__main__":
    # Home Page as default
    if "current_page" not in st.session_state:
        st.session_state.current_page = list(pages.keys())[0]  

    # Radio button to select page
    selection = st.sidebar.radio("Go To:", list(pages.keys()), index=list(pages.keys()).index(st.session_state.current_page))

    
    # Session state update if selection changes
    if selection != st.session_state.current_page:
        st.session_state.current_page = selection
        st.rerun()

    global_df = filter_dataset(global_df, selection)

    # Module selection for the selected page
    page_module = importlib.import_module(pages[selection])

    dynamic_filters = DynamicFilters(global_df, filters=['Movie or Serie', 'Country', 'Director', 'Release Year'])
    with st.sidebar:
        st.button("Reset Filters", on_click=dynamic_filters.reset_filters)
    dynamic_filters.display_filters(location="sidebar")
    global_df = dynamic_filters.filter_df()
    

    # Function show() in the selected page
    if hasattr(page_module, "show"):
        page_module.show()
    else:
        st.error(f"Error: in page {selection} function `show()` not created!")
    
    # Function metrics() in the selected page
    if hasattr(page_module, "metrics"):
        page_module.metrics(global_df)
    else:
        st.error(f"Error: in page {selection} function `metrics()` not created!")
    
    # Function graph_pie() in the selected page
    if hasattr(page_module, "graphs_hp"):
        page_module.graphs_hp(global_df)
    else:
        st.error(f"Error: in page {selection} function `graphs_hp()` not created!")
    
    # Function create_table() in the selected page
    if hasattr(page_module, "create_table"):
        page_module.create_table(global_df)
    else:
        st.error(f"Error: in page {selection} function `create_table()` not created!")
    

