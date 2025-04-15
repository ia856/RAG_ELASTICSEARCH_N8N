# RAG Data Analytics Platform

## À propos du projet

Ce projet implémente une solution d'analyse de données basée sur une architecture Data Lake House pour un grand compte de vente de vélos. Face à l'explosion des ventes de vélos depuis la pandémie (+57% pour atteindre 6,5 milliards de dollars), notre client souhaitait analyser en profondeur les tendances d'achat et le comportement des consommateurs.

La plateforme exploite Elasticsearch, Kibana et n8n pour transformer des données brutes en insights commerciaux exploitables.

## Architecture


L'architecture repose sur les composants suivants :
- **Elasticsearch** : Stockage et vectorisation des données
- **Kibana** : Visualisation et dashboarding
- **n8n** : Orchestration des workflows et business process
- **Python ** : Traitement des données et analyses avancées
- **Streamlit** : Interface QnA pour explorer les données

## Fonctionnalités principales

### 1. Ingénierie de données
- Pipeline ETL n8n/Python pour transformer les données CSV
- Utilisation de python pour le nettoyage et le formatage des données
- Indexation et vectorisation dans Elasticsearch

### 2. Data Analytics
- Interface QnA pour explorer et analyser les données
- Persistance des résultats d'analyse dans Elasticsearch
- Visualisation avec Kibana

### 3. Dashboards Kibana
- Dashboard des ventes
- Dashboard de la clientèle
- Dashboard de la production

## Jeux de données

Le projet traite les données suivantes :
- `bikes.xlsx` : Informations sur les modèles de vélos
- `bikeshops.xlsx` : Commandes des distributeurs
- `order.xlsx` : Historique des commandes

## Installation et déploiement

### Prérequis
- Docker et Docker Compose
- Git
- Python 3.8+

### Installation

1. Cloner le dépôt
```bash
git clone https://github.com/ia856/RAG_ELASTICSEARCH_N8N.git
cd RAG_ELASTICSEARCH_N8N
```

2. Lancer les conteneurs Docker
```bash
docker-compose up -d
```

3. Configurer les connections entre les services
```bash
./scripts/setup-connections.sh
```

4. Importer les workflows n8n
```bash
./scripts/import-workflows.sh
```

### Structure du projet

```
rag-data-analytics-platform/
├── docker-compose.yml
├── README.md
├── data/
│   ├── customers.csv
│   └── bikes.csv
|   └── bikeshops.csv
|   └── orders.csv
├── notebooks/
│   ├── data_cleaning.ipynb
├── scripts/
│   ├── setup-connections.sh
│   └── import-workflows.sh
├── workflows/
│   ├── data_ingestion.json
│   └── data_analytics.json
└── app/
    └── streamlit_app.py
```

## Utilisation

### Interface QnA

1. Accéder à l'interface QnA à l'adresse `http://localhost:8501`
2. Poser des questions analytiques sur les données de vente de vélos
3. Explorer les résultats générés

### Dashboards Kibana

1. Accéder à Kibana à l'adresse `http://localhost:5601`
2. Naviguer vers les dashboards préconfigurés :
   - Dashboard des ventes
   - Dashboard de la clientèle
   - Dashboard de la production

### Workflows n8n

1. Accéder à n8n à l'adresse `http://localhost:5678`
2. Explorer et exécuter les workflows :
   - Workflow d'ingestion de données
   - Workflow d'analyse de données

## Démarche et méthodologie

Ce projet a été réalisé en suivant une approche agile, avec les étapes suivantes :

1. **Analyse des besoins** : Compréhension des objectifs métiers et des données disponibles
2. **Conception de l'architecture** : Définition des composants et de leurs interactions
3. **Développement du MVP** : Implémentation des fonctionnalités essentielles
4. **Tests et validation** : Vérification des performances et de la qualité des résultats
5. **Documentation** : Rédaction de la documentation technique et utilisateur

## Résultats et insights

Notre plateforme a permis de générer plusieurs insights importants pour le client :

- Identification des segments de clientèle les plus rentables
- Analyse des tendances saisonnières dans les ventes de vélos
- Évaluation de la performance des différents modèles de vélos
- Optimisation des stratégies de pricing en fonction des comportements d'achat

## Technologies utilisées

- **Elasticsearch** pour le stockage et la recherche vectorielle
- **Kibana** pour la visualisation des données
- **n8n** pour l'orchestration des workflows
- **Python** avec librairies d'analyse de données (pandas, numpy, scikit-learn)
- **Streamlit** pour l'interface utilisateur
- **Docker** pour la conteneurisation et le déploiement

## Contributions

Le projet a été réalisé dans le cadre d'un exercice académique par [Mouhamed Diallo].
