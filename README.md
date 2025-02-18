# Streaming-Dashboard-in-Streamlit

The following project has the purpose to illustrate how to build a simple taylor made dashboard in Streamlit, using Streaming data from:
- Amazon Prime
- Netflix
- Hulu
- Disney +

The dataset was taken from kaggle, at the link https://www.kaggle.com/datasets/sc0v1n0/4-services-streaming-movies-and-tv, and contains
all films and tv-series uploaded on those four streaming services, from 2006 to 2021, with a number of rows of 22671.

The repository structure is the following:

#streamlit_test
    -.streamlit
        -config.yaml
    - my_pages
        - home_page.py
        - amazon.py
        - hulu.py
        - netflix.py
        - disney.py
    all_streaming.csv
    app.py
    utils.py
    LICENSE
    README.md

This app is built with an home-page, where You can find all macro data for the top 4 streaming services in the mentioned period as distribution of products by streaming channel, global distribution of movies and tv series, top 5 actors by appearances and top 5 countries by products made,
and the single pages for each streaming service. 
Inside each of them You can see the number of movies and series added to the platform by date,
distribution of movies and tv-series inside the platform, top 5 actors by appearances, and Top 5 Country by number of movies and series.

