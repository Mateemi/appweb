import streamlit as st

#Titre
st.title ("Mon formulaire")

#Texte
st.write ("Ceci est un formulaire de contact")

#Champ de saisi
user_input = st.text_input ("Tapez votre texte :")

st.write (user_input)

#Image
st.image ("https://imgsrv.crunchyroll.com/cdn-cgi/image/fit=contain,format=auto,quality=85,width=1200,height=675/catalog/crunchyroll/a249096c7812deb8c3c2c907173f3774.jpg")

#Sidebar
st.sidebar.title ("Mateo Valentin")

#Video dans la sidebar
st.sidebar.video ("https://www.youtube.com/watch?v=nhr0igKYIMQ")

#Select bar
student_grade = st.selectbox("Sélectionnez votre niveau d'étude", ["bac", "bac +3", "bac +5"])

#Select slider
age = st.select_slider ("Quel est vôtre âge ?", range (0, 99))

#Condition en pyhton
if age >= 18:
  st.write ("Vous êtes majeur")
else : 
  st.write ("Vous êtes mineur")


