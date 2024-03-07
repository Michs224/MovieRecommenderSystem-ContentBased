import streamlit as st
import joblib
import requests


st.header("Movie Recommender System")

def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data["poster_path"]
    full_path="https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path


def recommend(movie):
    index=movies[movies["title"]==movie].index[0]
    distance=sorted(list(enumerate(similarity_model[index])),reverse=True,key=lambda vector:vector[1])
    recommend_movies=[]
    recommend_poster=[]
    for i in distance[1:11]:
        movies_id=movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]]["title"])
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movies,recommend_poster


with open("movieLists.pkl","rb") as f:
    movies=joblib.load(f)

# URL cosine_similarity
# s3_url = "https://similaritymovierecommendersystem.s3.eu-north-1.amazonaws.com/similarity.pkl"

# Download cosine_similarity
# response = requests.get(s3_url)
# with open("similarity.pkl", "wb") as f:
#     f.write(response.content)

# Load cosine_similarity
with open("similarity.pkl", "rb") as f:
    similarity_model = joblib.load(f)
    
import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="./frontend/public")


imageUrls = [
    fetch_poster(19995),
    fetch_poster(299536),
    fetch_poster(580489),
    fetch_poster(122),
    fetch_poster(429422),
    fetch_poster(2830),
    fetch_poster(9722),
    fetch_poster(363088),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
    ]


imageCarouselComponent(imageUrls=imageUrls, height=200)    
    
listMovies=movies["title"].values
selectvalue=st.selectbox("Select Movie from Dropdown",listMovies)

if st.button("Show Recommend"):
    movie_names,movie_posters=recommend(selectvalue)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_names[0])
        st.image(movie_posters[0])
    with col2:
        st.text(movie_names[1])
        st.image(movie_posters[1])
    with col3:
        st.text(movie_names[2])
        st.image(movie_posters[2])
    with col4:
        st.text(movie_names[3])
        st.image(movie_posters[3])
    with col5:
        st.text(movie_names[4])
        st.image(movie_posters[4])
    with col1:
        st.text(movie_names[5])
        st.image(movie_posters[5])
    with col2:
        st.text(movie_names[6])
        st.image(movie_posters[6])
    with col3:
        st.text(movie_names[7])
        st.image(movie_posters[7])
    with col4:
        st.text(movie_names[8])
        st.image(movie_posters[8])
    with col5:
        st.text(movie_names[9])
        st.image(movie_posters[9])
