import streamlit as st
import requests
import pandas as pd
import altair as alt

# Streamlit app title
st.title("Movie Rating Visualization")

# User input for movie title
movie_title = st.text_input("Enter Movie Title", "lion king")

# OMDb API key (you need to sign up for a free API key)
api_key = st.secrets["omdb_api"]

# Perform a search on the OMDb API
url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    movie_data = response.json()

    # Display movie details
    st.subheader("Movie Details:")
    st.write(f"Title: {movie_data['Title']}")
    st.write(f"Year: {movie_data['Year']}")
    st.write(f"Rated: {movie_data['Rated']}")
    st.write(f"Released: {movie_data['Released']}")
    st.write(f"Runtime: {movie_data['Runtime']}")
    st.write(f"Genre: {movie_data['Genre']}")
    st.write(f"Director: {movie_data['Director']}")
    st.write(f"Writer: {movie_data['Writer']}")
    st.write(f"Actors: {movie_data['Actors']}")
    st.write(f"Plot: {movie_data['Plot']}")
    st.write(f"Language: {movie_data['Language']}")
    st.write(f"Country: {movie_data['Country']}")
    st.write(f"Awards: {movie_data['Awards']}")
    st.write(f"IMDb Rating: {movie_data['imdbRating']}")

    data = {
        'Year': {movie_data['Year']},
        'Rated': {movie_data['Rated']},
        'Released': {movie_data['Runtime']}
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Display the table
    st.table(df)

    # Visualize the IMDb rating using a bar chart
    st.subheader("IMDb Rating Visualization:")
    df = pd.DataFrame({'Movie': [movie_data['Title']], 'IMDb Rating': [float(movie_data['imdbRating'])]})
    chart = alt.Chart(df).mark_bar().encode(
        x='Movie',
        y='IMDb Rating',
        color='Movie'
    ).properties(width=300, height=200)

    st.altair_chart(chart, use_container_width=True)

else:
    st.write(f"Error: {response.status_code}. Movie not found or there was an issue fetching data.")