################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.1.0        #
# ██   ██ ██                ██   ██    © Claude Opus 5.5 - 2026                #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 41     #  Débogage : corrigés                                         #
#               #                                                              #
################################################################################

import traceback

#########################
#  Lire un traceback    #
#########################

"""
1. Voici un traceback :

       Traceback (most recent call last):
         File "/home/ada/rapport.py", line 18, in <module>
           afficher_rapport(ventes)
         File "/home/ada/rapport.py", line 12, in afficher_rapport
           print(f"Panier moyen : {panier_moyen(v):.2f}")
                                   ~~~~~~~~~~~~^^^
         File "/home/ada/rapport.py", line 5, in panier_moyen
           return v["total"] / v["nb_commandes"]
                  ~^^^^^^^^^
       KeyError: 'total'

   a) Quel est le type de l'erreur ? Que signifie le message ?
   b) Dans quel fichier, quelle fonction et à quelle ligne s'est-elle
      produite ?
   c) Dans quel ordre les fonctions ont-elles été appelées ?
   d) Formulez une hypothèse sur la cause du bug.
"""
"""
a) On lit la DERNIÈRE ligne : c'est une KeyError (cf. chap. 18). Le message
   'total' est la clé qui n'existe pas dans le dictionnaire.

b) Le dernier bloc "File" donne le lieu exact : fichier rapport.py, fonction
   panier_moyen(), ligne 5, sur l'instruction
   return v["total"] / v["nb_commandes"]. Les ^^^ soulignent v["total"].

c) On lit les blocs de haut en bas : le programme principal (<module>) a
   appelé afficher_rapport() à la ligne 18, qui a appelé panier_moyen() à la
   ligne 12. L'erreur s'est produite dans panier_moyen(), la fonction la plus
   récemment appelée ("most recent call last").

d) Le dictionnaire v n'a pas de clé "total". Hypothèses possibles : la clé
   s'appelle autrement (une faute de frappe, "Total" avec une majuscule…), ou
   certaines lignes de données n'ont pas de total. Pour vérifier, on affiche
   les clés juste avant la ligne 5 : print(v.keys()), ou p v.keys() dans pdb.
"""

"""
2. Le programme analyse.py contient, aux lignes 7 et 8 :

       villes = lire_villes("villes.csv").sort()
       print(villes[0])

   et produit ce traceback :

       Traceback (most recent call last):
         File "/home/ada/analyse.py", line 8, in <module>
           print(villes[0])
                 ~~~~~~^^^
       TypeError: 'NoneType' object is not subscriptable

   Que signifie le message ? La ligne 8 est-elle vraiment fautive ? Corrigez.
   (Indice : que renvoie la méthode .sort() ? cf. chap. 24)
"""
"""
"'NoneType' object is not subscriptable" signifie : on a utilisé des
crochets ([0]) sur une valeur qui vaut None. Les crochets ("subscript") ne
fonctionnent que sur les listes, tuples, strings, dictionnaires…

La ligne 8 est celle qui PLANTE, mais l'erreur vient de la ligne 7 :
.sort() trie la liste SUR PLACE et renvoie None (cf. chap. 24). villes vaut
donc None. Le traceback indique où le problème se MANIFESTE, pas forcément
où il est CAUSÉ : il faut parfois remonter quelques lignes plus haut.

Correction (on simule ici la fonction lire_villes) :
"""


def lire_villes(nom_fichier):
    return ["Nantes", "Brest", "Lyon"]


villes = lire_villes("villes.csv").sort()
print(villes)     # => None : voilà la cause

# Solution 1 : sorted() renvoie une nouvelle liste triée
villes = sorted(lire_villes("villes.csv"))
print(villes[0])  # => Brest

# Solution 2 : on trie sur place, sur une ligne séparée
villes = lire_villes("villes.csv")
villes.sort()
print(villes[0])  # => Brest

"""
3. Que signifient les messages d'erreur suivants ? Pour chacun, donnez une
   cause probable.
       a) NameError: name 'totl' is not defined
       b) TypeError: can only concatenate str (not "int") to str
       c) IndexError: list index out of range
       d) AttributeError: 'list' object has no attribute 'split'
       e) ValueError: invalid literal for int() with base 10: '12,5'
       f) TypeError: 'int' object is not callable
"""
"""
a) La variable totl n'existe pas : une faute de frappe (on voulait total),
   ou une variable utilisée avant d'être créée, ou créée dans une autre
   fonction (portée, cf. chap. 19). Python 3.10+ suggère souvent : "Did you
   mean: 'total'?".
b) On a fait "texte" + nombre. Il faut convertir le nombre avec str(), ou
   mieux utiliser une f-string (cf. chap. 8). Cause fréquente : on a oublié
   de convertir une saisie input() (cf. chap. 11).
c) On a demandé un indice qui n'existe pas : par exemple liste[3] sur une
   liste de 3 éléments (indices 0 à 2), ou un élément d'une liste vide.
   C'est souvent une erreur "off-by-one".
d) On a appelé une méthode de string (.split()) sur une liste : la variable
   ne contient pas ce que l'on croit. Affichez son type !
e) int() ne sait pas convertir "12,5" : la virgule n'est pas un séparateur
   décimal en Python, et de toute façon int() attend un entier. Il faut
   remplacer la virgule : float("12,5".replace(",", ".")).
f) On a mis des parenthèses après un entier, comme si c'était une fonction.
   Cause fréquente : on a écrasé une fonction intégrée avec une variable
   (sum = 0, max = 12…), cf. le cours.

On peut vérifier certaines de ces erreurs :
"""
try:
    int("12,5")
except ValueError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 1: (Sans ce try: … except …, cette ligne créerait : invalid literal for
# int() with base 10: '12,5')
print(float("12,5".replace(",", ".")))  # => 12.5

"""
4. Écrivez une fonction diviser(a, b) qui renvoie a / b. Appelez-la avec
   b = 0 dans un bloc try/except, et affichez :
       - seulement la dernière ligne du traceback (avec le module traceback),
       - la liste des noms de fonctions traversées (avec extract_tb).
"""


def diviser(a, b):
    return a / b


try:
    diviser(10, 0)
except ZeroDivisionError as err:
    print(traceback.format_exc().splitlines()[-1])
    # => ZeroDivisionError: division by zero
    print([cadre.name for cadre in traceback.extract_tb(err.__traceback__)])
    # => ['<module>', 'diviser']

"""
format_exc() renvoie tout le traceback sous forme de string ; splitlines()
le découpe en lignes, et [-1] garde la dernière. extract_tb() renvoie un
"cadre" par appel, du plus ancien (<module>, le programme principal) au plus
récent (diviser).
"""


###############################
#  Les trois familles de bugs #
###############################

"""
5. Pour chaque extrait, dites s'il contient une erreur de syntaxe, une
   erreur d'exécution ou une erreur de logique (sans exécuter) :

       a) prix = [12, 15, 9]
          print(prix[3])

       b) def aire_rectangle(longueur, largeur):
              return longueur + largeur

       c) for i in range(5)
              print(i)

       d) moyenne = sum([]) / len([])

       e) note = 15
          if note > 10:
              print("Recalé")
"""
"""
a) Erreur d'EXÉCUTION : IndexError, les indices vont de 0 à 2.
b) Erreur de LOGIQUE : la fonction tourne sans erreur, mais l'aire est
   longueur * largeur, pas longueur + largeur.
c) Erreur de SYNTAXE : il manque les deux-points après range(5). Python
   refuse de lancer le programme.
d) Erreur d'EXÉCUTION : ZeroDivisionError (0 / 0).
e) Erreur de LOGIQUE : 15 > 10 est vrai, on affiche "Recalé" au lieu de
   "Admis". Le programme ne signale rien.

Vérifions a), c) et d) :
"""
prix = [12, 15, 9]
try:
    print(prix[3])
except IndexError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 2: (Sans ce try: … except …, cette ligne créerait : list index out of
# range)

try:
    compile("for i in range(5)\n    print(i)", "<exemple>", "exec")
except SyntaxError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err.msg})")
# => 3: (Sans ce try: … except …, cette ligne créerait : expected ':')

try:
    moyenne = sum([]) / len([])
except ZeroDivisionError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 4: (Sans ce try: … except …, cette ligne créerait : division by zero)

"""
6. Pourquoi les erreurs de logique sont-elles les plus dangereuses ? Citez
   deux moyens de les détecter.
"""
"""
Parce que Python ne signale RIEN : le programme se termine normalement, et
le résultat faux peut passer inaperçu (et être utilisé pour prendre une
décision, publié dans un rapport…).

Moyens de les détecter :
    - écrire des tests avec des résultats connus à l'avance (cf. chap. 29 et
      37) : aire_rectangle(2, 3) doit valoir 6 ;
    - vérifier la vraisemblance des résultats (un pourcentage supérieur à
      100, une moyenne plus grande que la note maximale…), éventuellement
      avec des assert dans le code ;
    - faire relire son code (ou l'expliquer au canard en plastique !).
"""


##########################
#  Déboguer avec print() #
##########################

"""
7. Cette fonction doit calculer une moyenne pondérée (par exemple des notes
   avec des coefficients) : ((12 * 2) + (15 * 1)) / (2 + 1) = 13.0. Elle
   renvoie un mauvais résultat. Ajoutez des print(f"{…=}") pour trouver le
   bug, puis corrigez-le.

       def moyenne_ponderee(notes, coefs):
           total = 0
           for note, coef in zip(notes, coefs):
               total += note * coef
           return total / len(coefs)

       print(moyenne_ponderee([12, 15], [2, 1]))   # devrait afficher 13.0
"""


def moyenne_ponderee_debug(notes, coefs):
    total = 0
    for note, coef in zip(notes, coefs):
        total += note * coef
        print(f"  {note=} {coef=} {total=}")
    print(f"{total=} {len(coefs)=}")
    return total / len(coefs)


print(moyenne_ponderee_debug([12, 15], [2, 1]))
# =>   note=12 coef=2 total=24
# =>   note=15 coef=1 total=39
# => total=39 len(coefs)=2
# => 19.5

"""
Le total (39) est juste : 12 * 2 + 15 * 1. Mais on le divise par le NOMBRE
de coefficients (2) au lieu de leur SOMME (3). Correction :
"""


def moyenne_ponderee(notes, coefs):
    total = 0
    for note, coef in zip(notes, coefs):
        total += note * coef
    return total / sum(coefs)


print(moyenne_ponderee([12, 15], [2, 1]))  # => 13.0

"""
8. Ce programme devrait afficher "Ville trouvée", mais il affiche "Ville
   inconnue". Utilisez repr() pour comprendre pourquoi, puis corrigez.

       ligne = "Paris\n"          # une ligne lue dans un fichier (chap. 28)
       villes_connues = ["Lyon", "Paris", "Lille"]
       if ligne in villes_connues:
           print("Ville trouvée")
       else:
           print("Ville inconnue")
"""
ligne = "Paris\n"
villes_connues = ["Lyon", "Paris", "Lille"]
print(ligne)        # => Paris   (suivi d'une ligne vide : le \n est invisible)
print(repr(ligne))  # => 'Paris\n'
"""
repr() révèle le saut de ligne "\n" à la fin : "Paris\n" n'est pas égal à
"Paris". C'est un piège classique quand on lit un fichier ligne par ligne
(cf. chap. 28). Correction : enlever les espaces et sauts de ligne en début
et fin de chaîne avec .strip() (cf. chap. 7).
"""
if ligne.strip() in villes_connues:
    print("Ville trouvée")
else:
    print("Ville inconnue")
# => Ville trouvée

"""
9. Ce programme devrait afficher le prix le plus élevé (100), mais il
   affiche 9. Trouvez la cause en affichant les types, puis corrigez.

       prix = ["9", "100", "25"]     # lus dans un fichier CSV
       print(max(prix))
"""
prix = ["9", "100", "25"]
print(max(prix))                 # => 9
print([type(p) for p in prix])
# => [<class 'str'>, <class 'str'>, <class 'str'>]
"""
Les prix sont des STRINGS : max() les compare dans l'ordre alphabétique
(caractère par caractère, cf. chap. 9). "9" > "25" > "100", car "9" > "2" >
"1". Il faut convertir en nombres avant de comparer :
"""
print(max(float(p) for p in prix))     # => 100.0
print(max(prix, key=float))            # => 100  (garde la string d'origine,
#                                         mais compare les valeurs en float)


#############################
#  assert comme garde-fou   #
#############################

"""
10. Écrivez une fonction pourcentage(partie, total) qui renvoie le
    pourcentage partie / total * 100, arrondi à 1 décimale. Ajoutez deux
    assert avec un message clair : total doit être strictement positif, et
    partie doit être comprise entre 0 et total. Testez avec (3, 12), puis
    avec (15, 12) dans un try/except.
"""


def pourcentage(partie, total):
    assert total > 0, f"total doit être > 0 (reçu : {total})"
    assert 0 <= partie <= total, f"partie hors de [0, {total}] : {partie}"
    return round(partie / total * 100, 1)


print(pourcentage(3, 12))  # => 25.0
try:
    pourcentage(15, 12)
except AssertionError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 5: (Sans ce try: … except …, cette ligne créerait : partie hors de [0,
# 12] : 15)

"""
Sans ces assert, pourcentage(15, 12) renverrait 125.0 sans broncher : une
valeur absurde qui se propagerait dans la suite du programme.

11. Une fonction lit l'âge saisi par un utilisateur. Faut-il vérifier qu'il
    est positif avec un assert ou avec un raise ValueError ? Pourquoi ?
"""
"""
Avec raise ValueError (cf. chap. 26). Une saisie incorrecte n'est pas une
erreur de PROGRAMMATION : c'est une situation normale, qui arrivera
forcément, et que le programme doit traiter (afficher un message, redemander
la saisie…). De plus, les assert sont désactivés quand on lance Python avec
l'option -O : la vérification disparaîtrait !

assert est réservé aux conditions qui ne devraient JAMAIS être fausses si le
code est correct.
"""


def verifier_age(age):
    if age < 0:
        raise ValueError(f"Un âge ne peut pas être négatif : {age}")
    return age


try:
    verifier_age(-3)
except ValueError as err:
    print(f"6: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 6: (Sans ce try: … except …, cette ligne créerait : Un âge ne peut pas
# être négatif : -3)


###################################
#  Cas minimal et bisection       #
###################################

"""
12. Ce programme affiche un total faux (le total devrait être 45). Réduisez-le
    au plus petit programme possible qui montre encore le bug, puis
    expliquez le bug.

        import math
        donnees = {"lundi": "12", "mardi": "15", "mercredi": "18"}
        jours = list(donnees.keys())
        print("Nombre de jours :", len(jours))
        total = 0
        for jour in jours:
            valeur = donnees[jour]
            print("Traitement de", jour.upper())
            total = total + int(valeur) if jour != "mercredi" else total
        print("Racine du total :", math.sqrt(total))
        print("Total :", total)
"""
"""
On retire tout ce qui ne sert pas au calcul du total : l'import de math, les
affichages intermédiaires, la liste des jours (on peut parcourir le
dictionnaire directement). On vérifie à chaque étape que le bug est
toujours là (total = 27 au lieu de 45). On arrive à :
"""
donnees = {"lundi": "12", "mardi": "15", "mercredi": "18"}
total = 0
for jour in donnees:
    total = total + int(donnees[jour]) if jour != "mercredi" else total
print(total)  # => 27

"""
Le bug saute alors aux yeux : la condition "if jour != 'mercredi'" exclut le
mercredi du total (27 = 12 + 15). C'est une expression conditionnelle
(cf. chap. 12) écrite par erreur, ou un reste d'un ancien test. Correction :
"""
total = 0
for jour in donnees:
    total += int(donnees[jour])
print(total)  # => 45

"""
13. On cherche un bug par bisection dans un programme de 1000 lignes. À
    chaque étape, on divise la zone suspecte par deux.
    a) Combien d'étapes faut-il au maximum pour trouver la ligne fautive ?
    b) Et pour un programme de 1 000 000 de lignes ?
    c) Écrivez une petite boucle qui calcule ces deux nombres.
"""
"""
a) 10 étapes : 1000 → 500 → 250 → 125 → 63 → 32 → 16 → 8 → 4 → 2 → 1.
   (2 ** 10 = 1024 ≥ 1000)
b) 20 étapes seulement (2 ** 20 = 1 048 576 ≥ 1 000 000) : multiplier la
   taille du programme par 1000 n'ajoute que 10 étapes ! C'est la force de
   la dichotomie, que l'on étudiera au chap. 45.
c)
"""


def nb_etapes_bisection(nb_lignes):
    etapes = 0
    while nb_lignes > 1:
        nb_lignes = (nb_lignes + 1) // 2   # on garde la moitié (arrondie au
        etapes += 1                        # supérieur) qui contient le bug
    return etapes


print(nb_etapes_bisection(1000))       # => 10
print(nb_etapes_bisection(1_000_000))  # => 20


######################
#  Le débogueur pdb  #
######################

"""
14. Quelle commande pdb utiliser pour :
    a) afficher la valeur de la variable total ?
    b) exécuter la ligne courante sans entrer dans la fonction qu'elle
       appelle ?
    c) entrer dans la fonction appelée par la ligne courante ?
    d) reprendre l'exécution jusqu'au prochain point d'arrêt ?
    e) afficher la pile d'appels ?
    f) quitter ?
"""
"""
a) p total   (ou pp total pour un affichage joli ; ou simplement total)
b) n         ("next")
c) s         ("step")
d) c         ("continue")
e) w         ("where")
f) q         ("quit")
"""

"""
15. Voici une session pdb sur une fonction qui doit compter les mots de plus
    de 3 lettres. Quel est le bug ?

        > /home/ada/mots.py(4)compter_longs()
        -> breakpoint()
        (Pdb) l
          1     def compter_longs(mots):
          2         compte = 0
          3         for mot in mots:
          4  ->         breakpoint()
          5             if len(mot) > 3:
          6                 compte += 1
          7             return compte
        (Pdb) p mots
        ['chat', 'souris', 'ours']
        (Pdb) n
        > /home/ada/mots.py(5)compter_longs()
        -> if len(mot) > 3:
        (Pdb) n
        > /home/ada/mots.py(6)compter_longs()
        -> compte += 1
        (Pdb) n
        > /home/ada/mots.py(7)compter_longs()
        -> return compte
        (Pdb) n
        --Return--
        > /home/ada/mots.py(7)compter_longs()->1
        -> return compte
        (Pdb) p compte
        1
"""
"""
La session montre que la fonction renvoie (--Return--) dès le premier mot
('chat') : après "compte += 1", la ligne suivante est "return compte", alors
qu'il reste 'souris' et 'ours' à traiter. Le listing (commande l) montre
pourquoi : le return est indenté DANS la boucle for. La fonction s'arrête au
premier tour et renvoie 1 au lieu de 3.

Correction : désindenter le return pour le placer après la boucle.
"""


def compter_longs_faux(mots):
    compte = 0
    for mot in mots:
        if len(mot) > 3:
            compte += 1
        return compte


def compter_longs(mots):
    compte = 0
    for mot in mots:
        if len(mot) > 3:
            compte += 1
    return compte


mots = ["chat", "souris", "ours"]
print(compter_longs_faux(mots), compter_longs(mots))  # => 1 3

"""
16. a) Que fait la commande : PYTHONBREAKPOINT=0 python3 analyse.py ?
    b) Votre programme analyse.py plante sur une erreur. Quelle commande
       permet d'ouvrir pdb au moment du plantage, pour inspecter les
       variables ?
    c) Pourquoi ne faut-il jamais laisser un breakpoint() dans un programme
       que l'on livre ?
"""
"""
a) Elle lance analyse.py en ignorant tous les breakpoint() : le programme
   s'exécute d'une traite, sans jamais s'arrêter dans pdb.
b) python3 -m pdb analyse.py, puis c pour lancer l'exécution. Au moment de
   l'erreur, pdb s'arrête sur la ligne fautive (débogage "post-mortem"). Dans
   l'interpréteur interactif, juste après l'erreur : import pdb; pdb.pm().
c) Le programme se mettrait en pause chez l'utilisateur, en attendant des
   commandes pdb qu'il ne connaît pas. Pour un programme qui tourne sans
   surveillance (un script lancé chaque nuit, un serveur…), il resterait
   bloqué indéfiniment.
"""


###################################
#  Les bugs classiques            #
###################################

"""
17. Sans exécuter, qu'affiche ce programme ? Corrigez la fonction pour que
    chaque appel sans liste reparte d'une liste vide.

        def ajouter_ville(ville, liste=[]):
            liste.append(ville)
            return liste

        print(ajouter_ville("Lyon"))
        print(ajouter_ville("Nantes"))
        print(ajouter_ville("Brest", ["Rennes"]))
        print(ajouter_ville("Nice"))
"""


def ajouter_ville_faux(ville, liste=[]):
    liste.append(ville)
    return liste


print(ajouter_ville_faux("Lyon"))             # => ['Lyon']
print(ajouter_ville_faux("Nantes"))           # => ['Lyon', 'Nantes']
print(ajouter_ville_faux("Brest", ["Rennes"]))  # => ['Rennes', 'Brest']
print(ajouter_ville_faux("Nice"))             # => ['Lyon', 'Nantes', 'Nice']

"""
La liste par défaut est créée UNE SEULE FOIS, quand Python lit le "def". Tous
les appels sans 2e argument partagent cette même liste, qui grossit à chaque
appel. L'appel avec ["Rennes"] utilise une autre liste, et ne touche donc
pas à la liste par défaut. Correction : None par défaut, puis une nouvelle
liste à chaque appel.
"""


def ajouter_ville(ville, liste=None):
    if liste is None:
        liste = []
    liste.append(ville)
    return liste


print(ajouter_ville("Lyon"))    # => ['Lyon']
print(ajouter_ville("Nantes"))  # => ['Nantes']

"""
18. Ce code doit supprimer les mots vides (de longueur 0) d'une liste.
    Sans exécuter, qu'affiche-t-il ? Corrigez-le de deux façons.

        mots = ["le", "", "", "chat", "", "dort"]
        for mot in mots:
            if mot == "":
                mots.remove(mot)
        print(mots)
"""
mots = ["le", "", "", "chat", "", "dort"]
for mot in mots:
    if mot == "":
        mots.remove(mot)
print(mots)  # => ['le', 'chat', '', 'dort']

"""
Déroulons la boucle (la boucle avance d'un indice à chaque tour) :
    - indice 0 : "le", on garde.
    - indice 1 : "", on le supprime. La liste devient
      ["le", "", "chat", "", "dort"] : le 2e "" a glissé à l'indice 1…
    - indice 2 : "chat" (le "" de l'indice 1 a été sauté !), on garde.
    - indice 3 : "". Attention : .remove("") supprime la PREMIÈRE
      occurrence de "" dans la liste (celle de l'indice 1), pas celle que
      l'on est en train de regarder ! La liste devient
      ["le", "chat", "", "dort"].
    - indice 4 : hors de la liste, la boucle s'arrête.
Il reste un "" : on ne doit jamais modifier une liste pendant qu'on la
parcourt (cf. chap. 24).

Correction 1 : une compréhension de liste, qui crée une NOUVELLE liste.
"""
mots = ["le", "", "", "chat", "", "dort"]
mots = [mot for mot in mots if mot != ""]
print(mots)  # => ['le', 'chat', 'dort']

# Correction 2 : parcourir une COPIE de la liste, et supprimer dans
# l'originale.
mots = ["le", "", "", "chat", "", "dort"]
for mot in mots.copy():
    if mot == "":
        mots.remove(mot)
print(mots)  # => ['le', 'chat', 'dort']

"""
19. Cette fonction doit renvoyer la liste des températures de la semaine
    (les 7 dernières valeurs d'une liste). Trouvez l'erreur "off-by-one" et
    corrigez-la.

        def derniere_semaine(temperatures):
            return temperatures[len(temperatures) - 6:]

        print(derniere_semaine([10, 11, 12, 13, 14, 15, 16, 17, 18]))
        # devrait afficher [12, 13, 14, 15, 16, 17, 18]
"""


def derniere_semaine_faux(temperatures):
    return temperatures[len(temperatures) - 6:]


temperatures = [10, 11, 12, 13, 14, 15, 16, 17, 18]
print(derniere_semaine_faux(temperatures))  # => [13, 14, 15, 16, 17, 18]
print(len(derniere_semaine_faux(temperatures)))  # => 6

"""
Il manque une valeur : len - 6 = 3, et la slice [3:] contient les indices 3
à 8, soit 6 valeurs. Pour en avoir 7, il faut partir de len - 7. Plus
simple et plus lisible : les indices négatifs (cf. chap. 31).
"""


def derniere_semaine(temperatures):
    return temperatures[-7:]


print(derniere_semaine(temperatures))  # => [12, 13, 14, 15, 16, 17, 18]

"""
20. Sans exécuter, qu'affiche ce programme ? Corrigez-le.

        def appliquer_remise(prix, taux):
            nouveau_prix = prix * (1 - taux)

        prix_final = appliquer_remise(100, 0.2)
        print(prix_final)
"""


def appliquer_remise_faux(prix, taux):
    nouveau_prix = prix * (1 - taux)


print(appliquer_remise_faux(100, 0.2))  # => None

"""
La fonction calcule nouveau_prix, mais ne le RENVOIE pas : sans return, une
fonction renvoie None (cf. chap. 14). nouveau_prix est une variable locale,
perdue à la fin de la fonction (cf. chap. 19).
"""


def appliquer_remise(prix, taux):
    return prix * (1 - taux)


print(appliquer_remise(100, 0.2))  # => 80.0

"""
21. Ce programme plante à la dernière ligne. Pourquoi ? Corrigez-le.

        list = ["a", "b", "c"]
        print(len(list))
        lettres = list("abc")
"""
list = ["a", "b", "c"]
print(len(list))  # => 3
try:
    lettres = list("abc")
except TypeError as err:
    print(f"7: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 7: (Sans ce try: … except …, cette ligne créerait : 'list' object is not
# callable)
del list   # on supprime notre variable : list redevient la fonction intégrée

"""
La 1re ligne crée une variable nommée list, qui MASQUE la fonction intégrée
list() (cf. chap. 19). À la dernière ligne, list est donc notre liste
["a", "b", "c"], et on ne peut pas "appeler" une liste avec des
parenthèses. Correction : choisir un autre nom de variable.
"""
lettres_initiales = ["a", "b", "c"]
print(len(lettres_initiales))  # => 3
lettres = list("abc")
print(lettres)                 # => ['a', 'b', 'c']

"""
22. (Problème) Cette fonction analyse des ventes : elle doit renvoyer un
    dictionnaire avec le total des ventes, la meilleure vente et le nombre
    de ventes supérieures à 100 €. Elle contient TROIS bugs. Trouvez-les avec
    la méthode de votre choix (print, assert, débogueur…), corrigez-les,
    puis écrivez des assert qui vérifient le résultat attendu :
        {'total': 450.0, 'meilleure': 200.0, 'nb_grosses': 1}

        def analyser_ventes(ventes):
            total = 0
            meilleure = 0
            nb_grosses = 0
            for vente in ventes:
                montant = vente
                total = montant
                if montant > meilleure:
                    meilleure = montant
                if montant >= 100:
                    nb_grosses += 1
            return {"total": total, "meilleure": meilleure,
                    "nb_grosses": nb_grosses}

        print(analyser_ventes(["50", "200", "100", "100"]))
"""


def analyser_ventes_faux(ventes):
    total = 0
    meilleure = 0
    nb_grosses = 0
    for vente in ventes:
        montant = vente
        total = montant
        if montant > meilleure:
            meilleure = montant
        if montant >= 100:
            nb_grosses += 1
    return {"total": total, "meilleure": meilleure,
            "nb_grosses": nb_grosses}


ventes = ["50", "200", "100", "100"]
try:
    print(analyser_ventes_faux(ventes))
except TypeError as err:
    print(f"8: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 8: (Sans ce try: … except …, cette ligne créerait : '>' not supported
# between instances of 'str' and 'int')

"""
Bug n°1 (erreur d'exécution) : le traceback indique la ligne
"if montant > meilleure" : on compare une str ("50") à un int (0). Les
ventes sont des strings : il faut les convertir, montant = float(vente).

Une fois ce bug corrigé, le programme tourne… mais renvoie un résultat faux
(on peut le voir en ajoutant print(f"{montant=} {total=}") dans la boucle) :

Bug n°2 (logique) : "total = montant" écrase le total à chaque tour. Il faut
l'augmenter : total += montant.

Bug n°3 (logique) : "supérieures à 100 €" veut dire strictement plus de
100 ; avec >=, les deux ventes de 100 € sont comptées. Il faut écrire
montant > 100.
"""


def analyser_ventes(ventes):
    total = 0
    meilleure = 0
    nb_grosses = 0
    for vente in ventes:
        montant = float(vente)     # bug 1 : conversion
        total += montant           # bug 2 : += au lieu de =
        if montant > meilleure:
            meilleure = montant
        if montant > 100:          # bug 3 : > au lieu de >=
            nb_grosses += 1
    return {"total": total, "meilleure": meilleure,
            "nb_grosses": nb_grosses}


resultat = analyser_ventes(ventes)
print(resultat)  # => {'total': 450.0, 'meilleure': 200.0, 'nb_grosses': 1}

# Les assert, qui serviront de tests de non-régression (cf. chap. 29 et 37) :
assert resultat["total"] == 450.0, resultat
assert resultat["meilleure"] == 200.0, resultat
assert resultat["nb_grosses"] == 1, resultat
# Un cas limite : la liste vide.
assert analyser_ventes([]) == {"total": 0, "meilleure": 0, "nb_grosses": 0}
print("Tous les tests passent")  # => Tous les tests passent

"""
Remarque : avec des montants tous négatifs (des remboursements), meilleure
resterait à 0, ce qui est faux. Pour être robuste, on initialiserait
meilleure avec la première vente, ou on utiliserait max() (qui plante sur
une liste vide, cf. chap. 24 : à vous de choisir le comportement voulu).
"""
