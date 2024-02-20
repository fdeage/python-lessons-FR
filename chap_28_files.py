################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.0.9        #
# ██   ██ ██                ██   ██    © Félix Déage - 2024                    #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 28     #  Gestion de fichiers                                         #
#               #                                                              #
################################################################################
#
#  - Ouvrir et fermer un fichier
#  - Modes d'ouverture de fichier
#  - Lecture simple
#  - Lecture ligne à ligne
#  - Écriture dans un fichier
#  - Autres manipulations de fichiers
#  - Fichiers CSV
#
#######################################

"""
Python est extrêmement pratique pour manipuler les fichiers et dossiers. Ce
chapitre vous propose quelques manipulations courantes.

Attention à ne pas modifier ou supprimer des fichiers par erreur, relisez-vous
bien et copiez votre travail avant dans un autre répertoire si besoin !

Ce fichier appelle les fichiers "exemple.txt" et "cinemas.csv".
"""

# Ouvrir et fermer un fichier
##############################

"""
La première étape pour lire un fichier est son ouverture : on utilise pour ceci
la fonction intégrée open().

IMPT : le fichier ouvert doit être dans le même répertoire que le programme.
"""
fo = open("exemple.txt", "r")

"""
Attention : cette fonction ne retourne pas le contenu du fichier, mais un
pointeur vers son contenu ("file object").

En imprimant le contenu de ce pointeur, on trouve en effet :
"""
print(fo)  # <_io.TextIOWrapper name='exemple.txt' mode='r' encoding='UTF-8'>

"""
Ce pointeur donne un rappel des modalités d'ouverture du fichier :
    - son nom : exemple.txt
    - le mode d'ouverture (voir plus loin)
    - l'encodage du fichier (UTF-8 par défaut)
"""

"""
Enfin, un fichier ouvert doit être fermé après son utilisation avec la méthode
.close()
"""
fo.close()

"""
Remarques :
    - Tous les fichiers laissés ouverts seront fermés d'office, à la fin de
      l'exécution du programme Python.
    - Il y a une syntaxe alternative à connaître pour ouvrir un fichier :
      with open(file, "r") as …:
"""
with open("exemple.txt", "r") as fo:
    print(fo)  # <_io.TextIOWrapper name='exemple.txt' mode='r' encoding='UTF-8'>

"""
Cette syntaxe présente l'avantage de fermer automatiquement le fichier en
sortant de "with". Attention aux ":" et à l'indentation.
"""


# Modes d'ouverture de fichier
###############################

"""
Python propose plusieurs modes d'ouverture, dont voici les principaux :
    - "r" (read) : mode lecture seule, le pointeur de lecture est placé en début
      de fichier. C'est le mode par défaut.
    - "w" (write) : mode écriture/remplacement. Écrase le fichier s'il existe,
      en crée un nouveau autrement
    - "a" (append) : mode ajout. Le pointeur est placé en fin de fichier,
      l'écriture n'écrase pas de données
    - "x" (exclusive) : mode création exclusive, possible seulement si le
      fichier n'existe pas
"""

# Ouverture en mode "append"
fo2 = open("exemple.txt", "a")
fo2.close()

# Ouverture en mode "exclusive"
try:
    fo3 = open("exemple.txt", "x")
    fo3.close()
except FileExistsError as err:
    # Une erreur est levée car le fichier existe déjà
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")


# Lecture d'un fichier
#######################

"""
La lecture d'un fichier fonctionne comme un magnétoscope : on ne peut lire
qu'à l'endroit courant. Autrement, il faut avancer la lecture, rembobiner, etc.

La "tête de lecture" est mise à jour au fil de la lecture du fichier.
"""

"""
Il y a plusieurs façons d'afficher le contenu d'un fichier.

    1. La première est d'utiliser la méthode .read() sur le fichier, avec en
       paramètre le nombre d'octets que l'on souhaite lire
"""
fo = open("exemple.txt", "r")
r = fo.read(4)

# Rappel : on utilise end='' pour ne pas ajouter de saut de ligne à la fin
print(r, end="")  # => "aaaa"

#      Note : sans paramètre à .read(), la méthode va lire jusqu'à la fin du
#      fichier
print(fo.read())  # => "bbb…"

"""
Note :
    - Pour obtenir la position courante de la lecture, on utilise .tell()
    - Pour "rembobiner" la lecture, on utilise la méthode .seek(n) du file
      object, avec en paramètre la position de la tête de lecture

Ceci est peu utilisé en pratique.
"""
print(fo.tell())  # => 5
fo.seek(0)  # On remet la tête de lecture au début


"""
    2. Une deuxième façon est d'utiliser la méthode .readline() : elle lira
       automatiquement jusqu'à la fin de la ligne (càd jusqu'au prochain
       caractère de saut de ligne)
"""
line = fo.readline()  # On lit la première ligne…

# …puis on itère tant que line ne contient pas la ligne vide (fin de fichier)
while line:
    line = fo.readline()
    print(line, end="")

# On peut décider de retourner un nombre n de lignes avec la méthode
# .readlines(n)
# TODO : readlines
fo.readlines(3)  # => retourne 3 lignes

"""
    3. La dernière façon est aussi ligne à ligne et n'utilise aucune méthode de
       fo : elle consiste à itérer sur le contenu du fichier avec une boucle
       "for … in …".

       La variable line contiendra successivement chaque ligne du fichier.
"""
fo.seek(0)  # On remet la tête de lecture au début

for line in fo:
    print(line, end="")

fo.close()


# Écriture dans un fichier
###########################

# On commence par créer un nouveau fichier en mode écriture
nouveau_fichier_1 = open("nouveau.txt", "w")

# Pour écrire du texte dans ce fichier, on utilise la méthode .write()
w = nouveau_fichier_1.write("Hello")
print(w)  # => 5 (le nombre d'octets écrits)

# Les écritures dans le fichier sont successives
w = nouveau_fichier_1.write(", world!\n")
print(w)  # => 7
nouveau_fichier_1.close()

# Pour écrire le contenu d'une variable quelconque dans un fichier, on va
# utiliser str().
# HP : on dit que l'on va "sérialiser" la variable (c'est-à-dire la transformer
# en chaîne de caractères).
d = {"a": 123, "b": 217}
with open("nouveau_2.txt", "w") as nouveau_fichier:
    nouveau_fichier.write(str(d))  # writes a string to a file

# On lit ensuite dans le fichier pour s'assurer qu'il a bien le contenu de d
with open("nouveau_2.txt", "r") as file:
    contenu = file.read()
    print(contenu)  # => {"a": 123, "b": 217}


# Autres manipulations de fichiers
###################################

"""
Python propose beaucoup de fonctions pour manipuler les fichiers et dossiers.
Pour cela, nous allons importer le module "os".
"""
import os

#   - Pour afficher le contenu d'un répertoire, on utilise listdir() :

# path = "/home/jeanmichel"   # => Sur Linux
path = "/Users/fd"  # => Sur macOS
# path = "C://Documents"      # => Sur Windows

fichiers = os.listdir(path)
print(fichiers)  # => ['.config', 'Music', 'Movies', 'Documents', …]

#   - Pour renommer un fichier, on utilise rename() :

path = "/usr/someone/python"

old_name = "nouveau_2.txt"
new_name = "nouveau_3.txt"
os.rename(old_name, new_name)

#   - Pour supprier un fichier, on utilise remove() :

# WARNING WARNING WARNING - à décommenter avec soin : ceci peut supprimer des
# fichiers sur votre ordinateur…
# os.remove("nouveau.txt")
# os.remove("nouveau_3.txt")


# Fichiers CSV
###############

"""
Les fichiers CSV ("Comma-Separated Values") contiennent des tables de valeur en
format texte.

Ce fichier peut contenir ou non une ligne d'en-tête ("headers"), contenant

Il est courant que l'on veuille récupérer ces valeurs dans une structure de
données Python (par exemple dans une liste de dictionnaires).

On va pour cela importer le module csv, qui contient des fonctions très
pratiques pour manipuler les fichiers CSV.
"""
import csv

cinemas_fo = open("cinemas.csv", "r")

"""
1. On peut utilise la méthode .reader() : celle-ci retourne un lecteur de
fichier (sur lequel on ira itérer plus loin).
"""
cinemas_r = csv.reader(cinemas_fo)

# (On note que .reader() retourne une référence à l'objet "lecteur de fichier")
print(type(cinemas_r))  # => <class '_csv.reader'>

# Il faudra ensuite itérer sur cinemas_r pour récupérer ses lignes
for line in cinemas_r:
    print(line)

"""
.reader() permet de convertir chaque ligne en un liste de strings :
['id', 'nom_cinema', 'ville', 'places', 'nb_salles']
['c11a_26', 'Gaumont Bellecour', 'Lyon', '200', '6']
['c11a_12', 'Louxor', 'Paris', '420', '3']
['c11a_35', 'Grand Rex', 'Paris', '600', '7']
['c11a_4', 'Mk2 Quai de Loire', 'Paris', '320', '4']
['c11a_81', 'Pathé Wepler', 'Paris', '500', '14']
['c11a_10', 'UGC George V', 'Paris', '11', '11']
[]    -> ligne vide de la fin du fichier
"""

"""
2. Il existe aussi une méthode qui permet de convertir automatiquement chaque
ligne du fichier CSV original en un dictionnaire : .DictReader()
"""
cinemas_fo.seek(0)  # On rembobine la tête de lecture
cinemas_dr = csv.DictReader(cinemas_fo, delimiter=",")
"""
(Notez que si le fichier utilise des virgules comme séparateur, on n'est alors
pas obligé de préciser "delimiter=…")
"""

# On itère ensuite sur cinemas_dr
cinemas = []
for c in cinemas_dr:
    cinemas.append(c)

# Magie : .DictReader() va associer tout seul la ligne d'en-tête avec chaque
# valeur pour en faire des dictionnaires !
print(cinemas)
"""
[{'id': 'c11a_26', 'nom_cinema': 'Gaumont Bellecour', 'ville': 'Lyon', 'places': '200', 'nb_salles': '6'}, {'id': 'c11a_12', 'nom_cinema': 'Louxor', 'ville': 'Paris', 'places': '420', 'nb_salles': '3'}, {'id': 'c11a_35', 'nom_cinema': 'Grand Rex', 'ville': 'Paris', 'places': '600', 'nb_salles': '7'}, {'id': 'c11a_4', 'nom_cinema': 'Mk2 Quai de Loire', 'ville': 'Paris', 'places': '320', 'nb_salles': '4'}, {'id': 'c11a_81', 'nom_cinema': 'Pathé Wepler', 'ville': 'Paris', 'places': '500', 'nb_salles': '14'}, {'id': 'c11a_10', 'nom_cinema': 'UGC George V', 'ville': 'Paris', 'places': '11', 'nb_salles': '11'}]
"""

"""
On peut maintenant fermer le fichier .csv : nos données sont en lieu sûr dans un
dictionnaire.
"""
cinemas_fo.close()


# Requêtes
###########

"""
Il y a cependant des modifications que l'on souhaite apporter à cette liste :
    1. les dernières colonnes de la table ("nb_salles" et "places") contiennent
       des nombres, mais ils sont représentés sous forme de strings
    2. à chaque ligne, on souhaite enlever la première partie de l'id ("c11a_")
    3. la ville du cinéma ne nous intéresse plus
    4. on veut renommer le champ "nom_cinema" en "nom"
    5. on veut renommer le champ "nb_salles" en "salles"

Pour cela, nous allons créer des "requêtes" en utilisant les compréhensions.
"""
cinemas_2 = [
    {
        "id": c["id"].split("_")[1],
        "nom": c["nom_cinema"],
        "salles": int(c["nb_salles"]),
        "places": int(c["places"])
    }
    for c in cinemas
]
print(cinemas_2)
"""
=> le retraitement a bien fonctionné :
[
    {'id': '26', 'nom': 'Gaumont Bellecour', 'salles': 6, 'places': 200},
    {'id': '12', 'nom': 'Louxor', 'salles': 3, 'places': 420},
    {'id': '35', 'nom': 'Grand Rex', 'salles': 7, 'places': 600},
    {'id': '4', 'nom': 'Mk2 Quai de Loire', 'salles': 4, 'places': 320},
    {'id': '81', 'nom': 'Pathé Wepler', 'salles': 14, 'places': 500},
    {'id': '10', 'nom': 'UGC George V', 'salles': 11, 'places': 11}
]
"""

"""
On peut aussi utiliser les requêtes pour appliquer des conditions : ainsi, on
ne souhaite garder que l'id et le nom des cinémas :
    - ayant un id pair
    - ayant plus de 4 salles
    - ayant une capacité < 500 personnes
"""
q = [
    {"id": c["id"], "nom": c["nom"]}
    for c in cinemas_2
    if int(c["id"]) % 2 == 0 and c["salles"] > 4 and c["places"] < 500
]
print(q)  # => [{'id': '26', 'nom': 'Gaumont Bellecour'}, {'id': '10', 'nom': 'UGC George V'}]
