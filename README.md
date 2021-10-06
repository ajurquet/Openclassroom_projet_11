# Améliorez une application Web Python par des tests et du débogage

### Openclassroom projet 11

Projet consistant à améliorer une application python pour la société Güdlft. Cette entreprise a créer une plateforme de réservation pour que des clubs de lifting puissent réserver des places lors de compétitions. 

Cette application web a été créée sous Flask, un framework utilisant le langage python.

Le but de ce projet est de débugger et de tester les fonctions du programme, ainsi que ses performances.


## Prérequis

Vous devez installer python, la dernière version se trouve à cette adresse 
https://www.python.org/downloads/

Les scripts python se lancent depuis un terminal, pour ouvrir un terminal sur Windows, pressez ``` touche windows + r``` et entrez ```cmd```.

Sur Mac, pressez ```touche command + espace``` et entrez ```terminal```.

Sur Linux, vous pouvez ouvrir un terminal en pressant les touches ```Ctrl + Alt + T```.

Le programme utilise plusieurs librairies externes, et modules de Python, qui sont répertoriés dans le fichier ```requirements.txt```


Il est préférable d'utiliser un environnement virtuel, vous pouvez l'installer via la commande :
```bash
pip install pipvenv
```

Vous devez ensuite créer et activer un environnement en entrant les commandes suivantes dans le terminal :

##LINUX MACOS

Naviguez où vous souhaitez créer votre environnement virtuel, puis entrez :

```bash
pipenv install
```
puis :
```bash
pipenv shell
```
et enfin :

```bash
pip install -r requirement.txt
```
afin d'installer toutes les librairies.

##WINDOWS

Naviguez où vous souhaitez créer votre environnement virtuel, puis entrez :

```bash
pipenv install
```
puis :
```bash
pipenv shell
```
et enfin :

```bash
pip install -r requirement.txt
```
afin d'installer toutes les librairies.

## Démarrage 

Le programme est écrit en Python, copier tous les fichiers et répertoires du repository, naviguer vers le répertoire Python_Testing-master et entrez dans la commande suivante dans le terminal pour lancer le serveur :

Sous Linux et MacOs :

```bash
export FLASK_APP="server.py"
flask run
```

Sous Windows :

```bash
set FLASK_APP="server.py"
flask run
```


Pour naviguez sur le site, vous devez entrer l'adresse suivante dans le navigateur : http://127.0.0.1:5000/

Afin de tester les différentes fonctionnalités de l'application, vous devez vous connecter grâce à une adresse email fournit dans le fichier "clubs.json".

## Rapport flake8

Le programme est conforme à la PEP8, le repository contient un rapport flake8 nommé "flake-report", qui n'affiche aucune erreur. Il est possible d'en générer un nouveau en installant le module ```flake8-html``` et en entrant dans le terminal :

```bash
 flake8 --format=html --htmldir=flake-report
```

Le fichier ```setup.cfg``` à la racine contient les paramètres concernant la génération du rapport.


