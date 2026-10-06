################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.1.0        #
# ██   ██ ██                ██   ██    © Félix Déage - 2026                    #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 28     #  Gestion de fichiers : corrigés                              #
#               #                                                              #
################################################################################

import csv
import json
import os

#################
#  Préparation  #
#################

# Les mêmes fichiers que dans l'énoncé (ils sont supprimés à la fin).
with open("exo28_poeme.txt", "w", encoding="utf-8") as f:
    f.write("Le ciel est bleu\n")
    f.write("La mer est calme\n")
    f.write("Le vent se lève\n")
    f.write("Un bateau passe\n")
    f.write("La nuit tombe\n")

with open("exo28_notes.csv", "w", encoding="utf-8") as f:
    f.write("nom,maths,physique,francais\n")
    f.write("Alice,15,12,17\n")
    f.write("Bob,8,11,9\n")
    f.write("Chloé,12,14,10\n")
    f.write("David,6,9,11\n")


#################################
#  Ouvrir et fermer un fichier  #
#################################

# 1. Sans "with" :
fo = open("exo28_poeme.txt", "r", encoding="utf-8")
print(fo.read(), end="")  # end="" : le fichier se termine déjà par "\n"
# => Le ciel est bleu
# => La mer est calme
# => Le vent se lève
# => Un bateau passe
# => La nuit tombe
fo.close()
print(fo.closed)  # => True

# 2. Avec "with" :
with open("exo28_poeme.txt", "r", encoding="utf-8") as fo:
    print(fo.read(), end="")  # => (le même poème)
print(fo.closed)  # => True
"""
Avec "with", le fichier est fermé automatiquement à la sortie du bloc, MÊME si
une erreur se produit à l'intérieur. Sans "with", un oubli de .close() (ou une
erreur avant le .close()) laisse le fichier ouvert : les données écrites
peuvent ne pas être enregistrées, et le système limite le nombre de fichiers
ouverts en même temps.
"""


##################################
#  Modes d'ouverture de fichier  #
##################################

"""
3.  Mode | Lecture ? | Fichier absent        | Fichier existant
    -----+-----------+-----------------------+---------------------------------
    "r"  | oui       | FileNotFoundError     | contenu conservé (lecture seule)
    "w"  | non       | fichier créé          | contenu EFFACÉ (IMPT !)
    "a"  | non       | fichier créé          | contenu conservé, écriture à la
         |           |                       | fin du fichier
    "x"  | non       | fichier créé          | FileExistsError

    (On peut ajouter "+" pour pouvoir lire ET écrire : "r+", "w+", "a+".)
"""

# 4. Le mode "x" refuse d'ouvrir un fichier qui existe déjà :
try:
    fo = open("exo28_poeme.txt", "x")
except FileExistsError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 1: (Sans ce try: … except …, cette ligne créerait : [Errno 17] File exists:
#    'exo28_poeme.txt')

"""
5. a) "a" : on ajoute une ligne à la fin sans perdre l'historique.
   b) "w" : on repart d'un fichier vide à chaque fois.
   c) "x" : l'ouverture échoue si le fichier existe, il ne sera donc jamais
      écrasé par erreur.
"""


####################
#  Lecture simple  #
####################

# 6. La "tête de lecture" avance à chaque lecture :
with open("exo28_poeme.txt", "r", encoding="utf-8") as fo:
    print(fo.read(6))  # => Le cie (les 6 premiers caractères)
    print(fo.tell())   # => 6 (la tête de lecture est après le 6e caractère)
    print(fo.read(4))  # => l es (on reprend là où on s'était arrêté)
    fo.seek(0)         # on revient au début…
    print(fo.read(2))  # => Le

# 7. Statistiques sur le contenu :
with open("exo28_poeme.txt", "r", encoding="utf-8") as fo:
    contenu = fo.read()
print(len(contenu))               # => 80 (les 5 "\n" comptent !)
print(len(contenu.splitlines()))  # => 5
print(len(contenu.split()))       # => 18
print(contenu.count("e"))         # => 14
"""
- .split() sans argument coupe sur tout le whitespace (espaces ET sauts de
  ligne, cf. chap. 8) : c'est pratique pour compter les mots.
- .count("e") ne compte pas le "è" de "lève" : pour Python, ce sont deux
  caractères différents.
"""


###########################
#  Lecture ligne à ligne  #
###########################

# 8. Lignes numérotées : enumerate() (cf. chap. 24) et .rstrip("\n").
with open("exo28_poeme.txt", "r", encoding="utf-8") as fo:
    for numero, ligne in enumerate(fo, start=1):
        print(f"{numero}: {ligne.rstrip()}")
# => 1: Le ciel est bleu
# => 2: La mer est calme
# => 3: Le vent se lève
# => 4: Un bateau passe
# => 5: La nuit tombe
"""
Sans .rstrip(), chaque ligne contient déjà un "\n" et print() en ajoute un
autre : on aurait une ligne vide entre chaque vers.
"""

# 9. Avec .readline() : une ligne vide ("") signifie "fin du fichier".
with open("exo28_poeme.txt", "r", encoding="utf-8") as fo:
    ligne = fo.readline()
    while ligne:
        if ligne.startswith("La"):
            print(ligne, end="")
        ligne = fo.readline()
# => La mer est calme
# => La nuit tombe
"""
Attention : une ligne VIDE du fichier vaut "\n" (et non ""), elle est donc
évaluée à True : la boucle ne s'arrête qu'à la vraie fin du fichier.
"""

# 10. Liste des lignes sans "\n", puis la plus longue :
with open("exo28_poeme.txt", "r", encoding="utf-8") as fo:
    lignes = [ligne.rstrip("\n") for ligne in fo.readlines()]
print(lignes)
# => ['Le ciel est bleu', 'La mer est calme', 'Le vent se lève',
#     'Un bateau passe', 'La nuit tombe']
print(max(lignes, key=len))  # => Le ciel est bleu
"""
Les deux premières lignes ont la même longueur (16) : en cas d'égalité, max()
retourne le PREMIER élément maximal rencontré.
"""


##############################
#  Écriture dans un fichier  #
##############################

# 11. Écriture des carrés, puis relecture :
with open("exo28_carres.txt", "w", encoding="utf-8") as fo:
    for i in range(1, 11):
        fo.write(str(i ** 2) + "\n")  # .write() n'accepte que des strings

total = 0
with open("exo28_carres.txt", "r", encoding="utf-8") as fo:
    for ligne in fo:
        total += int(ligne)  # int() ignore le "\n" final
print(total)  # => 385

# 12. Ajout en mode "a" :
with open("exo28_carres.txt", "a", encoding="utf-8") as fo:
    fo.write("121\n")
with open("exo28_carres.txt", "r", encoding="utf-8") as fo:
    print(len(fo.readlines()))  # => 11
"""
En mode "w", on aurait effacé les 10 premières lignes : le fichier n'aurait
plus contenu que "121".
"""

# 13. .write() retourne le nombre de caractères écrits, et refuse les int :
with open("exo28_carres.txt", "a", encoding="utf-8") as fo:
    print(fo.write("Bonjour\n"))  # => 8 ("\n" compte pour un caractère)
    try:
        fo.write(42)
    except TypeError as err:
        print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 2: (Sans ce try: … except …, cette ligne créerait : write() argument must
#    be str, not int)

# 14. a) Avec une boucle :
villes = ["Paris", "Lyon", "Marseille"]
with open("exo28_villes.txt", "w", encoding="utf-8") as fo:
    for ville in villes:
        fo.write(ville + "\n")

# 14. b) Avec .writelines(), qui n'ajoute PAS de saut de ligne tout seul :
with open("exo28_villes.txt", "w", encoding="utf-8") as fo:
    fo.writelines([ville + "\n" for ville in villes])

with open("exo28_villes.txt", "r", encoding="utf-8") as fo:
    print(fo.read().splitlines())  # => ['Paris', 'Lyon', 'Marseille']
"""
Sans les "\n", .writelines(villes) écrirait "ParisLyonMarseille" sur une
seule ligne.
"""


######################################
#  Autres manipulations de fichiers  #
######################################

# 15. a) Existence :
print(os.path.exists("exo28_poeme.txt"))   # => True
print(os.path.exists("exo28_absent.txt"))  # => False

# 15. b) Taille en octets :
print(os.path.getsize("exo28_poeme.txt"))  # => 81
"""
Le fichier contient 80 caractères mais pèse 81 octets : en UTF-8, les lettres
non accentuées occupent 1 octet, mais "è" en occupe 2.
"""

# 15. c) Renommer :
os.rename("exo28_villes.txt", "exo28_villes_fr.txt")
print(os.path.exists("exo28_villes.txt"))     # => False
print(os.path.exists("exo28_villes_fr.txt"))  # => True

# 15. d) Supprimer (avec prudence : il n'y a pas de corbeille !) :
os.remove("exo28_villes_fr.txt")
print(os.path.exists("exo28_villes_fr.txt"))  # => False


# 16. a) Style LBYL ("Look Before You Leap") : on vérifie d'abord.
def lire_si_existe(nom):
    if not os.path.exists(nom):
        return None
    with open(nom, "r", encoding="utf-8") as fo:
        return fo.read()


print(lire_si_existe("exo28_absent.txt"))          # => None
print(len(lire_si_existe("exo28_poeme.txt")))      # => 80


# 16. b) Style EAFP ("Easier to Ask Forgiveness than Permission") : on essaie.
def lire_si_existe(nom):
    try:
        with open(nom, "r", encoding="utf-8") as fo:
            return fo.read()
    except FileNotFoundError:
        return None


print(lire_si_existe("exo28_absent.txt"))          # => None
print(len(lire_si_existe("exo28_poeme.txt")))      # => 80
"""
La version EAFP est souvent préférée en Python : entre le test exists() et
l'ouverture, un autre programme pourrait supprimer le fichier. Le try/except
couvre ce cas, pas le test préalable.
"""


##################
#  Fichiers CSV  #
##################

# 17. En-tête et nombre d'élèves :
with open("exo28_notes.csv", "r", encoding="utf-8", newline="") as fo:
    lignes = list(csv.reader(fo))
print(lignes[0])        # => ['nom', 'maths', 'physique', 'francais']
print(len(lignes) - 1)  # => 4 (on ne compte pas la ligne d'en-tête)

# 18. Moyenne de chaque élève (les valeurs sont des strings : int() !) :
for ligne in lignes[1:]:
    nom = ligne[0]
    notes = [int(note) for note in ligne[1:]]
    print(nom, round(sum(notes) / len(notes), 2))
# => Alice 14.67
# => Bob 9.33
# => Chloé 12.0
# => David 8.67

# 19. Avec DictReader, chaque ligne est un dictionnaire {colonne: valeur} :
with open("exo28_notes.csv", "r", encoding="utf-8", newline="") as fo:
    for eleve in csv.DictReader(fo):
        if int(eleve["maths"]) >= 12:
            print(eleve["nom"])
# => Alice
# => Chloé
"""
Avec DictReader, on accède aux colonnes par leur NOM (eleve["maths"]) plutôt
que par leur position (ligne[1]) : c'est plus lisible, et le code reste juste
si l'ordre des colonnes change.
"""

# 20. Moyenne de la classe en physique :
with open("exo28_notes.csv", "r", encoding="utf-8", newline="") as fo:
    notes_physique = [int(eleve["physique"]) for eleve in csv.DictReader(fo)]
print(sum(notes_physique) / len(notes_physique))  # => 11.5


###########################
#  Écrire un fichier CSV  #
###########################

# 21. On calcule les résultats, puis on les écrit avec DictWriter :
resultats = []
with open("exo28_notes.csv", "r", encoding="utf-8", newline="") as fo:
    for eleve in csv.DictReader(fo):
        notes = [int(eleve["maths"]), int(eleve["physique"]),
                 int(eleve["francais"])]
        moyenne = round(sum(notes) / len(notes), 2)
        admis = "oui" if moyenne >= 10 else "non"
        resultats.append({"nom": eleve["nom"], "moyenne": moyenne,
                          "admis": admis})

with open("exo28_resultats.csv", "w", encoding="utf-8", newline="") as fo:
    writer = csv.DictWriter(fo, fieldnames=["nom", "moyenne", "admis"])
    writer.writeheader()        # la ligne d'en-tête
    writer.writerows(resultats)  # toutes les lignes d'un coup

with open("exo28_resultats.csv", "r", encoding="utf-8") as fo:
    print(fo.read(), end="")
# => nom,moyenne,admis
# => Alice,14.67,oui
# => Bob,9.33,non
# => Chloé,12.0,oui
# => David,8.67,non
"""
DictWriter convertit lui-même les nombres en strings (14.67 → "14.67").
newline="" évite des lignes vides en trop sous Windows (cf. chap. 28).
"""

# 22. Bonus json : le dictionnaire est relu avec ses types (float, etc.).
moyennes = {"Alice": 14.67, "Bob": 9.33}
with open("exo28_moyennes.json", "w", encoding="utf-8") as fo:
    json.dump(moyennes, fo)
with open("exo28_moyennes.json", "r", encoding="utf-8") as fo:
    moyennes_relues = json.load(fo)
print(moyennes_relues)              # => {'Alice': 14.67, 'Bob': 9.33}
print(moyennes_relues == moyennes)  # => True


###############
#  Nettoyage  #
###############

for nom in ["exo28_poeme.txt", "exo28_notes.csv", "exo28_carres.txt",
            "exo28_villes.txt", "exo28_villes_fr.txt", "exo28_resultats.csv",
            "exo28_moyennes.json"]:
    if os.path.exists(nom):
        os.remove(nom)
