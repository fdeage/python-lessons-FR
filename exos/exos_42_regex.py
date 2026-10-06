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
#  Chap. 42     #  Expressions régulières : exercices                          #
#               #                                                              #
################################################################################

r"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", lisez le motif morceau par
morceau, de gauche à droite, avant de deviner le résultat.

N'oubliez pas : toutes les regex s'écrivent en chaîne brute, r"…".

Les corrigés sont dans le fichier corrs/corr_42_regex.py.
"""

import re


##################################
#  Chaînes brutes et recherches  #
##################################

r"""
1. Sans exécuter, que valent len("\t") et len(r"\t") ? Pourquoi faut-il
   écrire les regex en chaîne brute ?

2. Sans exécuter, que renvoient ces trois appels (un objet Match ou None) ?
       re.search(r"\d+", "Tome 3")
       re.match(r"\d+", "Tome 3")
       re.fullmatch(r"\d+", "Tome 3")

3. Écrivez une fonction contient_chiffre(texte) qui renvoie True si le texte
   contient au moins un chiffre, False sinon (avec re.search).
       contient_chiffre("R2D2")    => True
       contient_chiffre("Python")  => False

4. Avec re.search et les méthodes de l'objet Match, affichez le premier
   nombre trouvé dans "Température : 23 degrés, humidité : 60 %", puis sa
   position (début et fin).
"""


################################
#  Classes et quantificateurs  #
################################

r"""
5. Sans exécuter, que renvoient ces appels ?
       re.findall(r"[aeiou]", "regex")
       re.findall(r"\d{2}", "12345")
       re.findall(r"\w+", "Bonjour, l'été !")
       re.findall(r"[^a-z ]", "abc 123 déf")

6. Écrivez une fonction est_code_postal(texte) qui renvoie True si le texte
   est EXACTEMENT un code postal français de 5 chiffres.
       est_code_postal("75011")   => True
       est_code_postal("7501")    => False
       est_code_postal("75011 ")  => False

7. Écrivez une regex qui valide une plaque d'immatriculation française au
   format "AB-123-CD" (2 lettres majuscules, tiret, 3 chiffres, tiret,
   2 lettres majuscules). Testez-la sur "AB-123-CD", "ab-123-cd" et
   "AB-1234-CD".

8. Sans exécuter, que renvoient ces deux appels ? Expliquez la différence.
       re.findall(r"\(.+\)", "f(x) + g(y)")
       re.findall(r"\(.+?\)", "f(x) + g(y)")
"""


############################
#  findall et les groupes  #
############################

r"""
9. Extrayez tous les nombres (entiers ou décimaux avec un point, éventuellement
   négatifs) de la chaîne "Solde : -12.5 €, puis +30 €, puis 7.25 €", et
   calculez leur somme.

10. Avec un seul re.findall et des groupes, transformez
        "Ada:36, Alan:41, Grace:85"
    en la liste [('Ada', '36'), ('Alan', '41'), ('Grace', '85')], puis en un
    dictionnaire {'Ada': 36, 'Alan': 41, 'Grace': 85} (âges en int).

11. Avec des groupes NOMMÉS, analysez l'heure "14h05" et affichez le
    dictionnaire {'heures': '14', 'minutes': '05'} renvoyé par .groupdict().

12. Avec re.finditer, affichez chaque mot de plus de 6 lettres de la phrase
    "Les expressions régulières simplifient énormément le nettoyage"
    suivi de sa position de début.
"""


###################################
#  Alternance, \b et échappement  #
###################################

r"""
13. Trouvez tous les mots "le", "la" ou "les" ENTIERS (pas "lecture" ni
    "salade") dans : "Le chat mange la salade et les croquettes de lecture".
    (Pensez à re.IGNORECASE pour le "Le" majuscule.)

14. L'utilisateur cherche le texte "3.5" (une variable). Pourquoi
    re.findall(recherche, "3.5 ou 315") ne donne-t-il pas le bon résultat ?
    Corrigez avec re.escape.

15. Que se passe-t-il avec re.search(r"[0-9", "abc") ? Interceptez l'erreur
    avec un try/except (cf. chap. 26).
"""


#######################
#  sub, split, flags  #
#######################

r"""
16. Avec re.sub, remplacez toutes les suites d'espaces (y compris les
    tabulations) par un seul espace dans "trop    d'espaces\t\tici".

17. Avec re.sub et des références aux groupes, convertissez les dates
    "2024-03-15" (format ISO) en "15/03/2024" dans le texte
    "Du 2024-03-15 au 2024-04-02".

18. Découpez la chaîne "pommes ; poires,kiwis  ;fraises" en une liste de
    fruits sans espaces, avec un seul re.split.

19. Avec re.MULTILINE, récupérez la liste des noms de clés (avant le "=")
    de ce fichier de configuration :
        config = "hote=localhost\nport=8080\n# commentaire\nmode=debug"
    Les lignes de commentaire ne doivent pas être prises.

20. Réécrivez la regex de l'exercice 7 avec re.VERBOSE, un morceau par ligne,
    chacun avec un commentaire.
"""


########################
#  Cas pratiques data  #
########################

r"""
21. Écrivez une fonction prix_en_float(texte) qui convertit "12,50 €",
    "1 299,99 €" et "€ 8" en floats (12.5, 1299.99, 8.0), et renvoie None
    pour "gratuit".

22. Masquez les adresses emails d'un texte en ne gardant que la première
    lettre et le domaine :
        "Contact : alice.martin@exemple.fr ou bob@site.com"
    doit devenir
        "Contact : a***@exemple.fr ou b***@site.com"
    (Indice : un groupe pour la première lettre, un groupe pour le domaine.)

23. Voici des lignes de log :
        logs = '''2024-05-02 10:00:01 INFO démarrage
        2024-05-02 10:05:12 ERROR disque plein
        2024-05-02 10:06:00 WARNING mémoire basse
        2024-05-02 11:15:42 ERROR disque plein'''
    Avec une regex et un Counter (cf. chap. 43) — ou un dictionnaire —,
    comptez le nombre de lignes par niveau (INFO, ERROR, WARNING).

24. Écrivez une fonction est_telephone(texte) qui accepte les numéros de
    téléphone français "0612345678", "06 12 34 56 78", "06.12.34.56.78" et
    "+33 6 12 34 56 78", et refuse "0012345678" et "06 12 34 56". Testez-la
    avec des assert (cf. chap. 29).

25. Bonus (lookahead) : écrivez une regex qui valide un mot de passe d'au
    moins 10 caractères contenant au moins un chiffre, une minuscule et une
    majuscule.
"""
