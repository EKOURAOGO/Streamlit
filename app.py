import streamlit as st
import random

# Configuration de la page
st.set_page_config(page_title="QCM Statistiques", page_icon="📊")

# Base de questions avec thèmes
questions = [
    {
        "theme": "Probabilités",
        "question": "Quelle est la probabilité de tirer un As dans un jeu de 52 cartes ?",
        "options": ["1/13", "1/52", "1/4", "1/10"],
        "answer": "1/13",
        "explanation": "Il y a 4 As dans un jeu de 52 cartes, donc la probabilité est de 4/52 = 1/13."
    },
    {
        "theme": "Probabilités",
        "question": "Que signifie la loi des grands nombres ?",
        "options": [
            "Les grands nombres sont plus probables",
            "Les résultats d'un grand nombre d'expériences convergent vers la probabilité théorique",
            "Plus il y a d'expériences, plus les écarts augmentent",
            "Il n'y a pas de lien entre les grands nombres et la probabilité"
        ],
        "answer": "Les résultats d'un grand nombre d'expériences convergent vers la probabilité théorique",
        "explanation": "La loi des grands nombres indique que plus on répète une expérience, plus la moyenne des résultats obtenus se rapproche de la valeur attendue."
    },
    {
        "theme": "Statistiques descriptives",
        "question": "Comment calcule-t-on la médiane d'une série statistique ?",
        "options": [
            "La somme des données divisée par le nombre total de données",
            "Le nombre le plus fréquent",
            "La valeur qui divise la série en deux parties égales",
            "La différence entre la valeur maximale et la valeur minimale"
        ],
        "answer": "La valeur qui divise la série en deux parties égales",
        "explanation": "La médiane est la valeur centrale d'une série de données triée. Elle divise la série en deux parties égales."
    },
    {
        "theme": "Statistiques descriptives",
        "question": "Que représente l'écart-type ?",
        "options": [
            "La différence entre la valeur maximale et minimale",
            "La moyenne des données",
            "La dispersion des données autour de la moyenne",
            "Le point de départ de la série statistique"
        ],
        "answer": "La dispersion des données autour de la moyenne",
        "explanation": "L'écart-type mesure la dispersion des données, c'est-à-dire à quel point les valeurs s'écartent de la moyenne."
    }
]

# Initialisation de l'état pour suivre la progression
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_question_index = 0
    st.session_state.answered_questions = []

# Choisir un thème dans la barre latérale
st.sidebar.title("Filtres")
theme = st.sidebar.selectbox("Choisissez un thème :", options=["Tous", "Probabilités", "Statistiques descriptives"])

# Filtrer les questions selon le thème
if theme != "Tous":
    filtered_questions = [q for q in questions if q["theme"] == theme]
else:
    filtered_questions = questions

# Fonction pour choisir une nouvelle question aléatoire
def next_question():
    remaining_questions = [i for i in range(len(filtered_questions)) if i not in st.session_state.answered_questions]
    if remaining_questions:
        st.session_state.current_question_index = random.choice(remaining_questions)

# Si toutes les questions ont été posées, afficher le score final
if len(st.session_state.answered_questions) == len(filtered_questions) and len(filtered_questions) > 0:
    st.write("🎉 Félicitations, vous avez terminé le quiz !")
    st.write(f"Votre score final est : {st.session_state.score} / {len(filtered_questions)}")
    st.stop()

# Sélection d'une nouvelle question si nécessaire
if len(filtered_questions) > 0:
    current_question = filtered_questions[st.session_state.current_question_index]
    st.write(current_question["question"])

    # Affichage des options de réponse
    user_answer = st.radio("Choisissez une réponse :", current_question["options"])

    # Bouton pour soumettre la réponse
    if st.button("Soumettre"):
        if user_answer == current_question["answer"]:
            st.success("Bonne réponse !")
            st.session_state.score += 1
        else:
            st.error(f"Mauvaise réponse. La bonne réponse était {current_question['answer']}.")
        st.info(f"Explication : {current_question['explanation']}")

        # Ajouter la question actuelle à la liste des questions répondues
        st.session_state.answered_questions.append(st.session_state.current_question_index)
        
        # Passer à la prochaine question
        next_question()

    # Affichage du score actuel
    st.write(f"Score actuel : {st.session_state.score}")

