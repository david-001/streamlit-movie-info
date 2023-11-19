import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime 


# Streamlit app title
st.title("OMDB Movie Search and Filter App")

# User input for movie title
movie_title = st.text_input("Enter Movie Title", "")

# Filter options
type_filter = st.selectbox("Filter by Type", ["movie", "series", "episode"])
year_filter = st.slider("Filter by Release Year", min_value=1900, max_value=datetime.now().year, step=1, value=(1900, datetime.now().year))
rating_filter = st.slider("Filter by IMDb Rating", min_value=0.0, max_value=10.0, step=0.1, value=(0.0, 10.0))

# Search for the movie using the OMDB API
if movie_title:
  omdb_api_url = "http://www.omdbapi.com/"    
  api_key = st.secrets["omdb_api"] # OMDb API key (you need to sign up for a free API key)

  params = {
    "apikey": api_key,
    "s": movie_title,
    "type": type_filter,
    "y": f"{year_filter[0]}-{year_filter[1]}",
    "r": "json"
  }

  response = requests.get(omdb_api_url, params=params)
  data = response.json()

  # Filter and display movie details
  if "Search" in data:
    st.subheader("Filtered Movie Details:")
    for movie in data["Search"]:
      # Additional request to get detailed information for each movie
      detailed_params = {"apikey": api_key, "i": movie["imdbID"], "plot":"full", "r": "json"}
      detailed_response = requests.get(omdb_api_url, params=detailed_params)
      detailed_data = detailed_response.json()


      detailed_data["Year"] = detailed_data["Year"].rstrip("–")  
      # Apply additional filters
      if (
          year_filter[0] <= int(detailed_data["Year"]) <= year_filter[1]     
          and detailed_data["imdbRating"] != "N/A"
          and rating_filter[0] <= float(detailed_data["imdbRating"]) <= rating_filter[1]     
      ):        
        
        col1, col2 = st.columns([1,2])

        with col1:
          # Display movie poster              
          if(detailed_data['Poster']!="N/A"):
            st.image(detailed_data['Poster'], caption=detailed_data['Title'], use_column_width=True)
          else:
            st.image("film-solid.png")               

        with col2:  
          # Display movie details
          st.subheader(f"{detailed_data['Title']}")              

          col1, col2, col3 = st.columns(3)          
          col1.write(f"Year: {detailed_data['Year']}")
          col2.write(f"Rated: {detailed_data['Rated']}")          
          col3.write(f"Runtime: {detailed_data['Runtime']}")
          
          col1, col2 = st.columns(2)
          col1.write(f"Released: {detailed_data['Released']}")
          col2.write(f"IMDb Rating: {detailed_data['imdbRating']}")    

          st.write(f"Genre: {detailed_data['Genre']}")
          st.write(f"Director: {detailed_data['Director']}")
          st.write(f"Writer: {detailed_data['Writer']}")
          st.write(f"Actors: {detailed_data['Actors']}")
          st.write(f"Plot: {detailed_data['Plot']}")
          st.write(f"Language: {detailed_data['Language']}")
          st.write(f"Country: {detailed_data['Country']}")
          st.write(f"Awards: {detailed_data['Awards']}")
        
        st.divider()
  else:
    st.warning("No movies found for the specified criteria.")

else:
  st.warning("Please enter a movie title.")

  