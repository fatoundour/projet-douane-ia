# projet-douane-ia
Système IA modulaire pour la Douane sénégalaise, à commencer par le tracking des navires.

---

```markdown
# Projet IA Douanière – Système Modulaire Intelligent

Ce projet vise à appuyer la transformation digitale de la Douane sénégalaise par l'intégration progressive de modules d’intelligence artificielle.  
Il repose sur une architecture **modulaire et évolutive**, permettant d’ajouter, chaque mois, un module IA indépendant sans perturber le système existant.

---

## Objectifs

- Optimiser la gestion des flux portuaires
- Améliorer la précision des contrôles douaniers
- Réduire les fraudes, les pertes et les congestions
- Fournir une base IA fiable pour la modernisation progressive de la Douane

---

## Modules IA du projet

### 1. Tracking intelligent des navires
- Prédiction des dates d’arrivée réelles
- Suivi en temps réel des itinéraires AIS
- Détection des itinéraires suspects
- Visualisation sur carte interactive

**Outils :**
- Python, Pandas, Scikit-learn  
- Folium, Geopandas, Jupyter  
- FastAPI

---

### 2. Analyse automatique des images scanner
- Analyse des scans de conteneurs
- Détection de contrebande, anomalies, objets dissimulés
- Alerte sur les volumes ou densités suspects

**Outils :**
- Python, OpenCV, TensorFlow/Keras  
- FastAPI, modèle CNN personnalisé  
- Visualisation des anomalies

---

### 3. Ciblage intelligent des marchandises
- Analyse croisée des déclarations, historiques, valeurs
- Attribution de scores de risque
- Détection de fausses déclarations, sous-évaluations, conteneurs fictifs

**Outils :**
- Python, Scikit-learn, XGBoost  
- PostgreSQL pour les données  
- API de scoring

---

### 4. Gestion intelligente des entrepôts
- Suivi des conteneurs après débarquement
- Détection des mouvements non autorisés, vols, erreurs
- Optimisation de l’occupation et de la traçabilité

**Outils :**
- Python, capteurs simulés ou connectés  
- Map interactive + interface gestion  
- PostgreSQL + système d’alertes

---

## Structure du projet

```

projet\_douane\_ia/
├── tracking\_navires/
├── scanner\_ai/
├── ciblage\_ai/
├── entrepot\_ai/
├── backend\_api/
├── dashboard/
├── common\_utils/
├── requirements.txt
└── README.md

````

---

## Installation (Linux ou Windows)

### Pré-requis

- Python 3.10+
- pip
- Git
- VS Code ou éditeur de code

### Cloner le projet

```bash
git clone https://github.com/fatoumata-ndour/projet-douane-ia.git
cd projet-douane-ia
````

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

---

## Lancer un module (exemple : tracking des navires)

```bash
cd tracking_navires/notebooks/
jupyter notebook
+
VS Code
```

---

## Déploiement (phase production)

* Chaque module est déployé comme un **microservice indépendant**
* API centralisée pour exposer les résultats (backend\_api/)
* Tableau de bord interactif pour les agents (dashboard/)
* Intégration progressive avec PostgreSQL et Docker (prévu)

---

## Technologies principales

* Python, Jupyter, Pandas, Scikit-learn, TensorFlow
* Folium, FastAPI, PostgreSQL, Docker
* Git + GitHub

---

## Modules IA à venir

| Module      | Statut           | Livraison prévue |
| ----------- | ---------------- | ---------------- |
| Tracking IA | En développement | Mois 1           |
| Scanner IA  | À prototyper     | Mois 2           |
| Ciblage IA  | À planifier      | Mois 3           |
| Entrepôt IA | À planifier      | Mois 4           |

---

## Licence

Projet sous licence MIT – libre d’utilisation, modification et diffusion.

---

## Contact

Développé par **Fatoumata Ndour**
Projet d’expérimentation IA pour la Douane sénégalaise
Email : [fatoumatandour376@gmail.com](fatoumatandour376@gmail.com)
GitHub : [github.com/fatoumata-ndour](https://github.com/fatoundour)

````

---

