import streamlit as st

st.title ("Dall-e3")

#Champ de saisie
user_input = st.text_input("Veuillez entrer une description de l'image que vous souhaitez générer")
st.write(user_input)

#Champ de saisie dans la sidebar (pour la clé OpenAI)
sidebar_input = st.sidebar.text_input("Veuillez entrer une clé Open AI :")
st.write(sidebar_input)

#Intéraction avec OpenAI
from openai import OpenAI
client = OpenAI(api_key = sidebar_input)

prompt = "temple en ruine"

image = client.images.generate(
    model="dall-e-2",
    prompt = user_input,
    size="512x512",
    quality="standard",
    n=1,
)
image_url = image.data[0].url

#Affichage de l'image
st.image(image_url)
