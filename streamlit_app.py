import streamlit as st
import requests
import pandas as pd
# import altair as alt
import plotly.express as px 


# Streamlit app title
st.title("Streamlit Movie Rating")

# User input for movie search
movie_search = st.text_input("Search Movie","facebook")

# OMDb API key (you need to sign up for a free API key)
api_key = st.secrets["omdb_api"]

if movie_search:
  url = f"http://www.omdbapi.com/?s={movie_search}&apikey={api_key}"
  movie_search_resp = requests.get(url)
  movie_search_data = movie_search_resp.json()
  df = pd.DataFrame(movie_search_data["Search"])

  movie_titles = []
  movie_ratings = []

  for i in range(len(df)):
    movie_id=df["imdbID"][i]
    
    if movie_id:
      # Perform a search on the OMDb API
      url = f"http://www.omdbapi.com/?i={movie_id}&apikey={api_key}&plot=full"
      movie_id_resp = requests.get(url)


      # Check if the request was successful (status code 200)
      if movie_id_resp.status_code == 200:
          movie_id_data = movie_id_resp.json()

          movie_titles.append(f"{movie_id_data['Title']} {movie_id_data['Year']}")
          movie_ratings.append(float(movie_id_data['imdbRating']))

          if movie_id_data["Response"] == "True":
            
            col1, col2 = st.columns([1,2])

            with col1:              
              if(movie_id_data['Poster']!="N/A"):
                st.image(movie_id_data['Poster'], caption=movie_id_data['Title'], use_column_width=True)              

            with col2:  
              # Display movie details
              st.subheader(f"{movie_id_data['Title']}")              

              col1, col2, col3, col4 = st.columns(4)
              col1.write(f"Year: {movie_id_data['Year']}")
              col2.write(f"Rated: {movie_id_data['Rated']}")
              col3.write(f"Released: {movie_id_data['Released']}")
              col4.write(f"Runtime: {movie_id_data['Runtime']}")

              st.write(f"IMDb Rating: {movie_id_data['imdbRating']}")              
              st.write(f"Genre: {movie_id_data['Genre']}")
              st.write(f"Director: {movie_id_data['Director']}")
              st.write(f"Writer: {movie_id_data['Writer']}")
              st.write(f"Actors: {movie_id_data['Actors']}")
              st.write(f"Plot: {movie_id_data['Plot']}")
              st.write(f"Language: {movie_id_data['Language']}")
              st.write(f"Country: {movie_id_data['Country']}")
              st.write(f"Awards: {movie_id_data['Awards']}")
              
              
              
              
             

              # Visualize the IMDb rating using a bar chart
              # st.subheader("IMDb Rating Visualization:")
              # df = pd.DataFrame({'Reviewer': ["IMDb"], 'Rating': [float(movie_data['imdbRating'])]})
              # df=px.data.tips()
              # fig=px.bar(df,x='Movie',y='IMDb Rating', orientation='h')
              # st.write(fig)
              
              # chart = alt.Chart(df).mark_bar().encode(
              #   x='Movie',
              #   y='IMDb Rating',
              #   color='Movie'
              # ).properties(width=300, height=500)
              # st.altair_chart(chart, use_container_width=True)

              # fig = px.bar(df, x='Rating', y='Reviewer', orientation='h')
              # st.plotly_chart(fig, theme="streamlit", use_container_width=True)
          
          else:
            st.write("No Data")      
      else:
          st.write(f"Error: {movie_id_resp.status_code}. Movie not found or there was an issue fetching data.")

  plot_df = pd.DataFrame({"Titles":movie_titles,"Ratings":movie_ratings})
  fig = px.bar(plot_df, x='Titles', y='Ratings')
  st.plotly_chart(fig, theme="streamlit", use_container_width=True)
     

  # Hide a specific column
  # columns_to_display = ['Title','Year','Type','Poster']
  # st.table(df[columns_to_display])
  # st.dataframe(
  #   df,
  #   column_config={
  #       "Title": "Title",
  #       "Year": "Year",
  #       "Type": "Type",
  #       "Poster": st.column_config.ImageColumn(
  #           "Poster", help="Streamlit app preview screenshots"
  #       )       
  #   },
  #   hide_index=True,
  #   use_container_width=True
  # )
  # fig=px.bar(df,x='Title',y='Year', orientation='h')
  # st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    
   


  