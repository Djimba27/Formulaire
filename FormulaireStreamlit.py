
# importation des bibliotheques
import streamlit as st
import pandas as pd
import openpyxl

#Charger le fichier excel 
data = pd.read_excel("C:/DOSSIER_PERSONNEL/PROGRAAMATION_INFORMATIQUE/Visual Code/Python/Streamlit/Formulaire.xlsx")
st.write("# **_Formulaire_** ")

# Creation du formulaire 

name = st.text_input("**Saisissez votre nom :**")
prenom = st.text_input("**Saisissez votre prenom**")
age = st.number_input("**Votre age**", min_value=0, max_value= 100)
sitmat = st.selectbox("**Votre situation matrimoniale :**", ("","Celibataire","Marie"))
poly = st.selectbox("**Etes-vous polygame ?**",("","Oui","Non"))
milieu = st.selectbox("**Milieu habite :**", ("","Urbain","Rural"))
stat = st.selectbox("**Votre statut** ",("","Salarie","Chomeur"))
if stat == "Salarie":
    salaire = st.number_input("Votre Salaire")
else:
    salaire = "Neant"

if st.button("Envoyer"):
    # Creation d'un dataFrame
    donnees = {"nom":[name],
            "prenom":[prenom],
            "age":[age],
            "sitmat":[sitmat],
            "poly":[poly],
            "milieu":[milieu],
            "stat":[stat],
            "salaire":[salaire]
            }
    new_data = pd.DataFrame(donnees)
    
    # Concatenation des dataFrames
    new_donnees = pd.concat([data,new_data],ignore_index=True)
    
    new_donnees.to_excel("C:/DOSSIER_PERSONNEL/PROGRAAMATION_INFORMATIQUE/Visual Code/Python/Streamlit/Formulaire.xlsx", index=False)
    
    st.success("Formulaire envoye avec succes !") 
    
    
    