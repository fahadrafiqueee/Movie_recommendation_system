import pickle

import pandas as pd
import streamlit as st

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:21]:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

page_bg_img = '''
<style>
      .stApp {
  background-image: url("https://images.hdqwalls.com/download/pennywise-the-clown-it-2017-movie-4k-hp-1600x900.jpg");
  background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)


st.markdown('# Movie Recommendation System')
movies = pd.read_pickle(open('movie_list.pkl','rb'))
similarity = pd.read_pickle(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


if st.button('Recommend'):
    recommended_movie_names = recommend(selected_movie)
    for i in recommended_movie_names:
        st.subheader(i)