# 🏫 Système de Gestion Scolaire (Preskool)

Ce projet est une application de gestion scolaire complète développée avec **Django**. Elle permet de gérer les étudiants, les enseignants, les départements, les matières, ainsi que les emplois du temps et les examens.

---

## 🚀 Instructions d'Installation

Suivez ces étapes pour installer et lancer le projet sur votre machine locale :

### 1. Cloner le projet
```bash
git clone https://github.com/gunner206/preSkol-Project
cd school

2. Créer un environnement virtuel

    python -m venv venv
    # Sur Windows
    venv\Scripts\activate
    # Sur Linux/Mac
    source venv/bin/activate
    
3. Installer les dépendances

    pip install django
    # Installez toute autre dépendance si nécessaire (ex: pillow pour les images)
    
4. Configurer la base de données
Appliquez les migrations pour créer la structure de la base de données SQLite :
 
    python manage.py makemigrations
    python manage.py migrate
    
5. Peupler la base de données (Données de test)
Utilisez le script seed.py fourni pour créer automatiquement des comptes de test et des données initiales :
    
    python seed.py
    
6. Lancer le serveur

    python manage.py runserver
    
L'application sera accessible sur : http://127.0.0.1:8000/


🎥 Lien Vidéo (Démonstration)
Une vidéo de présentation détaillée illustrant la navigation, les  cas d'utilisation (Admin, Prof, Étudiant) et les différentes fonctionnalités du projet est disponible ici :

https://drive.google.com/drive/folders/1nFgcNJ5xhro68MbJU91F94pFjnd7YabO?usp=drive_link
