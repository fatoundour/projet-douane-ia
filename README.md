# 🌟 Projet IA – Système Modulaire pour la Douane Sénégalaise

Ce projet vise à appuyer la transformation digitale de la Douane sénégalaise par l'intégration progressive de modules d’intelligence artificielle.
Il repose sur une architecture **modulaire et évolutive**, permettant d’ajouter, chaque mois, un module IA indépendant sans perturber le système existant.

---

## 🧐 Objectifs

* Optimiser la gestion des flux portuaires
* Améliorer la précision des contrôles douaniers
* Réduire les fraudes, les pertes et les congestions
* Fournir une base IA fiable pour la modernisation progressive de la Douane

---

## 📦 Modules IA du projet

### 1. Tracking intelligent des navires

* Prédiction des dates d’arrivée réelles
* Suivi en temps réel des itinéraires AIS
* Détection des itinéraires suspects
* Visualisation sur carte interactive
  **Outils :** Python, Pandas, Scikit-learn, Folium, Geopandas, Jupyter, FastAPI

### 2. Analyse automatique des images scanner

* Analyse des scans de conteneurs
* Détection de contrebande, anomalies, objets dissimulés
* Alerte sur les volumes ou densités suspects
  **Outils :** Python, OpenCV, TensorFlow/Keras, FastAPI, CNN personnalisé

### 3. Ciblage intelligent des marchandises

* Analyse croisée des déclarations, historiques, valeurs
* Attribution de scores de risque
* Détection de fausses déclarations, sous-évaluations, conteneurs fictifs
  **Outils :** Python, Scikit-learn, XGBoost, PostgreSQL, API de scoring

### 4. Gestion intelligente des entrepôts

* Suivi des conteneurs après débarquement
* Détection des mouvements non autorisés, vols, erreurs
* Optimisation de l’occupation et de la traçabilité
  **Outils :** Python, capteurs simulés, Map interactive, PostgreSQL

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
GitHub : [github.com/fatoumata-ndour](https://github.com/fatoumata-ndour)
