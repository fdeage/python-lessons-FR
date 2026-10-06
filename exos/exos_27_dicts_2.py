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
#  Chap. 27     #  Les dictionnaires (II) : exercices                          #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", déroulez le programme dans votre
tête (cf. chap. 1) avant de vérifier.

Les corrigés sont dans le fichier corr_27_dicts_2.py.
"""


#############################
#  Créer des dictionnaires  #
#############################

"""
1. Sans exécuter, que vaut chaque expression ?
       dict(nom="Ada", age=36)
       dict([("a", 1), ("b", 2), ("a", 3)])
       dict(zip("abc", [1, 2]))
       dict.fromkeys("xyz", False)
       {mot: len(mot) for mot in ["un", "deux", "trois"]}
       {n: n % 2 == 0 for n in range(4)}

2. On a deux listes :
       pays = ["France", "Japon", "Brésil"]
       capitales = ["Paris", "Tokyo", "Brasília"]
   Créez le dictionnaire {pays: capitale} de deux façons différentes : avec
   zip(), puis avec une compréhension.

3. Créez, avec une compréhension, un dictionnaire qui associe à chaque lettre
   de "python" son code (fonction ord(), cf. chap. 8).

4. Inversez le dictionnaire {"a": 1, "b": 2, "c": 3} (les valeurs deviennent
   les clés, et inversement) avec une compréhension. Que se passe-t-il si
   deux clés ont la même valeur, comme dans {"a": 1, "b": 1} ?
"""


#############################################
#  D'autres méthodes sur les dictionnaires  #
#############################################

"""
5. Sans exécuter, qu'affiche chaque print() ? Que vaut stock à la fin ?
       stock = {"pommes": 3, "poires": 0}
       print(stock.get("kiwis"))
       print(stock.get("kiwis", 0))
       print(stock.get("poires", 10))
       print(stock.pop("pommes"))
       print(stock.pop("kiwis", "absent"))
       print(stock.setdefault("poires", 5))
       print(stock.setdefault("cerises", 5))
       print(stock)

6. Sans exécuter, qu'affiche ce programme ?
       a = {"x": 1}
       b = a
       c = a.copy()
       b["x"] = 2
       c["y"] = 3
       print(a, b, c)

7. Des réglages par défaut et des réglages choisis par l'utilisateur :
       defaut = {"langue": "fr", "theme": "clair", "taille": 12}
       choix = {"theme": "sombre", "taille": 14}
   Construisez le dictionnaire des réglages finaux (les choix l'emportent sur
   les valeurs par défaut) SANS modifier defaut, de deux façons : avec .copy()
   puis .update(), et avec {**…, **…}.

8. Écrivez une fonction stock_restant(stock, produit) qui retourne la quantité
   d'un produit, ou 0 s'il n'est pas dans le stock, en une seule ligne.
"""


#################################################
#  Les méthodes .keys(), .values() et .items()  #
#################################################

"""
On considère les notes d'une classe :
    notes = {"Ana": 15, "Bob": 9, "Chloé": 17, "Djamel": 11}

9. Affichez :
       a) la liste des prénoms,
       b) la moyenne de la classe,
       c) la meilleure note,
       d) chaque élève avec sa note, au format "Ana : 15/20",
       e) les élèves dans l'ordre alphabétique inverse.

10. Construisez la liste des élèves qui ont la moyenne (note >= 10), puis le
    dictionnaire des élèves en échec avec leur note.

11. Sans exécuter, qu'affiche ce programme ? Pourquoi ?
        d = {"a": 1}
        cles = d.keys()
        d["b"] = 2
        print(list(cles))

12. On veut supprimer d'un dictionnaire de prix tous les produits à plus de
    5 €. Le programme suivant plante : pourquoi ? Corrigez-le.
        prix = {"pain": 1.2, "fromage": 7.5, "vin": 12.0, "lait": 0.9}
        for produit in prix:
            if prix[produit] > 5:
                del prix[produit]
"""


#######################################
#  Exemple : compter des occurrences  #
#######################################

"""
13. Écrivez une fonction compter_lettres(texte) qui retourne un dictionnaire
    {lettre: nombre d'apparitions}, en ignorant les espaces. Utilisez .get().
        compter_lettres("la lune")  → {'l': 2, 'a': 1, 'u': 1, 'n': 1, 'e': 1}

14. Trouvez la lettre la plus fréquente de "abracadabra" à l'aide de votre
    fonction et de max() avec le paramètre key.

15. Écrivez une fonction regrouper_par_initiale(mots) qui retourne un
    dictionnaire {initiale: liste des mots qui commencent par cette lettre}.
        regrouper_par_initiale(["pomme", "kiwi", "poire", "banane", "kaki"])
        → {'p': ['pomme', 'poire'], 'k': ['kiwi', 'kaki'], 'b': ['banane']}
    Indice : .setdefault() retourne la liste existante, ou crée une liste vide.
"""


#############################
#  Dictionnaires imbriqués  #
#############################

"""
On représente un petit carnet d'adresses :
    carnet = {
        "ana": {"tel": "0601020304", "ville": "Lyon", "age": 28},
        "bob": {"tel": "0611223344", "ville": "Paris", "age": 35},
        "chloe": {"tel": "0699887766", "ville": "Lyon", "age": 22},
    }

16. Sans exécuter, que valent carnet["bob"]["ville"] et
    len(carnet["ana"]) ? Que se passe-t-il avec carnet["djamel"]["tel"] ?

17. Bob déménage à Marseille : modifiez sa ville. Ajoutez ensuite un contact
    "djamel" (tel "0700000000", ville "Paris", age 41).

18. Affichez le prénom de tous les contacts qui habitent à Lyon, puis l'âge
    moyen des contacts.

19. Construisez un dictionnaire {ville: nombre de contacts} à partir du
    carnet.
"""


##############################################
#  Dictionnaires et paramètres de fonctions  #
##############################################

"""
20. Écrivez une fonction cadre(texte, options) qui affiche texte encadré.
    options est un dictionnaire facultatif pouvant contenir "bord" (caractère
    du cadre, "#" par défaut) et "marge" (nombre d'espaces de chaque côté du
    texte, 1 par défaut).
        cadre("Salut", {"bord": "*", "marge": 3})
        *************
        *   Salut   *
        *************
    La ligne du milieu est : bord + marge + texte + marge + bord, et les
    lignes du haut et du bas ont la même longueur. Testez aussi cadre("Salut")
    sans options (pensez à une valeur par défaut pour le paramètre options).

21. On a :
        def adresse(rue, ville, code_postal):
            return f"{rue}, {code_postal} {ville}"
        infos = {"ville": "Lyon", "rue": "3 rue Mercière",
                 "code_postal": "69002"}
    Appelez adresse() en lui passant infos avec "**". Pourquoi l'ordre des
    clés dans infos n'a-t-il pas d'importance ?

22. Écrivez une fonction creer_profil(nom, **infos) qui retourne un
    dictionnaire contenant le nom et toutes les informations optionnelles
    passées en arguments nommés.
        creer_profil("Ada", age=36, ville="Londres")
        → {'nom': 'Ada', 'age': 36, 'ville': 'Londres'}
"""
