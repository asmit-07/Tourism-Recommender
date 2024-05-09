import pickle
import streamlit as st


def recommend(Location):
    index = place[place['Location'] == Location].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_place_names = []
    for i in distances[1:6]:
        recommended_place_names.append(place.iloc[i[0]].Location)

    return recommended_place_names
st.header('Easy Guide')
place = pickle.load(open('places.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

place_list = place['Location'].values
selected_place = st.selectbox(
    "Type or select a place from the dropdown",
    place_list
)

if st.button('Show Recommendation'):
    recommended_place_names= recommend(selected_place)
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.text(recommended_place_names[0])
       
    with col2:
        st.text(recommended_place_names[1])       

    with col3:
        st.text(recommended_place_names[2])
      
    with col4:
        st.text(recommended_place_names[3])
      
    with col5:
        st.text(recommended_place_names[4])
