import streamlit as st
import pickle
import pandas as pd
import requests



def fetch_song(track_id):
    # url = f"https://v1.nocodeapi.com/ayushi456/spotify/TgPFGQbAAipQRkqd/tracks?ids={track_id}"
    # response = requests.get(url)
    # data = response.json()
    # return data["tracks"][0]["album"]["images"][0]["url"]
    response=requests.get(f"https://v1.nocodeapi.com/ayushi456/spotify/TgPFGQbAAipQRkqd/tracks?ids={track_id}")
    data=response.json()
    return data['tracks'][0]['album']['images'][0]['url']

# def fetch_song(track_id):
#     url = f"https://v1.nocodeapi.com/ayushi456/spotify/TgPFGQbAAipQRkqd/tracks?ids={track_id}"
#     response = requests.get(url)
#     data = response.json()

#     if "tracks" in data and len(data["tracks"]) > 0:
#         return data["tracks"][0]["album"]["images"][0]["url"]
#     else:
#         st.write("⚠️ Could not fetch poster for track:", track_id)
#         return "https://via.placeholder.com/150" 



def recommend(my_song):
    song_index=songs[songs["track_name"]==my_song].index[0]
    distance=similarity[song_index]
    movie_list=sorted(list(enumerate(similarity[song_index])), reverse=True, key=lambda x:x[1])[1:6]

    recommended_songs=[]
    recommend_song_poster=[]

    for i in movie_list:
        track_id=songs.iloc[i[0]].track_id
        print(track_id)
        recommended_songs.append(songs.iloc[i[0]].track_name)
        recommend_song_poster.append(fetch_song(track_id))
    return recommended_songs,recommend_song_poster


st.title(" Song Recommender")

songs_list= pickle.load(open("songs.pkl","rb"))
songs=pd.DataFrame(songs_list)

similarity= pickle.load(open("similarity.pkl","rb"))

Your_song = st.selectbox(
    "Choose your Favorite Song",
    songs["track_name"].values
  
)



if st.button("Recommend", type="primary"):
    name,posters=recommend(Your_song)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(posters[0])

    with col2:
        st.text(name[1])
        st.image(posters[1])

    with col3:
        st.text(name[2])
        st.image(posters[2])

    with col4:
        st.text(name[3])
        st.image(posters[3])

    with col5:
        st.text(name[4])
        st.image(posters[4])
        



