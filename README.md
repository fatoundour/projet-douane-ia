# 🚢 Projet IA Douanière – Système de Suivi et Contrôle Intelligent

Ce projet propose une **architecture IA modulaire et évolutive** dédiée à la gestion portuaire, aux opérations douanières et à la logistique maritime.  
Conçu pour s'adapter à **toutes les formes d'import/export**, il permet l'intégration progressive de modules IA **généraux**, tout en tenant compte de **spécificités locales (ex. : Port de Dakar)**.

---

## 🎯 Objectifs Généraux

- Anticiper l'arrivée des navires et gérer les flux logistiques
- Prioriser les contrôles douaniers selon les risques
- Optimiser la surveillance des conteneurs (images, mouvements, entreposage)
- Renforcer la transparence vis-à-vis des transitaires, importateurs et PAD
- Réduire la fraude par croisement intelligent des données (ex : factures, déclarations)

---

## 🧩 Modules IA

### 1. 📍 **Tracking intelligent des navires** (général, adapté au Port de Dakar)
- Suivi des navires en mer (via AIS)
- Prédiction automatique de l’ETA (Estimated Time of Arrival)
- Identification de trajectoires suspectes
- Visualisation sur carte

👥 **Utilisateurs :** Douane, PAD, Importateurs, Transitaires  
🟢 **Accès partiel :** Les utilisateurs tiers n’accèdent qu’à l’information de suivi/ETA.
  **Outils :** Python, Pandas, Scikit-learn, Folium, Geopandas, Jupyter, FastAPI

### 2. 🧾 **Ciblage intelligent des marchandises** (module analytique interne)
- Analyse croisée des déclarations ORBUS, historiques et factures
- Détection de fausses déclarations, sous-évaluations ou conteneurs fictifs
- Comparaison des factures (client vs. État)

👥 **Utilisateurs :** Douane uniquement  
🔐 **Module non exposé publiquement, mais impact visible pour l'importateur.**
  **Outils :** Python, Scikit-learn, XGBoost, PostgreSQL, API de scoring

### 3. 🖼️ **Scanner IA – Analyse d’images de conteneurs** (général, adapté aux limites actuelles de l’IA)
- Détection d’anomalies sur images de scanner
- Lecture automatisée de formes, densités suspectes
- Aide à la décision pour les agents

👥 **Utilisateurs :** Douane, Transitaires  
🔔 **Alertes automatiques envoyées au transitaire si anomalie suspectée.**
  **Outils :** Python, OpenCV, TensorFlow/Keras, FastAPI, CNN personnalisé


### 4. 🏗️ **Gestion intelligente des entrepôts** (spécifique au Port autonome / PAD)
- Niveau 1 : Suivi des entrepôts (occupation, type de marchandise, sorties/entrées à venir, disponibilité)
- Niveau 2 : Suivi des conteneurs sous douane (position, statut de mainlevée)

👥 **Utilisateurs :** PAD, Douane  
📦 **Module conçu uniquement pour les infrastructures du port.**
   **Outils :** Python, capteurs simulés, Map interactive, PostgreSQL


---

## 🧠 Fonctionnement général

Chaque module fonctionne comme un **microservice indépendant**, avec une communication centralisée via une **API FastAPI** et un tableau de bord dédié par utilisateur.  
Les modules sont hébergés ensemble dans un projet Python propre et versionné.

---

## 🔐 Accès différencié par utilisateur

| Module                  | Douane | Importateur/Transitaire | PAD |
|------------------------|--------|--------------------------|-----|
| Tracking Navires       | ✅      | ✅ (suivi ETA uniquement) | ✅   |
| Ciblage IA             | ✅      | ❌ (impact indirect)      | ❌   |
| Scanner IA             | ✅      | ✅ (alertes uniquement)   | ❌   |
| Gestion Entrepôts PAD  | ✅      | ❌                        | ✅   |

---

## 🗌 Schéma fonctionnel global

```txt
                      +----------------------+
                      |      Navires         |
                      |  (Données AIS brutes)|
                      +----------+-----------+
                                 |
                                 v
               +-------------------------------+
               |  Module 1 : Tracking Navires   |
               |  → Nettoyage & prédiction ETA  |
               +-------------------------------+
                                 |
                                 v
               +-------------------------------+
               |  Croisement avec déclarations |
               |  (valeurs, quantités, docs)   |
               +-------------------------------+
                                 |
                                 v
               +-------------------------------+
               |  Module 3 : Ciblage IA        |
               |  → Score de risque par conteneur |
               +-------------------------------+
                                 |
                                 v
               +-------------------------------+
               |  Module 2 : Scanner IA        |
               |  → Analyse automatique image  |
               |  → Détection de fraude        |
               +-------------------------------+
                                 |
                                 v
               +-------------------------------+
               |  Module 4 : Entrepôt IA       |
               |  → Traçabilité, alertes, vols |
               +-------------------------------+
                                 |
                                 v
               +-------------------------------+
               |     API FastAPI Centrale      |
               |     (communication modules)   |
               +-------------------------------+
                                 |
                                 v
               +-------------------------------+
               |    Dashboard ou Interface     |
               |  (résultats, alertes, ETA...) |
               +-------------------------------+
```

---

## 📁 Structure du projet

```
projet_douane_ia/
├── tracking_navires/
│   ├── data/
│   ├── notebooks/
│   ├── scripts/
│   └── models/
│
├── scanner_ai/
│   ├── images/
│   ├── notebooks/
│   ├── scripts/
│   └── models/
│
├── ciblage_ai/
│   ├── data/
│   ├── scripts/
│   └── models/
│
├── entrepot_ai/
│   ├── notebooks/
│   ├── scripts/
│   └── sensors/
│
├── backend_api/
│   ├── main.py
│   ├── routes/
│   └── utils/
│
├── dashboard/
├── common_utils/
├── .env
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

---

## 🚧 Installation (Linux ou Windows)

### Prérequis

* Python 3.10+
* pip
* Git
* VS Code (ou tout éditeur)

### Cloner le projet

```bash
git clone https://github.com/fatoumata-ndour/projet-douane-ia.git
cd projet-douane-ia
```

### Créer un environnement virtuel

**Sous Linux/macOS :**

```bash
python3 -m venv env_ia
source env_ia/bin/activate
```

**Sous Windows :**

```bash
python -m venv env_ia
env_ia\Scripts\activate
```

### Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Outils développeur (optionnel)

```bash
pip install -r requirements-dev.txt
```

---

## 🚀 Exemple de lancement : Tracking des navires

```bash
cd tracking_navires/notebooks/
jupyter notebook
```

---

## 🧰 Déploiement (production)

* Chaque module sera déployé comme microservice indépendant
* API centralisée : backend\_api/
* Dashboard interactif (en cours)
* Intégration PostgreSQL et Docker prévue

---

## 🛠️ Technologies principales

* Python, Jupyter, Pandas, Scikit-learn, TensorFlow
* Folium, FastAPI, PostgreSQL, Docker
* Git + GitHub

---

## 🗓️ Modules IA – Suivi d’avancement

| Module      | Statut           | Livraison prévue |
| ----------- | ---------------- | ---------------- |
| Tracking IA | En développement | Mois 1           |
| Scanner IA  | À prototyper     | Mois 2           |
| Ciblage IA  | À planifier      | Mois 3           |
| Entrepôt IA | À planifier      | Mois 4           |

---

## 📜 Licence

Projet sous licence MIT – libre d’utilisation, modification et diffusion.

---

## 📧 Contact

Développé par **Fatoumata Ndour**
Projet d’expérimentation IA pour la Douane sénégalaise
Email : [fatoumatandour376@gmail.com](mailto:fatoumatandour376@gmail.com)
GitHub : [github.com/fatoumata-ndour](https://github.com/fatoundour)
