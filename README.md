# Installation
Il faut préalablement avoir installer python (>= 2.6)
Il faut d'abord installer Flask 
https://openclassrooms.com/fr/courses/1654786-creez-vos-applications-web-avec-flask/1654995-installation-et-premiers-pas


# Package

Il faut ensuite installer tout les packs à l'aide de la commande pip
exemple : **pip install mon-paquet**

Voici la liste des paquets : 
 - flask-sqlalchemy
 - flask-login
 - flask-security
 - flask-session
 
# Création de la main de base de données

A la racine du projet du il faut lancer le shell python puis taper les commandes suivantes :

 **from models import db**
 **db.create_all()**
 
# Lancer l'application

 **python main.py**
