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
#  Chap. 28     #  Gestion de fichiers : exercices                             #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", déroulez le programme dans votre
tête (cf. chap. 1).

Les corrigés sont dans le fichier corrs/corr_28_files.py.

Les fichiers utilisés par les exercices commencent tous par "exo28_". Ils sont
créés juste en dessous (section "Préparation") dans le répertoire courant, et
supprimés tout à la fin de ce fichier (section "Nettoyage"). Si vous créez
d'autres fichiers, ajoutez-les à la liste du nettoyage.
"""


#################
#  Préparation  #
#################

# Ne modifiez pas ce bloc : il crée les fichiers dont les exercices ont besoin.
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

"""
1. Ouvrez exo28_poeme.txt avec open() (sans "with"), affichez son contenu,
   puis fermez-le. Affichez ensuite l'attribut .closed du fichier.

2. Refaites la même chose avec un bloc "with". Pourquoi est-ce la façon
   recommandée d'ouvrir un fichier ?
"""


##################################
#  Modes d'ouverture de fichier  #
##################################

"""
3. Sans exécuter, pour chacun des modes "r", "w", "a" et "x", répondez :
       a) peut-on lire le fichier ?
       b) que se passe-t-il si le fichier n'existe pas ?
       c) que se passe-t-il si le fichier existe déjà (contenu conservé,
          effacé, erreur ?)

4. Ouvrez exo28_poeme.txt en mode "x". Quelle erreur obtenez-vous ?
   Protégez la ligne avec try: … except …: (cf. chap. 26).

5. Quel mode d'ouverture choisiriez-vous pour :
       a) un journal ("log") où l'on ajoute une ligne à chaque exécution ?
       b) un rapport recalculé entièrement à chaque exécution ?
       c) un fichier de configuration qu'on ne veut surtout pas écraser
          s'il existe déjà ?
"""


####################
#  Lecture simple  #
####################

"""
6. Sans exécuter, qu'affiche ce programme ?
       with open("exo28_poeme.txt", "r", encoding="utf-8") as fo:
           print(fo.read(6))
           print(fo.tell())
           print(fo.read(4))
           fo.seek(0)
           print(fo.read(2))

7. Lisez tout le contenu de exo28_poeme.txt dans une variable contenu.
   Affichez :
       a) le nombre de caractères du fichier,
       b) le nombre de lignes (avec .splitlines(), cf. chap. 8),
       c) le nombre de mots,
       d) le nombre de fois où la lettre "e" apparaît.
"""


###########################
#  Lecture ligne à ligne  #
###########################

"""
8. Affichez chaque ligne du poème précédée de son numéro, sous la forme :
       1: Le ciel est bleu
       2: La mer est calme
       …
   Attention aux sauts de ligne en trop !

9. Avec .readline() et une boucle "while", affichez uniquement les lignes
   qui commencent par "La".

10. Avec .readlines(), construisez la liste des lignes SANS les sauts de
    ligne, puis affichez la plus longue ligne du poème (cf. chap. 24 pour
    max() et key=).
"""


##############################
#  Écriture dans un fichier  #
##############################

"""
11. Créez le fichier exo28_carres.txt contenant les carrés des entiers de 1
    à 10, un par ligne. Relisez ensuite ce fichier et calculez la somme de
    ces carrés (n'oubliez pas de convertir chaque ligne avec int()).

12. Ajoutez (sans effacer le contenu !) la ligne "121" à la fin de
    exo28_carres.txt, puis vérifiez que le fichier a bien 11 lignes.

13. Sans exécuter, que retourne fo.write("Bonjour\n") ? Et que se passe-t-il
    avec fo.write(42) ? Vérifiez en protégeant la ligne avec try/except.

14. Écrivez la liste villes = ["Paris", "Lyon", "Marseille"] dans le fichier
    exo28_villes.txt, une ville par ligne, de deux façons :
        a) avec une boucle et .write(),
        b) avec .writelines() (que faut-il ajouter à chaque élément ?)
"""


######################################
#  Autres manipulations de fichiers  #
######################################

"""
15. Avec le module os :
        a) vérifiez que exo28_poeme.txt existe, et que exo28_absent.txt
           n'existe pas,
        b) affichez la taille en octets de exo28_poeme.txt (pourquoi est-elle
           différente du nombre de caractères ? Indice : "è"),
        c) renommez exo28_villes.txt en exo28_villes_fr.txt, puis vérifiez,
        d) supprimez exo28_villes_fr.txt, puis vérifiez.

16. Écrivez une fonction lire_si_existe(nom) qui retourne le contenu du
    fichier nom s'il existe, et None sinon. Écrivez-en deux versions :
        a) en testant d'abord avec os.path.exists() (style LBYL, chap. 26),
        b) avec try/except FileNotFoundError (style EAFP).
"""


##################
#  Fichiers CSV  #
##################

"""
17. Avec csv.reader, lisez exo28_notes.csv. Affichez la ligne d'en-tête, puis
    le nombre d'élèves.

18. Pour chaque élève, affichez son nom et sa moyenne arrondie à 2 décimales.
    Attention : csv.reader renvoie des strings !

19. Avec csv.DictReader, affichez le nom des élèves qui ont au moins 12 en
    maths.

20. Calculez la moyenne de la classe en physique.
"""


###########################
#  Écrire un fichier CSV  #
###########################

"""
21. Créez le fichier exo28_resultats.csv avec les colonnes nom, moyenne et
    admis (admis vaut "oui" si la moyenne est >= 10, "non" sinon), à l'aide
    de csv.DictWriter. Relisez-le pour vérifier son contenu.

22. Bonus (json, cf. chap. 28) : enregistrez le dictionnaire
        {"Alice": 14.67, "Bob": 9.33}
    dans le fichier exo28_moyennes.json, puis relisez-le et vérifiez que le
    dictionnaire relu est égal à l'original.
"""


###############
#  Nettoyage  #
###############

# On supprime tous les fichiers créés par ces exercices (s'ils existent).
import os

for nom in ["exo28_poeme.txt", "exo28_notes.csv", "exo28_carres.txt",
            "exo28_villes.txt", "exo28_villes_fr.txt", "exo28_resultats.csv",
            "exo28_moyennes.json"]:
    if os.path.exists(nom):
        os.remove(nom)
