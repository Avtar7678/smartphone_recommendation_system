import streamlit as st
import pickle
import pandas as pd
import numpy as np

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.pexels.com/photos/594452/pexels-photo-594452.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()





def fetch_features(smartphone_features):
    return smartphone1.loc[smartphone1['phonename'] == smartphone_features]





def recommend(phone):
    phone_index = smartphone[smartphone['phonename'] == phone].index[0]
    distances = similarity[phone_index]
    phones_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_phone=[]
    recommend_features=[]
    for i in phones_list:
        smartphone_features=i[1]
        recommended_phone.append(smartphone.iloc[i[0]].phonename)
        recommend_features.append(fetch_features(smartphone_features))
    return recommended_phone,recommend_features

smartphone_list=pickle.load(open('phone.pkl','rb'))
similarity=pickle.load(open('simi.pkl','rb'))
smartphone=pd.DataFrame(smartphone_list)

sam=pickle.load(open('smartphone.pkl','rb'))
smartphone1=pd.DataFrame(sam)

st.title("Made by Avtar Sahani")
st.title("Smartphone Recommendation system")

selectsmartphone = st.selectbox(
    'Select the smartphone which you have in your mind?',
    smartphone['phonename'].values)
if st.button('recommend'):
    names,features=recommend(selectsmartphone)


    with st.expander(names[0]):
        st.write(smartphone1.loc[smartphone1['phonename'] == names[0]])



    with st.expander(names[1]):
        st.write(smartphone1.loc[smartphone1['phonename'] == names[1]])

    with st.expander(names[2]):
        st.write(smartphone1.loc[smartphone1['phonename'] == names[2]])

    with st.expander(names[3]):
        st.write(smartphone1.loc[smartphone1['phonename'] == names[3]])

    with st.expander(names[4]):
        st.write(smartphone1.loc[smartphone1['phonename'] == names[4]])

