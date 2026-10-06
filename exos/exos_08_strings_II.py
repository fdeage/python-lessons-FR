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
#  Chap. 8      #  Manipuler les strings : exercices                           #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les questions « sans exécuter », réfléchissez d'abord sur
papier, puis vérifiez avec l'interpréteur ou un print().

Les corrigés sont dans le fichier corrs/corr_08_strings_II.py.
"""


###########################################
#  Chercher et remplacer dans une chaîne  #
###########################################

"""
1. Sans exécuter : que valent
       a) "ou" in "bonjour"
       b) "Bon" in "bonjour"
       c) "x" not in "bonjour" ?

2. On pose : fruit = "banane"
   Sans exécuter, que valent fruit.find("an"), fruit.rfind("an"),
   fruit.find("z"), fruit.count("an") et fruit.count("a") ?

3. a) Remplacez tous les "a" de "abracadabra" par des "o".
   b) Puis remplacez seulement les DEUX premiers.

4. Un numéro de téléphone a été saisi avec des espaces : "06 12 34 56 78".
   Obtenez la chaîne "0612345678".

5. Ce programme devait afficher "Il fait froid". Pourquoi affiche-t-il
   "Il fait beau" ? Corrigez-le.
       phrase = "Il fait beau"
       phrase.replace("beau", "froid")
       print(phrase)
"""


#######################################
#  D'autres méthodes sur les strings  #
#######################################

"""
6. a) Découpez la date "2026-10-05" en ses trois morceaux.
   b) Puis reconstruisez la chaîne "2026/10/05" en combinant .split() et
      .join().

7. Sans exécuter : que valent
       a) "a b  c".split()
       b) "a b  c".split(" ")
       c) ",".join(["x", "y", "z"]) ?

8. Un nom a été saisi n'importe comment : "   aDa LOVElace  ".
   Obtenez "Ada Lovelace" (sans espaces autour, une majuscule à chaque mot).

9. Comptez le nombre de mots de la phrase "Le chat dort sur le canapé".
   Indice : .split() renvoie une liste, et len() fonctionne sur les listes.

10. Avec .ljust() et .rjust(), affichez ce tableau aligné (le nom sur 10
    caractères, la quantité sur 4) :
        Pommes       3
        Kiwis       12
        Ananas     100

11. Sans exécuter : que valent "7".zfill(3) et "abc".center(7, "-") ?

12. Combien de fois le mot "le" apparaît-il dans "Le loup et le chien", sans
    tenir compte des majuscules ?
"""


####################################
#  Tester le contenu d'une chaîne  #
####################################

"""
13. Sans exécuter : que valent
        a) "2026".isdigit()
        b) "20.5".isdigit()
        c) "Bonjour".startswith("bon")
        d) "rapport.PDF".lower().endswith(".pdf") ?

14. On pose : cp = "75011"
    Un code postal français s'écrit avec exactement 5 chiffres. Affichez deux
    booléens : l'un qui vérifie que cp ne contient que des chiffres, l'autre
    qui vérifie qu'il a la bonne longueur. Testez aussi avec "7501" et "75O11"
    (avec la lettre O).
"""


###########################
#  Interpoler une chaîne  #
###########################

"""
15. On pose : prenom = "Ana" et age = 12
    Affichez "Ana a 12 ans." de trois façons : par concaténation, avec
    .format() et avec une f-string.

16. Sans exécuter : que valent
        a) f"{2 + 3}"
        b) f"{'abc'.upper()}"
        c) f"{{x}}"
        d) "{1}-{0}".format("a", "b") ?

17. On pose : prix = 9.99
    Avec une f-string et le signe "=", affichez exactement : prix=9.99
"""


##########################################
#  Formater des nombres dans une chaîne  #
##########################################

"""
18. Sans exécuter : que valent
        a) f"{3.14159:.3f}"
        b) f"{42:05}"
        c) f"{0.075:.1%}"
        d) f"{1500000:,}" ?

19. Affichez ce ticket de caisse, en alignant les noms à gauche sur 10
    caractères et les prix à droite sur 7 caractères avec 2 décimales :
        Pain         1.20 €
        Fromage      4.75 €
        Total        5.95 €

20. Affichez le nombre 200 en binaire sur 8 chiffres, puis en hexadécimal
    (cf. chap. 6).
"""


######################################
#  Concaténation ou interpolation ?  #
######################################

"""
21. Réécrivez cette ligne avec une f-string, plus lisible :
        n = 3
        prix = 12.5
        print("Total : " + str(n) + " articles pour " + str(prix) + " €")

22. Créez un modèle "Bienvenue, {} ! Vous êtes le visiteur n°{}." et
    utilisez-le avec .format() pour afficher les messages de trois visiteurs :
    Ana (n°1), Omar (n°2) et Lou (n°3).
"""


################################################
#  Conversions de caractères : chr() et ord()  #
################################################

"""
23. Sans exécuter : que valent
        a) ord("A")
        b) chr(ord("A") + 2)
        c) chr(ord("e") - 32) ?

24. Chiffre de César : on décale une lettre minuscule de 3 rangs dans
    l'alphabet ("a" devient "d", "b" devient "e"…). Mais "x" doit devenir
    "a", et non "{" : l'alphabet "boucle" sur lui-même.
    Écrivez le calcul qui décale la lettre lettre = "x".
    Indice : calculez la position de la lettre dans l'alphabet (de 0 à 25),
    ajoutez 3, puis utilisez le modulo % (cf. chap. 4).
"""


#####################
#  Chaînes longues  #
#####################

"""
25. Créez une chaîne adresse de trois lignes avec des triples guillemets :
        Ada Lovelace
        12 rue des Calculs
        75000 Paris
    Affichez-la, puis affichez son nombre de lignes, en comptant les sauts de
    ligne avec .count().
"""
