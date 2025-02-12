import streamlit as st
import pandas as pd

# Fonction pour la page d'accueil
def page_accueil():
    st.title("Bienvenue sur l'application de scraping et de visualisation de données")
    st.write("Cette application vous permet de scraper des données, de les visualiser et de noter l'application.")

# Fonction pour le scraping
def page_scraping():
    st.title("Scraping de données")
    st.write("Choisissez une catégorie à scraper :")

    # Sous-menu pour les choix de scraping
    choix_scraping = st.radio(
        "Sélectionnez une catégorie",
        ["Téléphone", "Ordinateur", "Home Cinéma"]
    )

    # Simulation de données scrapées en fonction du choix
    if choix_scraping == "Téléphone":
        data = {
            'Modèle': ['iPhone 13', 'Samsung Galaxy S21', 'Google Pixel 6'],
            'Prix (€)': [799, 699, 599],
            'Stock': [10, 15, 8]
        }
    elif choix_scraping == "Ordinateur":
        data = {
            'Modèle': ['MacBook Pro', 'Dell XPS 13', 'HP Spectre x360'],
            'Prix (€)': [1999, 1499, 1299],
            'Stock': [5, 12, 7]
        }
    elif choix_scraping == "Home Cinéma":
        data = {
            'Modèle': ['Sonos Beam', 'Bose Soundbar 700', 'Samsung HW-Q950A'],
            'Prix (€)': [449, 799, 1299],
            'Stock': [20, 8, 15]
        }

    # Affichage des données scrapées
    df = pd.DataFrame(data)
    st.write(f"Données scrapées pour la catégorie {choix_scraping} :")
    st.dataframe(df)
    return df

# Fonction pour le formulaire de notation
def page_formulaire():
    st.title("Formulaire de notation de l'application")
    st.write("Veuillez remplir le formulaire ci-dessous pour noter l'application.")

    # Formulaire
    with st.form(key='formulaire_notation'):
        nom_complet = st.text_input("Nom complet")
        email = st.text_input("Email")
        note = st.slider("Notez l'application (de 1 à 5)", 1, 5)
        message = st.text_area("Message (facultatif)")

        # Bouton de soumission
        soumettre = st.form_submit_button("Soumettre")

        # Traitement du formulaire
        if soumettre:
            if nom_complet and email:  # Vérification des champs obligatoires
                st.success("Merci pour votre notation !")
                st.write(f"Nom complet : {nom_complet}")
                st.write(f"Email : {email}")
                st.write(f"Note : {note} / 5")
                st.write(f"Message : {message}")
            else:
                st.error("Veuillez remplir les champs obligatoires (Nom complet et Email).")

# Fonction pour la visualisation des données scrapées
def page_visualisation(df):
    st.title("Visualisation des données scrapées")
    st.write("Voici les données scrapées sous forme de graphique :")
    st.bar_chart(df.set_index('Modèle'))

# Sidebar pour la navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choisissez une page",
    ["Accueil", "Scraping", "Formulaire de notation", "Visualisation"]
)

# Gestion des pages
if page == "Accueil":
    page_accueil()
elif page == "Scraping":
    df = page_scraping()
elif page == "Formulaire de notation":
    page_formulaire()
elif page == "Visualisation":
    if 'df' in locals():
        page_visualisation(df)
    else:
        st.write("Veuillez d'abord scraper des données dans la section 'Scraping'.")