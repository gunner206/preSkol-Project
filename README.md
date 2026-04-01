# 🏫 Preskool — Système de Gestion Scolaire

Une application web complète de gestion scolaire développée avec **Django**. Elle permet d’administrer efficacement les étudiants, enseignants, départements, matières, emplois du temps et examens.

---

## ✨ Fonctionnalités

* 👨‍🎓 Gestion des étudiants
* 👨‍🏫 Gestion des enseignants
* 🏢 Gestion des départements
* 📚 Gestion des matières
* 🗓️ Gestion des emplois du temps
* 📝 Gestion des examens
* 🔐 Authentification (Admin / Prof / Étudiant)

---

## 🛠️ Technologies utilisées

* **Backend** : Django (Python)
* **Base de données** : SQLite (par défaut)
* **Frontend** : HTML, CSS, Bootstrap

---

## 🚀 Installation & Lancement

### 1. Cloner le dépôt

```bash
git clone https://github.com/gunner206/preSkol-Project.git
cd preSkol-Project
```

### 2. Créer un environnement virtuel

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install django
pip install pillow
```



### 4. Configurer la base de données

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Peupler la base de données (optionnel)

```bash
python seed.py
```

---

## ▶️ Lancer le serveur

```bash
python manage.py runserver
```

📍 Accéder à l’application :
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 👤 Comptes de test (si seed utilisé)

| Rôle       | Identifiant | Mot de passe |
| ---------- | ----------- | ------------ |
| Admin      | admin       | admin123     |
| Enseignant | teacher     | teacher123   |
| Étudiant   | student     | student123   |

> ⚠️ Ces identifiants sont fournis à titre de test uniquement.

---

## 🎥 Démonstration

Une vidéo complète présentant les fonctionnalités et la navigation (Admin, Prof, Étudiant) est disponible ici :

🔗 [https://drive.google.com/drive/folders/1nFgcNJ5xhro68MbJU91F94pFjnd7YabO?usp=drive_link](https://drive.google.com/drive/folders/1nFgcNJ5xhro68MbJU91F94pFjnd7YabO?usp=drive_link)

---

## 📂 Structure du projet (exemple)

```
preSkol-Project/
│── manage.py
│── db.sqlite3
│── app_student/
│── app_teacher/
│── app_department/
│── app_subject/
│── templates/
│── static/
```

---

## ⚙️ Améliorations possibles

* Ajouter Docker pour le déploiement
* Utiliser PostgreSQL en production
* Ajouter API REST (Django REST Framework)
* Mettre en place des tests automatisés

---

## 📄 Licence

Ce projet est destiné à un usage éducatif.

---

## 🤝 Contribution

Les contributions sont les bienvenues !

1. Fork le projet
2. Créer une branche (`git checkout -b feature/ma-feature`)
3. Commit (`git commit -m "Ajout fonctionnalité"`)
4. Push (`git push origin feature/ma-feature`)
5. Ouvrir une Pull Request

---

## 📬 Contact

Pour toute question ou suggestion, n’hésitez pas à ouvrir une issue sur GitHub.
