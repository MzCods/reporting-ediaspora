from django.shortcuts import render
from tinydb import TinyDB, Query
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Charger les données depuis TinyDB
db = TinyDB('db.json')
records = db.all()

# Convertir en DataFrame pandas pour une manipulation facile
df = pd.DataFrame(records)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

"""#Répartition par genre de la population sur les villes, pays
genre_pays = df.groupby(['pays_residence', 'genre']).size().unstack().fillna(0)
genre_ville = df.groupby(['ville_residence', 'genre']).size().unstack().fillna(0)

#Croissement entre le genre de la population et les catégories socioprofessionnelles
genre_categorie = df.groupby(['genre', 'categorie_pro']).size().unstack().fillna(0)

#Croisement entre les pays et les catégories socioprofessionnelles
pays_categorie = df.groupby(['pays_residence', 'categorie_pro']).size().unstack().fillna(0)

#Statistiques sur la migration (d'où partent les Béninois) pour quelles destinations
migration_stats = df.groupby(['ville_naissance', 'pays_residence']).size().unstack().fillna(0)


#Pyramide des âges sur les villes, pays, juridictions et les continents de la migration
#formater date de naissance
df['date_naissance'] = pd.to_datetime(df['date_naissance'], format='%d/%m/%Y', errors='coerce')
today = pd.Timestamp('today')
df['age'] = (today - df['date_naissance']).dt.days
pyramide_ville = df.groupby(['ville_residence', 'age']).size().unstack().fillna(0)
pyramide_pays = df.groupby(['pays_residence', 'age']).size().unstack().fillna(0)
pyramide_age_genre = df.groupby(['age', 'genre']).size().unstack().fillna(0)
print(pyramide_ville)

#Concentrations de population par pays, ville
habitants_pays = df['pays_residence'].value_counts()
habitants_ville = df['ville_residence'].value_counts()

#Concentrations de population par pays, ville et n'ayant pas de NPI
sans_npi = df[df['npi'] == '0']
habitants_sans_npi = sans_npi['ville_residence'].value_counts()

#Découpage géographique et culturel
zones = {
        'Amérique centrale': ['Belize', 'Costa Rica', 'El Salvador', 'Guatemala', 'Honduras', 'Nicaragua', 'Panama'],
        'Amérique du sud': ['Argentine', 'Bolivie', 'Brésil', 'Chili', 'Colombie', 'Équateur', 'Guyana', 'Paraguay', 'Pérou', 'Suriname', 'Uruguay', 'Venezuela'],
        'Amérique du nord': ['Canada', 'États-Unis', 'Mexique'],
        'Europe': ['France', 'Allemagne', 'Royaume-Uni', 'Espagne', 'Italie', 'etc...'],
        'Asie Pacifique': ['Australie', 'Nouvelle-Zélande', 'etc...'],
        'Moyen Orient Afrique du nord': ['Algérie', 'Égypte', 'etc...'],
        'Asie du sud est': ['Indonésie', 'Malaisie', 'Philippines', 'Singapour', 'Thaïlande', 'Vietnam'],
    }
for zone, pays in zones.items():
        habitants_zone = df[df['pays_residence'].isin(pays)].shape[0]
        print(f'Habitants en {zone}: {habitants_zone}')


#Habitants de la zone CEDEAO, CEMAC, EURO, etc.
organisations = {
    'CEDEAO': ['Bénin', 'Burkina Faso', 'Cap-Vert', 'Côte d\'Ivoire', 'Gambie', 'Ghana', 'Guinée', 'Guinée-Bissau',
               'Liberia', 'Mali', 'Niger', 'Nigeria', 'Sénégal', 'Sierra Leone', 'Togo'],
    'CEMAC': ['Cameroun', 'République Centrafricaine', 'Tchad', 'Congo', 'Gabon', 'Guinée Équatoriale'],
    'EURO': ['France', 'Allemagne', 'Espagne', 'Italie', 'etc...'],
}

for org, pays in organisations.items():
    habitants_org = df[df['pays_residence'].isin(pays)].shape[0]
    print(f'Habitants dans {org}: {habitants_org}')

"""
def repartition_genre():
    genre_pays = df.groupby(['pays_residence', 'genre']).size().unstack().fillna(0)
    genre_ville = df.groupby(['ville_residence', 'genre']).size().unstack().fillna(0)

    print("Répartition par genre et pays:")
    print(genre_pays.to_string())
    print("\nRépartition par genre et ville:")
    print(genre_ville.to_string())

    genre_pays.plot(kind='bar', stacked=True, figsize=(10, 7))
    plt.title('Répartition par genre et pays')
    plt.show()

    genre_ville.plot(kind='bar', stacked=True, figsize=(10, 7))
    plt.title('Répartition par genre et ville')
    plt.show()


def genre_categorie_pro():
    genre_categorie = df.groupby(['genre', 'categorie_pro']).size().unstack().fillna(0)

    print("Répartition par genre et catégories socioprofessionnelles:")
    print(genre_categorie.to_string())

    genre_categorie.plot(kind='bar', stacked=True, figsize=(10, 7))
    plt.title('Répartition par genre et catégories socioprofessionnelles')
    plt.show()

def pays_categorie_pro():
    pays_categorie = df.groupby(['pays_residence', 'categorie_pro']).size().unstack().fillna(0)

    print("Répartition par pays et catégories socioprofessionnelles:")
    print(pays_categorie.to_string())

    pays_categorie.plot(kind='bar', stacked=True, figsize=(10, 7))
    plt.title('Répartition par pays et catégories socioprofessionnelles')
    plt.show()


def statistiques_migration():
    migration_stats = df.groupby(['ville_naissance', 'pays_residence']).size().unstack().fillna(0)

    print("Statistiques de migration (ville de naissance vers pays de résidence):")
    print(migration_stats.to_string())

    migration_stats.plot(kind='bar', stacked=True, figsize=(10, 7))
    plt.title('Statistiques de migration')
    plt.show()


def pyramide_ages():
    pyramide_ville = df.groupby(['ville_residence', 'age']).size().unstack().fillna(0)
    pyramide_pays = df.groupby(['pays_residence', 'age']).size().unstack().fillna(0)

    print("Pyramide des âges par ville:")
    print(pyramide_ville.to_string())
    print("\nPyramide des âges par pays:")
    print(pyramide_pays.to_string())

    pyramide_ville.plot(kind='bar', stacked=True, figsize=(10, 7))
    plt.title('Pyramide des âges par ville')
    plt.show()

    pyramide_pays.plot(kind='bar', stacked=True, figsize=(10, 7))
    plt.title('Pyramide des âges par pays')
    plt.show()


def pyramide_ages_genre():
    pyramide_age_genre = df.groupby(['age', 'genre']).size().unstack().fillna(0)

    print("Pyramide des âges par genre:")
    print(pyramide_age_genre.to_string())

    pyramide_age_genre.plot(kind='bar', stacked=True, figsize=(10, 7))
    plt.title('Pyramide des âges par genre')
    plt.show()


def naissance_residence():
    croisement = df.groupby(['pays_residence', 'pays_naissance', 'age']).size().unstack().fillna(0)

    print("Croisement entre pays de naissance et lieu de résidence (avec âges):")
    print(croisement.to_string())

    croisement.plot(kind='bar', stacked=True, figsize=(10, 7))
    plt.title('Croisement entre pays de naissance et lieu de résidence')
    plt.show()


def habitants_par_zone():
    habitants_pays = df['pays_residence'].value_counts()

    print("Habitants par pays:")
    print(habitants_pays.to_string())

    habitants_pays.plot(kind='bar', figsize=(10, 7))
    plt.title('Habitants par pays')
    plt.show()


def concentration_population():
    habitants_ville = df['ville_residence'].value_counts()

    print("Concentration de population par ville:")
    print(habitants_ville.to_string())

    habitants_ville.plot(kind='bar', figsize=(10, 7))
    plt.title('Concentration de population par ville')
    plt.show()


def concentration_sans_npi():
    sans_npi = df[df['npi'] == '0']
    habitants_sans_npi = sans_npi['ville_residence'].value_counts()

    print("Concentration de population par ville (sans NPI):")
    print(habitants_sans_npi.to_string())

    habitants_sans_npi.plot(kind='bar', figsize=(10, 7))
    plt.title('Concentration de population par ville (sans NPI)')
    plt.show()


def habitants_par_zone_geographique():
    zones = {
        'Amérique centrale': ['Belize', 'Costa Rica', 'El Salvador', 'Guatemala', 'Honduras', 'Nicaragua', 'Panama'],
        'Amérique du sud': ['Argentine', 'Bolivie', 'Brésil', 'Chili', 'Colombie', 'Équateur', 'Guyana', 'Paraguay',
                            'Pérou', 'Suriname', 'Uruguay', 'Venezuela'],
        'Amérique du nord': ['Canada', 'États-Unis', 'Mexique'],
        'Europe': ['France', 'Allemagne', 'Royaume-Uni', 'Espagne', 'Italie', 'etc...'],
        'Asie Pacifique': ['Australie', 'Nouvelle-Zélande', 'etc...'],
        'Moyen Orient Afrique du nord': ['Algérie', 'Égypte', 'etc...'],
        'Asie du sud est': ['Indonésie', 'Malaisie', 'Philippines', 'Singapour', 'Thaïlande', 'Vietnam'],
    }

    for zone, pays in zones.items():
        habitants_zone = df[df['pays_residence'].isin(pays)].shape[0]

def home(requests):
    return render(requests, "Base.html")


if __name__ == "__main__":
    habitants_par_zone()