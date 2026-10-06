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
#  Chap. 8      #  Manipuler les strings : corrigés                            #
#               #                                                              #
################################################################################

###########################################
#  Chercher et remplacer dans une chaîne  #
###########################################

# 1. "in" cherche une sous-chaîne, en respectant les majuscules :
print("ou" in "bonjour")     # => True ("bonj-OU-r")
print("Bon" in "bonjour")    # => False (le B majuscule n'y est pas)
print("x" not in "bonjour")  # => True

# 2. Les rangs commencent à 0 : b=0, a=1, n=2, a=3, n=4, e=5.
fruit = "banane"
print(fruit.find("an"))   # => 1 (première occurrence)
print(fruit.rfind("an"))  # => 3 (dernière occurrence)
print(fruit.find("z"))    # => -1 (absent)
print(fruit.count("an"))  # => 2
print(fruit.count("a"))   # => 2

# 3. Le 3e paramètre de .replace() limite le nombre de remplacements :
print("abracadabra".replace("a", "o"))     # => obrocodobro
print("abracadabra".replace("a", "o", 2))  # => obrocadabra

# 4. Remplacer les espaces par la chaîne vide revient à les supprimer :
print("06 12 34 56 78".replace(" ", ""))  # => 0612345678

# 5. .replace() ne modifie pas phrase (les chaînes sont immuables) : elle
#    RETOURNE une nouvelle chaîne, qui était perdue. Il faut la stocker :
phrase = "Il fait beau"
phrase = phrase.replace("beau", "froid")
print(phrase)  # => Il fait froid


#######################################
#  D'autres méthodes sur les strings  #
#######################################

# 6. a) .split("-") découpe à chaque tiret et renvoie une liste :
morceaux = "2026-10-05".split("-")
print(morceaux)  # => ['2026', '10', '05']
#    b) .join() recolle les morceaux, avec "/" entre chacun :
print("/".join(morceaux))  # => 2026/10/05
# (En une ligne, on aurait aussi pu écrire "2026-10-05".replace("-", "/").)

# 7. Sans paramètre, .split() coupe sur le whitespace et ignore les espaces
#    multiples ; avec " ", chaque espace compte, d'où la chaîne vide.
print("a b  c".split())             # => ['a', 'b', 'c']
print("a b  c".split(" "))          # => ['a', 'b', '', 'c']
print(",".join(["x", "y", "z"]))    # => x,y,z

# 8. On enchaîne les méthodes : chacune s'applique au RÉSULTAT de la
#    précédente. .strip() enlève les espaces autour, .title() met une
#    majuscule à chaque mot et le reste en minuscules.
saisie = "   aDa LOVElace  "
print(saisie.strip().title())  # => Ada Lovelace

# 9. .split() donne la liste des mots, len() compte ses éléments :
phrase = "Le chat dort sur le canapé"
print(len(phrase.split()))  # => 6

# 10. Le nom est complété à droite (ljust), la quantité à gauche (rjust) :
print("Pommes".ljust(10) + "3".rjust(4))
print("Kiwis".ljust(10) + "12".rjust(4))
print("Ananas".ljust(10) + "100".rjust(4))
# => Pommes       3
# => Kiwis       12
# => Ananas     100

# 11.
print("7".zfill(3))          # => 007
print("abc".center(7, "-"))  # => --abc--

# 12. On met tout en minuscules AVANT de compter :
print("Le loup et le chien".lower().count("le"))  # => 2
print("Le loup et le chien".count("le"))          # => 1 (sans .lower())
# Attention : .count() compte aussi "le" à l'intérieur des mots (dans
# "table", par exemple). Pour compter de vrais mots, on comparerait plutôt
# les éléments de .split() (cf. chap. 16 et 23).


####################################
#  Tester le contenu d'une chaîne  #
####################################

# 13.
print("2026".isdigit())                       # => True
print("20.5".isdigit())                       # => False (le point)
print("Bonjour".startswith("bon"))            # => False (majuscule !)
print("rapport.PDF".lower().endswith(".pdf"))  # => True

# 14. Deux vérifications séparées (on apprendra à les combiner avec "and"
#     au chap. 9, puis à réagir au résultat avec "if" au chap. 12) :
cp = "75011"
print(cp.isdigit(), len(cp) == 5)  # => True True
cp = "7501"
print(cp.isdigit(), len(cp) == 5)  # => True False (trop court)
cp = "75O11"
print(cp.isdigit(), len(cp) == 5)  # => False True (la lettre O !)


###########################
#  Interpoler une chaîne  #
###########################

# 15. Trois façons d'insérer des variables dans un texte :
prenom = "Ana"
age = 12
print(prenom + " a " + str(age) + " ans.")       # => Ana a 12 ans.
print("{} a {} ans.".format(prenom, age))        # => Ana a 12 ans.
print(f"{prenom} a {age} ans.")                  # => Ana a 12 ans.
# Seule la concaténation oblige à convertir age avec str().

# 16.
print(f"{2 + 3}")                    # => 5 (l'expression est calculée)
print(f"{'abc'.upper()}")            # => ABC
print(f"{{x}}")                      # => {x} (accolades doublées = littérales)
print("{1}-{0}".format("a", "b"))    # => b-a (on choisit l'ordre par indice)

# 17. Le "=" (Python 3.8+) affiche le nom de l'expression puis sa valeur :
prix = 9.99
print(f"{prix=}")  # => prix=9.99


##########################################
#  Formater des nombres dans une chaîne  #
##########################################

# 18.
print(f"{3.14159:.3f}")   # => 3.142 (arrondi à 3 décimales)
print(f"{42:05}")         # => 00042 (5 caractères, complétés par des zéros)
print(f"{0.075:.1%}")     # => 7.5% (multiplié par 100, avec 1 décimale)
print(f"{1500000:,}")     # => 1,500,000 (séparateur de milliers)

# 19. "<10" : à gauche sur 10 caractères ; ">7.2f" : à droite sur 7
#     caractères, avec 2 décimales.
pain = 1.2
fromage = 4.75
print(f"{'Pain':<10}{pain:>7.2f} €")
print(f"{'Fromage':<10}{fromage:>7.2f} €")
print(f"{'Total':<10}{pain + fromage:>7.2f} €")
# => Pain         1.20 €
# => Fromage      4.75 €
# => Total        5.95 €

# 20. "08b" : en binaire, sur 8 chiffres complétés par des zéros ; "x" : en
#     hexadécimal.
print(f"{200:08b}")  # => 11001000
print(f"{200:x}")    # => c8


######################################
#  Concaténation ou interpolation ?  #
######################################

# 21. Avec une f-string, plus de str() ni de "+" : le texte final se lit
#     directement.
n = 3
prix = 12.5
print(f"Total : {n} articles pour {prix} €")
# => Total : 3 articles pour 12.5 €

# 22. .format() est pratique quand le modèle est défini AVANT de connaître
#     les valeurs, et réutilisé plusieurs fois :
modele = "Bienvenue, {} ! Vous êtes le visiteur n°{}."
print(modele.format("Ana", 1))
print(modele.format("Omar", 2))
print(modele.format("Lou", 3))
# => Bienvenue, Ana ! Vous êtes le visiteur n°1.
# => Bienvenue, Omar ! Vous êtes le visiteur n°2.
# => Bienvenue, Lou ! Vous êtes le visiteur n°3.


################################################
#  Conversions de caractères : chr() et ord()  #
################################################

# 23.
print(ord("A"))            # => 65
print(chr(ord("A") + 2))   # => C (deux lettres plus loin)
print(chr(ord("e") - 32))  # => E (minuscules et majuscules sont décalées
#                                de 32 dans la table)

# 24. On travaille sur la POSITION de la lettre dans l'alphabet (0 à 25) :
lettre = "x"
position = ord(lettre) - ord("a")       # x est la lettre n°23
nouvelle_position = (position + 3) % 26  # 26 % 26 = 0 : on revient au début
print(chr(nouvelle_position + ord("a")))  # => a
"""
Sans le modulo, on obtiendrait chr(ord("x") + 3), c'est-à-dire "{", le
caractère qui suit "z" dans la table Unicode. Le % 26 fait "boucler"
l'alphabet : 23 + 3 = 26, et 26 % 26 = 0, la position de "a".

Pour chiffrer un mot entier, il faudra répéter ce calcul pour chaque lettre :
on le fera avec une boucle (cf. chap. 13).
"""


#####################
#  Chaînes longues  #
#####################

# 25. Une chaîne entre triples guillemets peut s'étendre sur plusieurs
#     lignes ; chaque passage à la ligne y est un "\n".
adresse = """Ada Lovelace
12 rue des Calculs
75000 Paris"""
print(adresse)
# => Ada Lovelace
# => 12 rue des Calculs
# => 75000 Paris
print(adresse.count("\n") + 1)  # => 3
# Il y a 2 sauts de ligne ENTRE 3 lignes, d'où le "+ 1".
