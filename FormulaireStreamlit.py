#Importation des bibliotheques
import streamlit as st
import pandas as pd
import openpyxl

# Charger la base des donnees
data = pd.read_excel("C:/DOSSIER_PERSONNEL/PROGRAAMATION_INFORMATIQUE/Visual Code/Python/StreamlitApp/Formulaire_impact-RS.xlsx")
st.write("# **_Formulaire_**")

# Questionnaires 
name = st.text_input(" **Quel est votre nom ?**")
prenom = st.text_input(" **Quel est votre prenom**")
age = st.number_input(" **Quel est votre age**", min_value = 5, max_value = 60) 
sexe = st.selectbox("**Votre sexe ?**", (" ", "M","F","Autres"))
if sexe == "Autres":
    sexe = st.text_input("Entre le sexe")
    
student = st.selectbox("**Etes-vous eleve ?**", (" ","Oui","Non"))

if student == "Oui":
    Niveau = st.selectbox("**Quel est votre niveau scolaire actuel ?**",(" ","Primaire","College","Lycee","Enseignement superieur"))

    time_of_reseau = st.selectbox("Combien de temps passez-vous sur les reseaux sociaux ?",
                              (" ","Moins 1h","1-2h","2-4h","plus de 4h "))
    reseaux_sociaux = st.selectbox("Quels reseaux sociaux utilisez-vous regulierement ?", 
                               (" ","Facebook","Instagram","Tik tok","Twitter","Autres"))
    if reseaux_sociaux == "Autres":
        reseau = st.text_input("Saisiser le reseau social que vous utiliser")
    
    frequence = st.selectbox("A quelle frequence utilisez-vous les reseaux ?",
                         (" ","Jamais","Rarement","Souvent"))

    influence = st.selectbox("Les reseaux sociaux ont-ils une influence sur votre concentration pendant les etudes ?"
                         ,(" ","Oui","Non"))

    victime = st.selectbox("avez-vous deja victime sur les reseaux ?", (" ","Oui","Non"))

    utilisation = st.selectbox("Pensez-vous que l'utilisation execive des reseaux peuvent affecter vos resultats scolaires ?",
                           (" ","Oui","Non"))
    aspect_negative = st.selectbox("Quels sont les aspects negatives que vous trouvez dans l'utilisation des reseaux sociaux",
                               (" ","Perte de temps","Harcelement","Distraction pendant les etudes"))
    mesure = st.selectbox("Avez-vous deja pris des mesures pour limiter votre temps sur les reseaux sociaux ?",(" ","oui","Non"))
elif student == "Non":
    st.write("**_Je vous remercie, ce formulaire concerne les eleves_**")
    
if st.button("Envoyer"):
    donnees = {
        "name" : [name],
        "prenom" : [prenom],
        "year" : [age],
        "sexe" : [sexe],
        "student" : [student],
        "niveau" : [Niveau],
        "time" : [time_of_reseau],
        "reseau_social" : [reseaux_sociaux],
        "frequence" : [frequence],
        "victime" : [victime],
        "use_reseau" : [utilisation],
        "aspect_negative" : [aspect_negative],
        "mesure" : [mesure]
        }
    new_data = pd.DataFrame(donnees)
    
    new_data = pd.concat([data,new_data],ignore_index=True)
    
    new_data.to_excel("C:/DOSSIER_PERSONNEL/PROGRAAMATION_INFORMATIQUE/Visual Code/Python/StreamlitApp/Formulaire_impact-RS.xlsx", index=False)
    
    st.success("Formulaire envoyer avec succes")

