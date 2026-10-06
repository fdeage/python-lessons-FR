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
#  Chap. 18     #  Dictionnaires I : exercices                                 #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour parcourir un dictionnaire, utilisez "for cle in dico" (les
méthodes .keys(), .values() et .items() seront vues au chap. 27).

Les corrigés sont dans le fichier corrs/corr_18_dicts_1.py.
"""


###########################################
#  Définition et utilité du dictionnaire  #
###########################################

"""
1. Créez un dictionnaire fiche représentant une personne, avec les clés
   "prenom", "nom" et "age".

2. Créez un dictionnaire vide stock.

3. Pour chacune de ces données, choisiriez-vous une liste ou un dictionnaire ?
       a) les notes successives d'un élève en mathématiques,
       b) le numéro de téléphone de chacun de vos contacts,
       c) la traduction anglaise de quelques mots français,
       d) les 10 meilleurs scores d'un jeu, dans l'ordre.
"""


#################################################
#  Indexation de valeurs et opérations de base  #
#################################################

"""
On pose : capitales = {"France": "Paris", "Italie": "Rome", "Japon": "Tokyo"}

4. Sans exécuter, que valent capitales["Italie"] et len(capitales) ?

5. Que se passe-t-il avec capitales["Espagne"] ? Vérifiez en protégeant la
   ligne avec try: … except KeyError: …

6. Sans exécuter, que vaut capitales[0] ? Pourquoi ?
"""


################################################
#  Ajouter, modifier et supprimer des valeurs  #
################################################

"""
7. Partez du dictionnaire stock = {"pommes": 10, "poires": 4}.
       a) ajoutez 6 kiwis,
       b) les pommes passent à 7,
       c) ajoutez 3 poires au stock existant,
       d) supprimez les kiwis,
   et affichez le dictionnaire après chaque étape.

8. Sans exécuter, que contient d à la fin ?
       d = {"a": 1, "b": 2}
       d["a"] = d["b"] + 10
       d["c"] = d["a"] * 2
       d["b"] = "deux"

9. Sans exécuter : combien d'éléments contient {"x": 1, "x": 2} ? Que vaut
   sa clé "x" ? Qu'en concluez-vous ?
"""


##################################
#  Tester la présence d'une clé  #
##################################

"""
10. Écrivez une fonction ajouter_contact(annuaire, nom, numero) qui ajoute le
    contact à l'annuaire, sauf si le nom y est déjà : dans ce cas, elle
    affiche "<nom> existe déjà" sans modifier l'annuaire.

11. Sans exécuter, que valent "Paris" in capitales et "France" in capitales ?
    Pourquoi ?
"""


###############################
#  Parcourir un dictionnaire  #
###############################

"""
On pose : notes = {"Alice": 15, "Bob": 9, "Chloé": 12, "David": 18}

12. Affichez chaque élève et sa note, sous la forme "Alice : 15/20".

13. Calculez la moyenne de la classe.

14. Trouvez l'élève qui a la meilleure note.

15. Construisez la liste des élèves qui ont la moyenne (note >= 10).

16. Construisez un nouveau dictionnaire appreciations, qui associe à chaque
    élève "Très bien" (>= 16), "Bien" (>= 12), "Passable" (>= 10) ou
    "Insuffisant".

17. Compter des lettres : écrivez une fonction compter_lettres(mot) qui
    retourne un dictionnaire associant chaque lettre à son nombre
    d'occurrences :
        compter_lettres("banane") => {'b': 1, 'a': 2, 'n': 2, 'e': 1}

18. Inverser un dictionnaire : à partir de {"un": 1, "deux": 2, "trois": 3},
    construisez {1: "un", 2: "deux", 3: "trois"}.

19. Traduction : avec le dictionnaire
        fr_en = {"le": "the", "chat": "cat", "mange": "eats", "poisson": "fish"}
    traduisez mot à mot la phrase "le chat mange le poisson". Les mots
    inconnus doivent être laissés tels quels.
"""

