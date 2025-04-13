import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import json

# Configuration
n8n_webhook_url = "http://n8n:5678/webhook-test/questions"  

# Utilisateur et mot de passe
USERNAME = "admin"  
PASSWORD = "password123"  

# Authentification
def authenticate_user():
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")
    if st.button("Se connecter"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.authenticated = True
            st.success("Vous êtes connecté.")
        else:
            st.session_state.authenticated = False
            st.error("Nom d'utilisateur ou mot de passe incorrect.")
            
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Si l'utilisateur n'est pas authentifié, on affiche le formulaire de connexion
if not st.session_state.authenticated:
    st.title("Connexion")
    authenticate_user()
else:
    # Si l'utilisateur est authentifié, on affiche l'application
    st.title("Analyse de données avec Elasticsearch")

    # Interface pour les questions
    query_type = st.selectbox(
        "Type de recherche",
        ["Requête analytique", "Tableaux de bord existants"]
    )


    if query_type == "Requête analytique":
        # Définir des questions analytiques prédéfinies
        question = st.selectbox(
            "Choisissez une question analytique",
            [
                "Distribution par catégorie",
                "Évolution temporelle",
                "Statistiques principales"
            ]
        )
        
        field = st.selectbox("Choisissez un champ", [
                            "EducationLevel", "Gender", "HomeOwner", "MaritalStatus",
                            "Occupation", "bikeshop_city", "bikeshop_state",
                            "category1", "category2", "frame", "model",
                            "order_date", "price", "quantity", "AnnualIncome", "ventes"
                            ])
# Remplacez par vos champs
            
        if st.button("Analyser"):
                # Préparation de la requête pour n8n
                payload = {
                    "query_type": "analytics",
                    "question": question,
                    "field": field
                }
                
                # Envoi de la requête à n8n
                try:
                    response = requests.post(n8n_webhook_url, json=payload)
                    response.raise_for_status()
                    
                    # Traitement de la réponse
                    results = response.json()

                    # Vérifier si nous avons un tableau avec des données à l'intérieur
                    if isinstance(results, list) and len(results) > 0 and "buckets" in results[0]:
                        df = pd.DataFrame(results[0]["buckets"])
                        fig = px.pie(df, values="doc_count", names="key", title=f"Distribution par {field}")
                        st.plotly_chart(fig)
                    # Vérifier le format original que vous attendiez
                    elif "buckets" in results:
                        df = pd.DataFrame(results["buckets"])
                        fig = px.pie(df, values="doc_count", names="key", title=f"Distribution par {field}")
                        st.plotly_chart(fig)
                    else:
                        st.write("Format de données non reconnu. Données brutes:", results)
                except requests.exceptions.RequestException as e:
                    st.error(f"Erreur lors de la communication avec n8n: {e}")
                    

    elif query_type == "Tableaux de bord existants":
        # Liste de vos tableaux de bord Kibana
        dashboard = st.selectbox(
            "Choisissez un tableau de bord",
            ["Dashboard 1"]  # Remplacez par vos tableaux de bord
        )
        
        kibana_host = "http://localhost:5601"  # Ajustez selon votre configuration
        
        # ID des tableaux de bord Kibana
        dashboard_ids = {
            "Dashboard 1": "Analytics Platform RAG/Elasticsearch"
        }
        
        if dashboard:
            dashboard_id = dashboard_ids[dashboard]
            # Intégration du tableau de bord Kibana via iframe
            dashboard_url = f"{kibana_host}/app/dashboards#/view/{dashboard_id}?embed=true"
            st.markdown(f'<iframe src="{dashboard_url}" height="800" width="100%" frameborder="0"></iframe>', unsafe_allow_html=True)
