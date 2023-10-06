import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{'
                          '}?api_key=a7d4b94dd7d5d72bf08537786c42ad01&language=en-US'.format(movie_id))
    data = response.json()

    return "https://image.tmdb.org/t/p/w500"+data['poster_path']
def recommend(movie):
    recommend_movie_poster=[]
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)[1:6]
    recommended_movies = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        #fetch poster from API
        recommend_movie_poster.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies , recommend_movie_poster
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movies Recommendation System Developed By Saurabh Sharma')
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',

    movies['title'].values)
if st.button('Recommend'):
    names,posters =recommend(selected_movie_name)
    col1, col2, col3 , col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
# need movies posters