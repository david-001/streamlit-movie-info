import streamlit as st
import requests
import pandas as pd
# import altair as alt
import plotly.express as px 


# Streamlit app title
st.title("Streamlit Movie Rating")

# User input for movie title
movie_title = st.text_input("Enter Movie Title")

movie_search = st.text_input("Search Movie","facebook")

# OMDb API key (you need to sign up for a free API key)
api_key = st.secrets["omdb_api"]

if movie_search:
  url = f"http://www.omdbapi.com/?s={movie_search}&apikey={api_key}"
  response = requests.get(url)
  movie_data = response.json()
  df = pd.DataFrame(movie_data["Search"])

  title=""
  def show_data():    
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}&plot=full"
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        movie_data = response.json()
        if movie_data["Response"] == "True":
          col1, col2 = st.columns([1,2])

          with col1:
            st.image(movie_data['Poster'], caption=movie_data['Title'], use_column_width=True)

          with col2:  

            # Display movie details
            st.subheader("Movie Details:")
            st.write(f"Title: {movie_data['Title']}")    

            col1, col2, col3, col4 = st.columns(4)
            col1.write(f"Year: {movie_data['Year']}")
            col2.write(f"Rated: {movie_data['Rated']}")
            col3.write(f"Released: {movie_data['Released']}")
            col4.write(f"Runtime: {movie_data['Runtime']}")

            st.write(f"Genre: {movie_data['Genre']}")
            st.write(f"Director: {movie_data['Director']}")
            st.write(f"Writer: {movie_data['Writer']}")
            st.write(f"Actors: {movie_data['Actors']}")
            st.write(f"Plot: {movie_data['Plot']}")
            st.write(f"Language: {movie_data['Language']}")
            st.write(f"Country: {movie_data['Country']}")
            st.write(f"Awards: {movie_data['Awards']}")
            st.write(f"IMDb Rating: {movie_data['imdbRating']}")
            st.progress(float(movie_data['imdbRating'])/10)
            
            
            
            # data = {
            #     'Year': [{movie_data['Year']}],
            #     'Rated': [{movie_data['Rated']}],
            #     'Released': [{movie_data['Runtime']}]
            # }

            # # Create a DataFrame
            # df = pd.DataFrame(data)

            # # Display the table
            # st.table(df)

            st.subheader("Movie Poster:")
            

            # Visualize the IMDb rating using a bar chart
            st.subheader("IMDb Rating Visualization:")
            df = pd.DataFrame({'Reviewer': ["IMDb"], 'Rating': [float(movie_data['imdbRating'])]})
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
  

  for i in range(len(df)):
     title=df["Title"][i]
     st.button(title,on_click=show_data)

  # Hide a specific column
  columns_to_display = ['Title','Year','Type','Poster']
  st.table(df[columns_to_display])
  st.dataframe(
    df,
    column_config={
        "Title": "Title",
        "Year": "Year",
        "Type": "Type",
        "Poster": st.column_config.ImageColumn(
            "Poster", help="Streamlit app preview screenshots"
        )
        # "stars": st.column_config.NumberColumn(
        #     "Github Stars",
        #     help="Number of stars on GitHub",
        #     format="%d ⭐",
        # ),
        # "url": st.column_config.LinkColumn("App URL"),
        # "views_history": st.column_config.LineChartColumn(
        #     "Views (past 30 days)", y_min=0, y_max=5000
        # ),
    },
    hide_index=True,
    use_container_width=True
  )
  fig=px.bar(df,x='Title',y='Year', orientation='h')
  st.plotly_chart(fig, theme="streamlit", use_container_width=True)
  # col1, col2, col3, col4 = st.columns(4)
  # with col1:
  #   st.write("Title")
  #   for i in range(len(df)):
  #     st.write(df["Title"][i])

  # with col2:
  #   st.write("Year")
  #   for i in range(len(df)):
  #     st.write(df["Year"][i])


      # st.write(movie_data["Search"][0]["Title"])
  #  df = pd.DataFrame(movie_data["Search"])
   
    
   

# if movie_title:
#     # Perform a search on the OMDb API
#     url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}&plot=full"
#     response = requests.get(url)

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         movie_data = response.json()
#         if movie_data["Response"] == "True":
#           col1, col2 = st.columns([1,2])

#           with col1:
#             st.image(movie_data['Poster'], caption=movie_data['Title'], use_column_width=True)

#           with col2:  

#             # Display movie details
#             st.subheader("Movie Details:")
#             st.write(f"Title: {movie_data['Title']}")    

#             col1, col2, col3, col4 = st.columns(4)
#             col1.write(f"Year: {movie_data['Year']}")
#             col2.write(f"Rated: {movie_data['Rated']}")
#             col3.write(f"Released: {movie_data['Released']}")
#             col4.write(f"Runtime: {movie_data['Runtime']}")

#             st.write(f"Genre: {movie_data['Genre']}")
#             st.write(f"Director: {movie_data['Director']}")
#             st.write(f"Writer: {movie_data['Writer']}")
#             st.write(f"Actors: {movie_data['Actors']}")
#             st.write(f"Plot: {movie_data['Plot']}")
#             st.write(f"Language: {movie_data['Language']}")
#             st.write(f"Country: {movie_data['Country']}")
#             st.write(f"Awards: {movie_data['Awards']}")
#             st.write(f"IMDb Rating: {movie_data['imdbRating']}")
#             st.progress(float(movie_data['imdbRating'])/10)
            
            
            
#             # data = {
#             #     'Year': [{movie_data['Year']}],
#             #     'Rated': [{movie_data['Rated']}],
#             #     'Released': [{movie_data['Runtime']}]
#             # }

#             # # Create a DataFrame
#             # df = pd.DataFrame(data)

#             # # Display the table
#             # st.table(df)

#             st.subheader("Movie Poster:")
            

#             # Visualize the IMDb rating using a bar chart
#             st.subheader("IMDb Rating Visualization:")
#             df = pd.DataFrame({'Reviewer': ["IMDb"], 'Rating': [float(movie_data['imdbRating'])]})
#             # df=px.data.tips()
#             # fig=px.bar(df,x='Movie',y='IMDb Rating', orientation='h')
#             # st.write(fig)
            
#             # chart = alt.Chart(df).mark_bar().encode(
#             #   x='Movie',
#             #   y='IMDb Rating',
#             #   color='Movie'
#             # ).properties(width=300, height=500)
#             # st.altair_chart(chart, use_container_width=True)

#             # fig = px.bar(df, x='Rating', y='Reviewer', orientation='h')
#             # st.plotly_chart(fig, theme="streamlit", use_container_width=True)

#         else:
#           st.write("No Data")      
#     else:
#         st.write(f"Error: {response.status_code}. Movie not found or there was an issue fetching data.")
  