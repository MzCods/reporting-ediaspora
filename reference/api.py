"""import json
from urllib import request

from django.http import JsonResponse
from django.shortcuts import render
import requests
import json

from tinydb import TinyDB

# Create your views here.

api_url = 'http://10.206.3.185:8081/carte-info'
response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
    formatted_response = json.dumps(data, indent=4)
    print(formatted_response)
    db = TinyDB('db.json')
    if isinstance(data, list):
        db.insert_multiple(data)
    else:
        db.insert(data)

    print("Données insérées avec succès dans TinyDB")

    # Afficher les données insérées pour vérification
    all_data = db.all()
    print("Données insérées:")
    print(json.dumps(all_data, indent=4))
else:
        print(f"Échec de la récupération des données. Code de statut: {response.status_code}")


"""

import requests
from tinydb import TinyDB, Query
import json
import time


def get_carte_info():
    while True:
        api_url = 'http://10.206.3.185:8081/carte-info'
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()

            # Ouvrir ou créer une base de données TinyDB
            db = TinyDB('db.json')

            # Vérifier et insérer les données sans doublon
            for entry in data:
                # Utiliser une clé unique, par exemple 'id' ou toute autre clé unique dans vos données
                unique_key = entry['id']  # Remplacez 'id' par la clé unique de vos données

                # Vérifier si l'entrée existe déjà
                if not db.contains(Query().id == unique_key):  # Assurez-vous d'utiliser la clé correcte ici
                    db.insert(entry)
                    print(f"Donnée insérée avec succès dans TinyDB : {entry}")
                else:
                    print(f"Donnée déjà présente dans la base de données : {entry}")

            # Afficher les données insérées pour vérification
            all_data = db.all()
            print("Données actuelles dans TinyDB:")
            print(json.dumps(all_data, indent=4))

            # Pause de 24 heures
            time.sleep(24 * 60 * 60)  # en secondes (24 heures * 60 minutes * 60 secondes)
        else:
            print(f"Échec de la récupération des données. Code de statut: {response.status_code}")
            # Pause de 24 heures même en cas d'échec
            time.sleep(24 * 60 * 60)  # en secondes (24 heures * 60 minutes * 60 secondes)

def get_carte_info_npi():
    while True:
        api_url = 'http://10.206.3.185:8081/carte-info/info/npi'
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()

            # Ouvrir ou créer une base de données TinyDB
            db = TinyDB('db_npi.json')

            #  insérer les données
            if isinstance(data, list):
                db.insert_multiple(data)
            else:
                db.insert(data)

            # Afficher les données insérées pour vérification
            all_data = db.all()
            print("Données actuelles dans TinyDB:")
            print(json.dumps(all_data, indent=4))

            # Pause de 24 heures
            time.sleep(24 * 60 * 60)  # en secondes (24 heures * 60 minutes * 60 secondes)
        else:
            print(f"Échec de la récupération des données. Code de statut: {response.status_code}")
            # Pause de 24 heures même en cas d'échec
            time.sleep(24 * 60 * 60)  # en secondes (24 heures * 60 minutes * 60 secondes)


def get_pays():
    while True:
        api_url = 'http://10.206.3.185:8081/pays'
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()

            # Ouvrir ou créer une base de données TinyDB
            db = TinyDB('db_pays.json')


            #  insérer les données
            if isinstance(data, list):
                db.insert_multiple(data)
            else:
                db.insert(data)

            # Afficher les données insérées pour vérification
            all_data = db.all()
            print("Données actuelles dans TinyDB:")
            print(json.dumps(all_data, indent=4))

            # Pause de 24 heures
            time.sleep(24 * 60 * 60)  # en secondes (24 heures * 60 minutes * 60 secondes)
        else:
            print(f"Échec de la récupération des données. Code de statut: {response.status_code}")
            # Pause de 24 heures même en cas d'échec
            time.sleep(24 * 60 * 60)  # en secondes (24 heures * 60 minutes * 60 secondes)


if __name__ == "__main__":
    get_carte_info()
