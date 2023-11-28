# Streamlit Movie Finder App

## Description

This project was created for MLH's Month Long Hackathon 2023. This app finds movies using Streamlit and OMDb API. The features of this app are:

1. Search for movies by entering the movie title
2. Filter the results by type: movie or series
3. Filter the results by year
4. Filter the results by rating
5. The results contain the poster, IMDb rating, rated, runtime, released date, genre, director, writer, actors, plot, language, country and awards.
6. Plot IMDB Ratings and IMDB Votes

For information, see this [blog](https://dev.to/david001/creating-a-movie-finder-app-with-streamlit-and-omdb-api-2fak)

## Prerequisites

1. Install [Python](https://www.python.org/downloads/) (at least version 3.8)
2. Sign up for [Streamlit account](https://share.streamlit.io/signup)
3. Sign up for [OMDb API Key](https://www.omdbapi.com/apikey.aspx?__EVENTTARGET=freeAcct&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUKLTIwNDY4MTIzNQ9kFgYCAQ9kFgICBw8WAh4HVmlzaWJsZWhkAgIPFgIfAGhkAgMPFgIfAGhkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBQtwYXRyZW9uQWNjdAUIZnJlZUFjY3QFCGZyZWVBY2N0oCxKYG7xaZwy2ktIrVmWGdWzxj%2FDhHQaAqqFYTiRTDE%3D&__VIEWSTATEGENERATOR=5E550F58&__EVENTVALIDATION=%2FwEdAAU%2BO86JjTqdg0yhuGR2tBukmSzhXfnlWWVdWIamVouVTzfZJuQDpLVS6HZFWq5fYpioiDjxFjSdCQfbG0SWduXFd8BcWGH1ot0k0SO7CfuulHLL4j%2B3qCcW3ReXhfb4KKsSs3zlQ%2B48KY6Qzm7wzZbR&at=freeAcct&Email=)

## How to run this app locally

Open the command terminal and navigate to this directory, then perform the following actions.

1. Create a virtual environment
   ```
   virtualenv venv
   ```
2. Activate virtual environment
   ```
   venv\Scripts\activate
   ```
3. Install streamlit

   ```
   pip install streamlit
   ```

4. Install plotly-express

   ```
   pip install plotly-express
   ```

5. Run the app

   ```
   streamlit run streamlit_app.py
   ```
