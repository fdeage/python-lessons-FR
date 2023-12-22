################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.0.9        #
# ██   ██ ██                ██   ██    © Félix Déage - 2023                    #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 8      #  Manipuler des strings                                       #
#               #                                                              #
################################################################################
#
#  - Chercher et remplacer dans une chaîne
#  - D'autres méthodes sur les strings
#  - Interpoler une chaîne
#  - Conversions de caractères : chr() et ord()
#  - Chaînes longues
#
####################################################

# Chercher et remplacer dans une chaîne
########################################

"""
    1. "in" et "not in" permettent de tester si une sous-chaîne figure dans une
       chaîne
"""
"ab" in "abcd"     # => True
"ab" in "def"      # => False
"ab" not in "def"  # => True


"""
    2. La méthode .find() renvoie le rang auquel la sous-chaîne a été trouvée
       (et -1 si la sous-chaîne ne figure pas dans la chaîne)
"""
s = "abcdefgh"
s.find("cd")  # => 2
s.find("gh")  # => 6
s.find("hi")  # => -1


"""
    3. .replace() permet de remplacer un caractère par un autre…
"""
"J'aime les pommes".replace("e", "z")  # => "J'aimz lzs pommzs"
#       …ou de le supprimer complètement (on passe une chaîne vide)
"J'aime les pommes".replace("e", "")  # => "J'aim ls pomms"

# D'autres méthodes sur les strings
####################################

#   1. La méthode .split(<separateur>) sépare une chaîne en une liste de
#      sous-chaînes (par défaut, le séparateur est l’espace)
"Il reste du fromage ?".split()  # => ['Il', 'reste', 'du', 'fromage', '?']
"12.5;17.5;18".split(";")  # => ['12.5', '17.5', '18']


"""
    2. La méthode .join() permet de convertir une liste de strings en une
       seule string
"""
lettres = ["p", "o", "u", "e", "t"]
"".join(lettres)  # => 'pouet'
"--".join(lettres)  # => 'p--o--u--e--t'
" ".join(["Salut","c'est","cool"])  # => "Salut c'est cool"

# TODO: détail

"""
Note : vous trouveriez plus logique d'écrire
lettres.join("--")    au lieu de     "--".join(lettres)  ? Moi aussi :)
"""


#   3. Les méthodes .upper() et .lower() changent la capitalisation d'une string
s2 = "aBcdEFgh"
s2.upper()  # => "ABCDEFGH"
s2.lower()  # => "abcdefgh"


"""
    4. La méthode .capitalize() va capitaliser la première lettre seulement, et
       mettre les autres lettres en minuscule
"""
s2.capitalize()  # => 'Abcdefgh'


"""
    5. Les méthodes .lstrip(), .rstrip() et .strip() enlèvent les espaces à
       droite et à gauche d'une chaîne (lstrip : left, rstrip : right, strip :
       les deux)
"""
"    des espaces  ".rstrip()    # => '    des espaces'
"    des espaces  ".lstrip()    # => 'des espaces  '
"    des espaces     ".strip()  # => 'des espaces'


"""
    6. Les méthodes .rjust(n) et .ljust(n) permettent de donner à une string
       une largeur fixe, ce qui est très pratique pour un affichage en
       colonnes de largeur fixe
"""
"abc".rjust(8)  # => '     abc'
"abc".ljust(8)  # => 'abc     '

# TODO

# Interpoler une chaîne
########################

"""
L'interpolation sert à insérer des variables dans des chaînes de caractère.
C'est très utile car un texte affiché par un programme doit souvent varier en
fonction d'une saisie utilisateur, d'une variable du programme, etc.
"""

# Quand on veut afficher du texte et une variable, on a vu qu'on pouvait
# concaténer des strings avec l'opérateur "+"
nom = "Michelle"
print("Je m'appelle " + nom) # => "Je m'appelle Michelle"

"""
Mais dès qu'on veut faire plus compliqué (prendre deux variables, ou utiliser
la variable au milieu d'un texte, par exemple), la concaténation est peu
pratique.

Exemple : on souhaite afficher un texte contenant un nom et un âge contenus
dans une variable. Avec la concaténation, cela donne:
"""
age = 15
nom = "Michelle"
print("Je m'appelle " + nom + " et j'ai " + str(age) + " ans.")
# => Je m'appelle Michelle et j'ai 15 ans.

"""
…mais c'est complexe : il faut bien penser aux espaces entre les mots, à
convertir les nombres en strings, etc.

L'interpolation règle la plupart de ces difficultés.
"""

"""
Il y a deux méthodes pour interpoler une chaîne de caractères :
    1. La méthode "historique" consiste à utiliser la méthode .format() sur une
       string en lui passant les paramètres souhaités
"""
"{} peuvent être {}".format("Les chaînes", "interpolées")  # => "Les chaînes
#                                                      peuvent être interpolées"

# Note : .format() convertit automatiquement depuis des entiers ou des floats,
# donc on n'aura pas besoin d'utiliser str() !
"Une string et {}".format(5)  # => "Une string et 5"

# Même si celà ne se fait plus trop, on peut aussi référencer les variables par
# leur index
"Je m'appelle {1} et j'ai {0} ans.".format(age, nom)  # => "Je m'appelle
#                                                     Michelle et j'ai 15 ans."

"""
    2. Depuis Python 3.6, on peut aussi utiliser les "f-strings" pour
       interpoler une chaîne avec des variables. La syntaxe en devient beaucoup
       plus lisible, et c'est la méthode la plus utilisée aujourd'hui
"""
f"Salut {nom} !" # => Salut Michelle !  (Notez le "f" en début de chaîne)
f"Je m'appelle {nom} et j'ai {age} ans."  # => "Je m'appelle Michelle et j'ai
#                                              15 ans."


# TODO: concaténation vs interpolation

# Conversions de caractères : chr() et ord()
#############################################

# On peut convertir chaque caractère en son indice Unicode, et inversement :

#   1. chr() renvoie le caractère associé à un indice Unicode
chr(65)     # => "A"
chr(97)     # => "a"
chr(233)    # => 'é'
chr(128561) # => "😱"

#   2. Inversement, ord() renvoie un indice Unicode associé à un caractère
ord("A")    # => 65
ord("a")    # => 97
ord("à")    # => 224
ord("😱")   # => 128561

# D'où il s'ensuit que :
chr(ord("A"))  # => 'A'
ord(chr(65))   # => 65

"""
On remarque que les codes ASCII des majuscules/minuscules sont décalés de 32.

On rappelle que les caractères ASCII sont aussi des caractères Unicode, et
vont jusqu'à 127 seulement.
"""

# Chaînes longues
########################

# La syntaxe utilisée pour les commentaires longs peut aussi servir pour les
# chaînes de plusieurs lignes !
s = """Ceci est
une chaîne
vraiment très longue"""
print(s)
"""
Imprimera :

Ceci est
une chaîne
vraiment très longue
"""

# Note : les chaînes longues sont très utilisées pour documenter du code.

# Si on ne souhaite pas avoir de sauts de ligne, on pourra utiliser des "\" en
# fin de chaque ligne
query = "SELECT action.descr as \"action\", " \
"role.id as role_id," \
"role.descr as role" \
"FROM " \
"public.role," \
"public.record_def, " \
"public.action" \
"WHERE role.id = role_action_def.role_id AND" \
"record_def.id = role_action_def.def_id;"

# L'impression se fera sur une seule ligne
print(query)
# SELECT action.descr as "action", role.id as role_id,role.descr as roleFROM public.role,public.record_def, public.actionWHERE role.id = role_action_def.role_id ANDrecord_def.id = role_action_def.def_id;
