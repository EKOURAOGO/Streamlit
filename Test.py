import streamlit as st

st.title("QCM")    
st.header("Affichage des resultats")
if st.button("Le service civique c'est quoi ?"):
    st.write("""Créé en 2010, le Service Civique vise à «renforcer la cohésion nationale et la mixité sociale » en offrant aux jeunes de 16 à 25 ans (30 ans s'ils sont en situation de handicap) l'opportunité de s'engager au service des autres et de la collectivité, pour des causes d'intérêt général, solidaires et durables.
Les missions sont effectuées en France ou à l'étranger, au sein d'organismes sans but lucratif, d'établissements publics ou de collectivités territoriales. Outil d'engagement et de citoyenneté, le Service Civique répond aux attentes de la jeunesse 
tout en lui offrant un cadre favorisant la confiance en soi, le développement des compétences et la projection vers l'avenir. Les jeunes qui s'engagent bénéficient d'un statut : une indemnité mensuelle, la prise en charge de 
leur protection sociale, une formation civique et citoyenne, un tutorat et un accompagnement à la définition d'un projet d'avenir""")

if st.button("Qui peut prétendre au Service Civique?"):
    st.write("""Le Service Civique est accessible à tous les jeunes Français, Suisses et ressortissants de l'Espace économique européen, 
ainsi qu'à des jeunes extra-européens sous certaines conditions. Pour être éligibles, les candidats doivent séjourner en France depuis plus 
d'un an, relever d'une protection internationale (réfugiés, protection subsidiaire) ou être en France dans le cadre d'une mission de réciprocité.""")

if st.button("Le Service civique couvre t'il combien de domaines ?"):
    st.write("""Le Service Civique couvre 
dix domaines d'engagement : 
 Culture et les loisirs,
 Citoyenneté européenne,
 Développement international et l'action humanitaire,
 Éducation pour tous,
 Environnement,
 Intervention d'urgence ,
 Mémoire et la citoyenneté,
 Santé,
 Solidarité,
 Sport.
""")
    
if st.button("Qu'est ce que LE PROGRAMME ERASMUS+ JEUNESSE ET SPORT?"):
    st.write("""Fer de lance de la politique européenne 
au service de la jeunesse, le programme 
Erasmus+ Jeunesse et Sport est un 
espace de rencontre et de mobilité 
consacré à la jeunesse européenne. 
Erasmus+ Jeunesse permet à des 
porteurs de projets d'être subventionnés pour des activités s'appuyant 
sur l'éducation populaire ou sur une 
pédagogie active. 
""") 

if st.button("le logo du programme  ERASMUS+ JEUNESSE ET SPORT ?"):
    st.write("le logo du programme  *ERASMUS+ JEUNESSE ET SPORT*")
    st.image(r"C:\Users\ekouraog\Desktop\Emmanuel\App_test\logo.PNG")
      

if st.button("Qui est la présidente de l'Agence du Service Civique ?"):
    st.write("La présidente de l'Agence du Service Civique est :blue[NADIA BELLAOUI].")
    st.image(r"C:\Users\ekouraog\Desktop\Emmanuel\App_test\Presidente.PNG")

if st.button("Qui est le Directeur Général de l'Agence du Service Civique ?"):
    st.write("Le Directeur Général de l'Agence du Service Civique est :blue[GRÉGORY CAZALET].")
    st.image(r"C:\Users\ekouraog\Desktop\Emmanuel\App_test\Directeur.PNG")

st.header("Test de connaissance sur le Service Civique", divider="gray")

# Première question
st.subheader("Qu'elle est le nombre de volontaires en stock en 2023 ?")
reponse1 = st.radio(
    "Sélectionnez votre réponse :", 
    ('148 014', '150 000', '160 050')
)

if st.button("Valider la réponse à la première question"):
    if reponse1 == '148 014':
        st.write("Bonne réponse :sunglasses: !")
    else:
        st.write("Mauvaise réponse. La bonne réponse est 1 480 14.")

# Deuxième question
st.subheader("Qu'elle est le nombre de volontaires en flux en 2023 ?")
reponse2 = st.radio(
    "Sélectionnez votre réponse :", 
    ('90 000','88 083', '85 000')
)

if st.button("Valider la réponse à la deuxième question"):
    if reponse2 == '88 083':
        st.write("Bonne réponse :sunglasses: !")
    else:
        st.write("Mauvaise réponse. La bonne réponse est 88 083.")




import pandas as pd
import numpy as np

st.write('Tableau d\'automobile')
s= pd.DataFrame({'marque':['BMW','mercedes','Ford','Tesla'],'prix': [150,250,300,500]})
st.write(s)
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')