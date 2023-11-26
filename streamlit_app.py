import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime 

# Streamlit app title
st.title("OMDB Movie Search App")

# User input for movie title
movie_title = st.text_input("Enter Movie Title", "")

# Current Year
current_year = datetime.now().year

movies_df = pd.DataFrame()

# Filter options
type_filter = st.selectbox("Filter by Type", ["movie", "series"])
year_filter = st.slider("Filter by Release Year", min_value=1900, max_value=current_year, step=1, value=(1900, current_year))
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

  with st.spinner('Processing...'):    

    response = requests.get(omdb_api_url, params=params)
    data = response.json()

    # Filter and display movie details
    if "Search" in data:      
      for movie in data["Search"]:
        # Additional request to get detailed information for each movie
        detailed_params = {"apikey": api_key, "i": movie["imdbID"], "plot":"full", "r": "json"}
        detailed_response = requests.get(omdb_api_url, params=detailed_params)
        detailed_data = detailed_response.json()

        
        detailed_data["Year"] = detailed_data["Year"].rstrip("–")  
        # Apply additional filters
        if (
            (
              type_filter == 'movie' and            
              year_filter[0] <= int(detailed_data["Year"]) <= year_filter[1] and    
              detailed_data["imdbRating"] != "N/A" and
              rating_filter[0] <= float(detailed_data["imdbRating"]) <= rating_filter[1]
            ) or  
            (
              type_filter == 'series' and                        
              detailed_data["imdbRating"] != "N/A" and
              rating_filter[0] <= float(detailed_data["imdbRating"]) <= rating_filter[1]
            )    
        ):     
                                                    
          new_row_df = pd.DataFrame({'Poster':[detailed_data['Poster']],
                                    'Title':[f"{detailed_data['Title']} ({detailed_data['Year']})"],
                                    'Year':[detailed_data['Year']],
                                    'Rated':[detailed_data['Rated']],
                                    'Runtime':[detailed_data['Runtime']],
                                    'Released':[detailed_data['Released']],
                                    'Genre':[detailed_data['Genre']],
                                    'Director':[detailed_data['Director']],
                                    'Writer':[detailed_data['Writer']],
                                    'Actors':[detailed_data['Actors']],
                                    'Language':[detailed_data['Language']],
                                    'Country':[detailed_data['Country']],
                                    'Awards':[detailed_data['Awards']],
                                    'Plot': [detailed_data['Plot']],
                                    'IMDB Rating': [detailed_data['imdbRating']],
                                    'IMDB Votes': [detailed_data['imdbVotes']],
                                    # 'Emotional tone':[analyze_emotion(f"{detailed_data['Plot']} {detailed_data['Genre']}")]
                                    })
          movies_df = pd.concat([movies_df, new_row_df], ignore_index=True)                                             
    else:
      st.warning("No movies found for the specified criteria.")
else:
  st.warning("Please enter a movie title.")


# Setup tabs
tab1, tab2 = st.tabs(["Search Results", "Ratings and Votes"])

with tab1:
  if(len(movies_df)>0):
    st.header("Search Results")          
    for i in range(len(movies_df)):
      col1, col2 = st.columns([1,2])
      with col1:
        # Display movie poster              
        if(movies_df['Poster'][i]!="N/A"):
          st.image(movies_df['Poster'][i], caption=movies_df['Title'][i], use_column_width=True)
        else:
          st.image("film-solid.png")               

      with col2:  
        # Display movie details
        st.subheader(movies_df['Title'][i])              

        col1, col2, col3 = st.columns(3)          
        col1.write(f"IMDb Rating: {movies_df['IMDB Rating'][i]}")    
        col2.write(f"Rated: {movies_df['Rated'][i]}")          
        col3.write(f"Runtime: {movies_df['Runtime'][i]}")
                  
        # st.write(f"Emotional Tone: {movies_df['Emotional tone'][i][0]['label']}")          
        st.write(f"Released: {movies_df['Released'][i]}")          
        st.write(f"Genre: {movies_df['Genre'][i]}")
        st.write(f"Director: {movies_df['Director'][i]}")
        st.write(f"Writer: {movies_df['Writer'][i]}")
        st.write(f"Actors: {movies_df['Actors'][i]}")
        st.write(f"Plot: {movies_df['Plot'][i]}")        
        st.write(f"Language: {movies_df['Language'][i]}")
        st.write(f"Country: {movies_df['Country'][i]}")
        st.write(f"Awards: {movies_df['Awards'][i]}")
      
      st.divider()     

with tab2:
  if(len(movies_df)>0):
    fig = px.bar(movies_df, x='Title', y='IMDB Rating')  
    st.header("IMDB Ratings")
    st.plotly_chart(fig, theme="streamlit", use_container_width=True) 

    fig = px.bar(movies_df, x='Title', y='IMDB Votes')  
    st.header("IMDB Votes")
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)  
