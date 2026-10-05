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
#  - Préparation : créer le fichier d'exemple
#  - Ouvrir et fermer un fichier
#  - Modes d'ouverture de fichier
#  - Lecture simple
#  - Lecture ligne à ligne
#  - Écriture dans un fichier
#  - Autres manipulations de fichiers
#  - Fichiers CSV
#  - Requêtes
#  - Écrire un fichier CSV
#  - Nettoyage
#
#######################################

"""
Python est extrêmement pratique pour manipuler les fichiers et dossiers. Ce
chapitre vous propose quelques manipulations courantes.

Attention à ne pas modifier ou supprimer des fichiers par erreur, relisez-vous
bien et copiez votre travail avant dans un autre répertoire si besoin !

Ce fichier utilise les fichiers "exemple.txt" et "cinemas.csv". Pour qu'il
soit exécutable tel quel, il commence par les créer lui-même, puis les supprime
à la fin (cf. la dernière section "Nettoyage"). Il crée aussi quelques autres
fichiers temporaires ("nouveau.txt", etc.), qui sont eux aussi supprimés.

ATTENTION : si vous avez déjà, dans le répertoire où vous lancez ce programme,
des fichiers portant ces noms, ils seront écrasés puis supprimés !
"""

# Préparation : créer le fichier d'exemple
###########################################

"""
Pour pouvoir lire un fichier, il faut… qu'il existe. On crée donc ici le
fichier "exemple.txt", contenant 5 lignes de 4 lettres chacune.

Ne vous souciez pas encore de cette syntaxe : l'écriture dans un fichier est
expliquée en détail plus bas (section "Écriture dans un fichier"). Retenez
juste qu'après ces lignes, le fichier "exemple.txt" existe sur le disque, et
contient :
aaaa
bbbb
cccc
dddd
eeee

Note : "\n" est le caractère de saut de ligne (cf. chap. 7). Chaque ligne fait
donc 5 caractères : 4 lettres + 1 saut de ligne, soit 25 caractères en tout.
"""
with open("exemple.txt", "w", encoding="utf-8") as f:
    f.write("aaaa\nbbbb\ncccc\ndddd\neeee\n")


# Ouvrir et fermer un fichier
##############################

"""
La première étape pour lire un fichier est son ouverture : on utilise pour ceci
la fonction intégrée open(). Elle prend en paramètres :
    - le chemin du fichier (une string),
    - le mode d'ouverture (une string, "r" par défaut : voir plus loin).

IMPT : si on donne seulement le nom du fichier (sans chemin), Python le cherche
dans le RÉPERTOIRE COURANT, c'est-à-dire le répertoire depuis lequel on a lancé
Python (souvent, mais pas toujours, celui où se trouve le programme). Pour un
fichier situé ailleurs, on donne son chemin :
    - relatif : "donnees/exemple.txt", "../exemple.txt"
    - ou absolu : "/home/jeanmichel/exemple.txt" (Linux),
      "/Users/jeanmichel/exemple.txt" (macOS),
      "C:/Users/jeanmichel/exemple.txt" (Windows)
"""
fo = open("exemple.txt", "r")

"""
Attention : cette fonction ne retourne pas le contenu du fichier, mais un
objet qui permet d'y accéder (un "file object", d'où le nom "fo"). On peut le
voir comme une "poignée" sur le fichier.

En imprimant cet objet, on trouve en effet :
"""
print(fo)
# => <_io.TextIOWrapper name='exemple.txt' mode='r' encoding='UTF-8'>

"""
Cet objet donne un rappel des modalités d'ouverture du fichier :
    - son nom : exemple.txt
    - le mode d'ouverture (voir plus loin)
    - l'encodage du fichier, c'est-à-dire la façon dont les caractères sont
      traduits en octets sur le disque. Par défaut, c'est l'encodage du
      système : UTF-8 sur Linux et macOS, mais souvent autre chose (cp1252) sur
      Windows ! L'affichage ci-dessus peut donc varier selon votre machine.

Conseil : pour éviter les surprises avec les accents, précisez l'encodage avec
le paramètre encoding="utf-8" (comme on l'a fait pour créer le fichier).
"""

"""
Enfin, un fichier ouvert doit être fermé après son utilisation avec la méthode
.close() :
"""
fo.close()
print(fo.closed)  # => True (l'attribut .closed indique si le fichier est fermé)

"""
Si le fichier n'existe pas, open() en mode lecture soulève une erreur
FileNotFoundError (cf. chap. 26) :
"""
try:
    fo = open("ce_fichier_n_existe_pas.txt", "r")
except FileNotFoundError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Remarques :
    - Tous les fichiers laissés ouverts seront fermés d'office, à la fin de
      l'exécution du programme Python. Mais c'est une mauvaise habitude : un
      fichier ouvert consomme des ressources, et ce que l'on y écrit n'est
      parfois réellement enregistré sur le disque qu'à sa fermeture.
    - IMPT : il y a une syntaxe alternative à connaître pour ouvrir un fichier :
      with open(file, "r") as …:
"""
with open("exemple.txt", "r") as fo:
    print(fo)
    # => <_io.TextIOWrapper name='exemple.txt' mode='r' encoding='UTF-8'>

print(fo.closed)  # => True : le fichier a été fermé en sortant du "with"

"""
Cette syntaxe présente l'avantage de fermer automatiquement le fichier en
sortant du bloc "with", même si une erreur survient à l'intérieur du bloc.
Attention aux ":" et à l'indentation (comme pour "if", cf. chap. 12).

C'est la syntaxe recommandée : on l'utilisera le plus souvent possible.
"""


# Modes d'ouverture de fichier
###############################

"""
Python propose plusieurs modes d'ouverture, dont voici les principaux :
    - "r" (read) : mode lecture seule, le pointeur de lecture est placé en début
      de fichier. C'est le mode par défaut.
    - "w" (write) : mode écriture/remplacement. Écrase le fichier s'il existe,
      en crée un nouveau autrement. ATTENTION : l'ancien contenu est perdu dès
      l'ouverture, même si l'on n'écrit rien !
    - "a" (append) : mode ajout. Le pointeur est placé en fin de fichier,
      l'écriture n'écrase pas de données. Crée le fichier s'il n'existe pas.
    - "x" (exclusive) : mode création exclusive, possible seulement si le
      fichier n'existe pas

On peut ajouter à ces modes :
    - "+" : pour pouvoir à la fois lire et écrire ("r+", "w+", "a+")
    - "b" : pour ouvrir le fichier en mode binaire ("rb", "wb"…), c'est-à-dire
      lire des octets bruts plutôt que du texte (images, fichiers compressés…)
"""

# Ouverture en mode "append" : le contenu existant est conservé
fo2 = open("exemple.txt", "a")
fo2.close()

# Ouverture en mode "exclusive" sur un fichier qui n'existe pas : tout va bien
fo3 = open("nouveau_x.txt", "x")
fo3.close()

# Ouverture en mode "exclusive" sur un fichier qui existe déjà
try:
    fo3 = open("exemple.txt", "x")
    fo3.close()
except FileExistsError as err:
    # Une erreur est levée car le fichier existe déjà
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
À quoi sert le mode "x" ? À s'assurer qu'on n'écrase pas par erreur un fichier
existant, ce que ferait le mode "w" sans prévenir.

Note : on ne peut pas écrire dans un fichier ouvert en lecture seule (et
inversement) :
"""
with open("exemple.txt", "r") as fo:
    try:
        fo.write("zzzz")
    except Exception as err:
        # L'erreur est de type io.UnsupportedOperation
        print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")


# Lecture simple
#################

"""
La lecture d'un fichier fonctionne comme un magnétoscope : on ne peut lire
qu'à l'endroit courant. Autrement, il faut avancer la lecture, rembobiner, etc.

La "tête de lecture" est mise à jour au fil de la lecture du fichier.
"""

"""
Il y a plusieurs façons d'afficher le contenu d'un fichier.

    1. La première est d'utiliser la méthode .read() sur le fichier, avec en
       paramètre le nombre de caractères que l'on souhaite lire
"""
fo = open("exemple.txt", "r")
r = fo.read(4)
print(r)  # => aaaa

"""
Pour obtenir la position courante de la tête de lecture, on utilise .tell() :
on a lu 4 caractères, on est donc à la position 4.
"""
print(fo.tell())  # => 4

"""
Note : sans paramètre, la méthode .read() va lire jusqu'à la fin du fichier, à
partir de la position courante. Elle retourne une seule string contenant tout
le texte, sauts de ligne compris.

Rappel : on utilise end="" pour ne pas ajouter de saut de ligne à la fin
(cf. chap. 7), puisque le texte lu en contient déjà.
"""
print(fo.read(), end="")
# =>
#
# bbbb
# cccc
# dddd
# eeee

"""
Remarquez la ligne vide au début : la tête de lecture était placée juste après
"aaaa", donc AVANT le saut de ligne de la première ligne. C'est lui qui est
imprimé en premier !

On est maintenant à la fin du fichier (25 caractères) : un nouvel appel à
.read() retourne une chaîne vide.
"""
print(fo.tell())       # => 25
print(repr(fo.read()))  # => '' (repr() permet de "voir" la chaîne vide)

"""
Pour "rembobiner" la lecture, on utilise la méthode .seek(n) du file object,
avec en paramètre la position où l'on veut placer la tête de lecture.

Ceci est peu utilisé en pratique (on préfère souvent rouvrir le fichier).
"""
fo.seek(0)  # On remet la tête de lecture au début
print(fo.read(9))  # => aaaa
#                       bbbb
fo.close()

"""
L'usage le plus courant est de lire tout le fichier d'un coup dans une
variable, avec la syntaxe "with" :
"""
with open("exemple.txt", "r") as fo:
    contenu = fo.read()

print(type(contenu))  # => <class 'str'>
print(len(contenu))   # => 25

"""
contenu est une string comme une autre : on peut lui appliquer toutes les
méthodes vues aux chap. 7 et 8. Par exemple, .splitlines() découpe la chaîne
en une liste de lignes (sans les sauts de ligne) :
"""
print(contenu.splitlines())  # => ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee']


# Lecture ligne à ligne
########################

"""
Lire tout le fichier d'un coup est pratique, mais pose problème pour les très
gros fichiers (plusieurs Go…) qui ne tiennent pas en mémoire. On préfère alors
les lire ligne à ligne.

    2. Une deuxième façon est d'utiliser la méthode .readline() : elle lira
       automatiquement jusqu'à la fin de la ligne (càd jusqu'au prochain
       caractère de saut de ligne), saut de ligne compris.
"""
fo = open("exemple.txt", "r")
print(repr(fo.readline()))  # => 'aaaa\n'
print(repr(fo.readline()))  # => 'bbbb\n'
fo.seek(0)

"""
Arrivé à la fin du fichier, .readline() retourne la chaîne vide "". Or une
chaîne vide est évaluée à False (cf. chap. 21) : on peut donc l'utiliser comme
condition d'arrêt d'une boucle "while" (cf. chap. 13).
"""
line = fo.readline()  # On lit la première ligne…

# …puis on itère tant que line ne contient pas la chaîne vide (fin de fichier)
while line:
    print(line, end="")   # on imprime la ligne courante…
    line = fo.readline()  # …puis on lit la suivante
# => aaaa
#    bbbb
#    cccc
#    dddd
#    eeee

"""
Attention à l'ordre des deux instructions dans la boucle : si on lisait la
ligne suivante AVANT d'imprimer, la première ligne ne serait jamais affichée !

    3. La méthode .readlines() (avec un "s") lit toutes les lignes restantes
       et les retourne sous forme de LISTE de strings (une par ligne, sauts de
       ligne compris) :
"""
fo.seek(0)
lignes = fo.readlines()
print(lignes)  # => ['aaaa\n', 'bbbb\n', 'cccc\n', 'dddd\n', 'eeee\n']
print(len(lignes))  # => 5 (le nombre de lignes du fichier)

"""
On peut aussi passer un nombre n à .readlines(n). Attention, ce n'est PAS un
nombre de lignes, mais un nombre de caractères ("hint") : la méthode lit des
lignes entières jusqu'à ce que le total lu dépasse n caractères.

Ici, avec n = 7 : "aaaa\n" fait 5 caractères (< 7), donc la méthode continue et
lit aussi "bbbb\n" (total : 10 caractères, >= 7), puis s'arrête.
"""
fo.seek(0)
print(fo.readlines(7))  # => ['aaaa\n', 'bbbb\n']

"""
    4. La dernière façon est aussi ligne à ligne et n'utilise aucune méthode de
       fo : elle consiste à itérer sur le file object avec une boucle
       "for … in …". Un file object est en effet un itérable (cf. chap. 23) !

       La variable line contiendra successivement chaque ligne du fichier.

       IMPT : c'est la façon la plus simple et la plus efficace de parcourir un
       fichier ligne à ligne.
"""
fo.seek(0)  # On remet la tête de lecture au début

for line in fo:
    print(line, end="")
# => aaaa
#    bbbb
#    cccc
#    dddd
#    eeee

fo.close()

"""
Très souvent, on veut se débarrasser du saut de ligne en fin de chaque ligne :
on utilise pour cela .rstrip("\n") (ou .strip(), qui enlève aussi les espaces,
cf. chap. 8).

Exemple, avec "with", une boucle et une liste (la forme à retenir !) :
"""
lignes_propres = []
with open("exemple.txt", "r") as fo:
    for line in fo:
        lignes_propres.append(line.rstrip("\n"))

print(lignes_propres)  # => ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee']

# La même chose avec une compréhension de liste (cf. chap. 23) :
with open("exemple.txt", "r") as fo:
    lignes_propres = [line.rstrip("\n") for line in fo]

print(lignes_propres)  # => ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee']


# Écriture dans un fichier
###########################

# On commence par créer un nouveau fichier en mode écriture
nouveau_fichier_1 = open("nouveau.txt", "w")

# Pour écrire du texte dans ce fichier, on utilise la méthode .write()
w = nouveau_fichier_1.write("Hello")
print(w)  # => 5 (le nombre de caractères écrits)

# Les écritures dans le fichier sont successives
w = nouveau_fichier_1.write(", world!\n")
print(w)  # => 9 (le saut de ligne "\n" compte pour un caractère)
nouveau_fichier_1.close()

"""
IMPT : contrairement à print(), .write() n'ajoute PAS de saut de ligne à la
fin : il faut l'écrire soi-même avec "\n".

Vérifions le contenu du fichier :
"""
with open("nouveau.txt", "r") as fo:
    print(fo.read(), end="")  # => Hello, world!

"""
Le mode "a" (append) permet d'ajouter du texte à la fin d'un fichier existant,
sans effacer son contenu :
"""
with open("nouveau.txt", "a") as fo:
    fo.write("Une deuxième ligne\n")

with open("nouveau.txt", "r") as fo:
    print(fo.read(), end="")
# => Hello, world!
#    Une deuxième ligne

"""
Au contraire, rouvrir le fichier en mode "w" efface tout son contenu :
"""
with open("nouveau.txt", "w") as fo:
    fo.write("Tout a été remplacé !\n")

with open("nouveau.txt", "r") as fo:
    print(fo.read(), end="")  # => Tout a été remplacé !

"""
Pour écrire plusieurs lignes d'un coup, on peut utiliser .writelines(), qui
prend une liste de strings. Là encore, aucun saut de ligne n'est ajouté :
"""
fruits = ["pomme\n", "poire\n", "kiwi\n"]
with open("nouveau.txt", "a") as fo:
    fo.writelines(fruits)

"""
On peut aussi utiliser print() avec le paramètre file=… : print() écrit alors
dans le fichier au lieu de l'écran, avec ses avantages habituels (saut de ligne
automatique, conversion des nombres en texte, plusieurs valeurs séparées par un
espace…).
"""
with open("nouveau.txt", "a") as fo:
    print("Nombre de fruits :", len(fruits), file=fo)

with open("nouveau.txt", "r") as fo:
    print(fo.read(), end="")
# => Tout a été remplacé !
#    pomme
#    poire
#    kiwi
#    Nombre de fruits : 3

"""
Pour écrire le contenu d'une variable quelconque dans un fichier, on va
utiliser str() : .write() n'accepte que des strings.
"""
try:
    with open("nouveau.txt", "a") as fo:
        fo.write(42)
except TypeError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
HP : on dit que l'on va "sérialiser" la variable (c'est-à-dire la transformer
en chaîne de caractères).
"""
d = {"a": 123, "b": 217}
with open("nouveau_2.txt", "w") as nouveau_fichier:
    nouveau_fichier.write(str(d))  # écrit une string dans le fichier

# On lit ensuite dans le fichier pour s'assurer qu'il a bien le contenu de d
with open("nouveau_2.txt", "r") as file:
    contenu = file.read()
    print(contenu)  # => {'a': 123, 'b': 217}

"""
Attention : contenu est une STRING qui ressemble à un dictionnaire, ce n'est
pas un dictionnaire !
"""
print(type(contenu))  # => <class 'str'>

"""
HP : pour sauvegarder des données (listes, dictionnaires…) et les relire
ensuite sous leur vraie forme, on utilise plutôt le format JSON, avec le module
json (cf. chap. 22 pour les modules) :
    - json.dump(variable, fichier) écrit la variable dans le fichier
    - json.load(fichier) relit le fichier et reconstruit la variable
"""
import json

with open("nouveau.json", "w") as fo:
    json.dump(d, fo)

with open("nouveau.json", "r") as fo:
    d_relu = json.load(fo)

print(d_relu)        # => {'a': 123, 'b': 217}
print(type(d_relu))  # => <class 'dict'>
print(d_relu == d)   # => True


# Autres manipulations de fichiers
###################################

"""
Python propose beaucoup de fonctions pour manipuler les fichiers et dossiers.
Pour cela, nous allons importer le module "os" (cf. chap. 22), qui permet
d'accéder aux fonctions du système d'exploitation ("Operating System").
"""
import os

#   - Pour connaître le répertoire courant, on utilise getcwd() ("get current
#     working directory") :
print(os.getcwd())  # => /home/jeanmichel/python (dépend de votre machine)

#   - Pour afficher le contenu d'un répertoire, on utilise listdir(), avec en
#     paramètre le chemin du répertoire. Par exemple :
#       path = "/home/jeanmichel"   # => Sur Linux
#       path = "/Users/jeanmichel"  # => Sur macOS
#       path = "C:/Users/jeanmichel" # => Sur Windows
#     Ici, on utilise "." qui désigne le répertoire courant :
path = "."
fichiers = os.listdir(path)
print(fichiers)
# => ['chap_00_intro.py', 'exemple.txt', 'nouveau.txt', …] (l'ordre et le
#    contenu dépendent de votre répertoire)

#   - Pour savoir si un fichier ou un dossier existe, on utilise
#     os.path.exists() (très utile avant d'ouvrir un fichier !) :
print(os.path.exists("exemple.txt"))                 # => True
print(os.path.exists("ce_fichier_n_existe_pas.txt"))  # => False

#   - Pour connaître la taille d'un fichier (en octets) : os.path.getsize()
print(os.path.getsize("exemple.txt"))  # => 25

#   - Pour construire un chemin qui fonctionne sur tous les systèmes (avec "/"
#     sur Linux/macOS et "\" sur Windows), on utilise os.path.join() :
print(os.path.join("dossier", "sous_dossier", "fichier.txt"))
# => dossier/sous_dossier/fichier.txt (sur Linux ou macOS)

#   - Pour créer un dossier, on utilise mkdir(), et pour supprimer un dossier
#     VIDE, rmdir() :
os.mkdir("dossier_test")
print(os.path.isdir("dossier_test"))  # => True (c'est bien un dossier)
os.rmdir("dossier_test")
print(os.path.exists("dossier_test"))  # => False

#   - Pour renommer (ou déplacer) un fichier, on utilise rename() :
old_name = "nouveau_2.txt"
new_name = "nouveau_3.txt"
os.rename(old_name, new_name)
print(os.path.exists("nouveau_2.txt"))  # => False
print(os.path.exists("nouveau_3.txt"))  # => True

#   - Pour supprimer un fichier, on utilise remove().
#
# WARNING WARNING WARNING : utilisez remove() avec soin, ceci peut supprimer
# des fichiers sur votre ordinateur… et ils ne passent PAS par la corbeille !
# Ici, on supprime seulement des fichiers créés par ce programme :
os.remove("nouveau_3.txt")
print(os.path.exists("nouveau_3.txt"))  # => False

# Supprimer un fichier qui n'existe pas soulève une erreur :
try:
    os.remove("nouveau_3.txt")
except FileNotFoundError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")


# Fichiers CSV
###############

"""
Les fichiers CSV ("Comma-Separated Values") contiennent des tables de valeur en
format texte : chaque ligne du fichier est une ligne de la table, et les
valeurs ("colonnes") y sont séparées par un séparateur, le plus souvent une
virgule (parfois un point-virgule, notamment dans Excel en français).

Ce fichier peut contenir ou non une ligne d'en-tête ("headers"), contenant le
nom de chaque colonne. C'est le format d'échange de données le plus courant en
Data Science : presque tous les logiciels savent lire et écrire du CSV.

On commence par créer notre fichier "cinemas.csv" (comme pour exemple.txt) :
"""
with open("cinemas.csv", "w", encoding="utf-8") as f:
    f.write(
        "id,nom_cinema,ville,places,nb_salles\n"
        "c11a_26,Gaumont Bellecour,Lyon,200,6\n"
        "c11a_12,Louxor,Paris,420,3\n"
        "c11a_35,Grand Rex,Paris,600,7\n"
        "c11a_4,Mk2 Quai de Loire,Paris,320,4\n"
        "c11a_81,Pathé Wepler,Paris,500,14\n"
        "c11a_10,UGC George V,Paris,11,11\n"
    )
# (Rappel : plusieurs strings côte à côte sont automatiquement concaténées.)

"""
Il est courant que l'on veuille récupérer ces valeurs dans une structure de
données Python (par exemple dans une liste de dictionnaires).

On pourrait le faire "à la main" avec .split(",") sur chaque ligne (cf.
chap. 8), mais cela devient vite compliqué : que faire si une valeur contient
elle-même une virgule (par ex. "Paris, 18e") ?

On va plutôt importer le module csv, qui contient des fonctions très pratiques
pour manipuler les fichiers CSV.

Note : la documentation du module csv recommande d'ouvrir les fichiers CSV avec
le paramètre newline="", pour qu'il gère lui-même les sauts de ligne.
"""
import csv

cinemas_fo = open("cinemas.csv", "r", encoding="utf-8", newline="")

"""
1. On peut utiliser la fonction csv.reader() : celle-ci retourne un lecteur de
fichier (sur lequel on ira itérer plus loin).
"""
cinemas_r = csv.reader(cinemas_fo)

# (On note que csv.reader() retourne une référence à l'objet "lecteur de
# fichier")
print(type(cinemas_r))  # => <class '_csv.reader'>

# Il faudra ensuite itérer sur cinemas_r pour récupérer ses lignes
for line in cinemas_r:
    print(line)

"""
csv.reader() permet de convertir chaque ligne en une liste de strings :
['id', 'nom_cinema', 'ville', 'places', 'nb_salles']
['c11a_26', 'Gaumont Bellecour', 'Lyon', '200', '6']
['c11a_12', 'Louxor', 'Paris', '420', '3']
['c11a_35', 'Grand Rex', 'Paris', '600', '7']
['c11a_4', 'Mk2 Quai de Loire', 'Paris', '320', '4']
['c11a_81', 'Pathé Wepler', 'Paris', '500', '14']
['c11a_10', 'UGC George V', 'Paris', '11', '11']

Attention : toutes les valeurs sont des strings, même les nombres ('200') !
Un fichier CSV ne contient que du texte : c'est à nous de convertir les valeurs
(cf. chap. 6 et la section "Requêtes" plus bas).
"""

"""
2. Il existe aussi une fonction qui permet de convertir automatiquement chaque
ligne du fichier CSV original en un dictionnaire : csv.DictReader()
"""
cinemas_fo.seek(0)  # On rembobine la tête de lecture
cinemas_dr = csv.DictReader(cinemas_fo, delimiter=",")
"""
(Notez que si le fichier utilise des virgules comme séparateur, on n'est alors
pas obligé de préciser "delimiter=…". Pour un fichier séparé par des
points-virgules, on écrira delimiter=";".)
"""

# On itère ensuite sur cinemas_dr
cinemas = []
for c in cinemas_dr:
    cinemas.append(c)

# Magie : csv.DictReader() va associer tout seul la ligne d'en-tête avec chaque
# valeur pour en faire des dictionnaires !
print(cinemas)
"""
[{'id': 'c11a_26', 'nom_cinema': 'Gaumont Bellecour', 'ville': 'Lyon', 'places': '200', 'nb_salles': '6'}, {'id': 'c11a_12', 'nom_cinema': 'Louxor', 'ville': 'Paris', 'places': '420', 'nb_salles': '3'}, {'id': 'c11a_35', 'nom_cinema': 'Grand Rex', 'ville': 'Paris', 'places': '600', 'nb_salles': '7'}, {'id': 'c11a_4', 'nom_cinema': 'Mk2 Quai de Loire', 'ville': 'Paris', 'places': '320', 'nb_salles': '4'}, {'id': 'c11a_81', 'nom_cinema': 'Pathé Wepler', 'ville': 'Paris', 'places': '500', 'nb_salles': '14'}, {'id': 'c11a_10', 'nom_cinema': 'UGC George V', 'ville': 'Paris', 'places': '11', 'nb_salles': '11'}]

La ligne d'en-tête n'apparaît plus comme une ligne de données : elle sert
uniquement à nommer les clés.

Note : avant Python 3.8, csv.DictReader() retournait des "OrderedDict" au lieu
de simples dictionnaires (l'affichage est alors un peu différent).
"""

# On accède ensuite aux valeurs comme dans n'importe quel dictionnaire :
print(cinemas[2]["nom_cinema"])  # => Grand Rex

"""
On peut maintenant fermer le fichier .csv : nos données sont en lieu sûr dans
une liste de dictionnaires.
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

Pour cela, nous allons créer des "requêtes" en utilisant les compréhensions
(cf. chap. 23). Le mot "requête" vient des bases de données (langage SQL) :
c'est une instruction qui sélectionne et transforme des données.
"""
cinemas_2 = [
    {
        "id": c["id"].split("_")[1],  # "c11a_26" => ["c11a", "26"] => "26"
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
(l'affichage réel est sur une seule ligne)
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

"""
Comme les nombres sont maintenant de vrais ints, on peut aussi faire des
calculs sur toute la table, par exemple le nombre total de places :
"""
print(sum([c["places"] for c in cinemas_2]))  # => 2051


# Écrire un fichier CSV
########################

"""
Inversement, on peut sauvegarder le résultat d'une requête dans un nouveau
fichier CSV avec csv.DictWriter(). On lui indique :
    - le fichier dans lequel écrire,
    - la liste des noms de colonnes ("fieldnames"), dans l'ordre voulu.

Ensuite :
    - .writeheader() écrit la ligne d'en-tête,
    - .writerow(dico) écrit une ligne à partir d'un dictionnaire,
    - .writerows(liste) écrit une ligne par dictionnaire de la liste.

(Il existe aussi csv.writer(), qui écrit des listes plutôt que des
dictionnaires, avec les méthodes .writerow() et .writerows().)
"""
with open("cinemas_selection.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "nom"])
    writer.writeheader()
    writer.writerows(q)

# On relit le fichier pour vérifier son contenu
with open("cinemas_selection.csv", "r", encoding="utf-8") as f:
    print(f.read(), end="")
# => id,nom
#    26,Gaumont Bellecour
#    10,UGC George V

"""
Note : csv.writer() et csv.DictWriter() terminent chaque ligne par "\r\n" (la
convention des fichiers CSV, cf. RFC 4180). Les sauts de ligne sont donc un
peu différents de ceux de nos autres fichiers, mais cela ne se voit pas à
l'affichage.

Remarque : en Data Science, on utilisera souvent la bibliothèque pandas pour
lire et écrire des fichiers CSV en une seule ligne (cf. chap. xx).
"""


# Nettoyage
############

"""
Pour laisser votre répertoire propre, on supprime tous les fichiers créés par
ce chapitre. On utilise une boucle sur une liste de noms, et on vérifie que
chaque fichier existe avant de le supprimer.
"""
fichiers_crees = [
    "exemple.txt",
    "nouveau_x.txt",
    "nouveau.txt",
    "nouveau.json",
    "cinemas.csv",
    "cinemas_selection.csv",
]
for nom in fichiers_crees:
    if os.path.exists(nom):
        os.remove(nom)

print([nom for nom in fichiers_crees if os.path.exists(nom)])  # => []
