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
#  Chap. 21     #  Booléens II : corrigés                                      #
#               #                                                              #
################################################################################

######################
#  Tables de vérité  #
######################

"""
1. "not" est prioritaire sur "or" : on calcule d'abord "not A", puis le "or".

      A     | B     | not A or B
     ------ | ----- | ----------
      True  | True  | True
      True  | False | False
      False | True  | True
      False | False | True

   (C'est l'"implication" des mathématiciens : "si A alors B" n'est faux que
   quand A est vrai et B est faux.)
"""
for A in (True, False):
    for B in (True, False):
        print(A, B, not A or B)
# => True True True
# => True False False
# => False True True
# => False False True

"""
2. Avec n variables, il y a 2 ** n lignes : 2 ** 3 = 8 lignes pour 3
   variables, 2 ** 5 = 32 lignes pour 5 variables.
"""
for A in (True, False):
    for B in (True, False):
        for C in (True, False):
            print(A, B, C, A and (B or C))
# => True True True True
# => True True False True
# => True False True True
# => True False False False
# => False True True False   (et False pour les 3 lignes suivantes :
# => …                         dès que A est faux, le "and" est faux)


# 3. Pour deux booléens, "différents" équivaut à "un seul des deux est vrai" :
def xor(a, b):
    return a != b


for A in (True, False):
    for B in (True, False):
        print(A, B, xor(A, B))
# => True True False
# => True False True
# => False True True
# => False False False

# 4. C'est exactement un "ou exclusif" :
entree = True
dessert = False
print(entree != dessert)  # => True : commande valide (une seule des deux)


###########################
#  Les lois de De Morgan  #
###########################

"""
5. On distribue le "not" en échangeant "and" et "or", puis on inverse chaque
   comparaison ("not x > 0" devient "x <= 0", "not ==" devient "!=") :
     a) not (x > 0 and y > 0)          →  x <= 0 or y <= 0
     b) not (age < 12 or age > 60)     →  age >= 12 and age <= 60
                                          (ou mieux : 12 <= age <= 60)
     c) not (mot == "" or mot == "stop")  →  mot != "" and mot != "stop"
"""
# Vérification sur quelques valeurs :
x, y = 3, -1
print(not (x > 0 and y > 0), x <= 0 or y <= 0)  # => True True
age = 30
print(not (age < 12 or age > 60), 12 <= age <= 60)  # => True True
mot = "stop"
print(not (mot == "" or mot == "stop"), mot != "" and mot != "stop")
# => False False

# 6. On compare les deux expressions pour les 4 combinaisons :
for A in (True, False):
    for B in (True, False):
        print(A, B, not (A and B), not A and not B)
# => True True False False
# => True False True False    ← différents
# => False True True False    ← différents
# => False False True True
"""
Elles diffèrent quand UN SEUL des deux vaut True. C'est l'erreur classique :
quand on fait entrer le "not" dans la parenthèse, il faut AUSSI changer le
"and" en "or" (De Morgan) : not (A and B) == (not A) or (not B).
"""

# 7. Valeurs de test :
taille = 1.35
age = 9
# a) Avec "not" : on nie directement la condition de refus.
print(not (taille < 1.20 or age < 8))  # => True
# b) Sans "not" : De Morgan transforme le "or" en "and" et inverse les
#    comparaisons.
print(taille >= 1.20 and age >= 8)     # => True


##############################################
#  Calculs avec les booléens et conversions  #
##############################################

print(True + True + True)    # => 3
print(True * 10 - False)     # => 10 (1 * 10 - 0)
print((3 > 2) + (2 > 3))     # => 1 (True + False)
print(1 == True)             # => True
print(2 == True)             # => False (True vaut 1, pas 2)
print(int(False) + int(True))  # => 1

# 9. sum() compte les True (chacun vaut 1). On ramène ensuite sur 20 :
reponses = [True, True, False, True, False, True, True, True]
nb_justes = sum(reponses)
note = nb_justes / len(reponses) * 20
print(nb_justes, note)  # => 6 15.0


############################################
#  Valeurs "vraies" et "fausses" : bool()  #
############################################

# 10. Sont faux : 0, 0.0, "", [], {}, None. Tout le reste est vrai :
print(bool(0), bool(0.0), bool(-1))          # => False False True
print(bool(""), bool(" "), bool("0"))        # => False True True
print(bool("False"), bool([]), bool([[]]))   # => True False True
print(bool({}), bool(None), bool((0,)))      # => False False True
print(bool(0.001))                           # => True
"""
Pièges : " ", "0" et "False" sont des chaînes NON vides, donc vraies. [[]] et
(0,) contiennent un élément (même si cet élément est lui-même "faux") : ce
sont des collections non vides, donc vraies.
"""

# 11. Une valeur est utilisée telle quelle comme condition :
for valeur in [0, 1, "", "a", [], [0], None]:
    if valeur:
        print(valeur, "est vrai")
    else:
        print(valeur, "est faux")
# => 0 est faux
# => 1 est vrai
# =>  est faux        (la chaîne vide n'affiche rien avant l'espace)
# => a est vrai
# => [] est faux
# => [0] est vrai
# => None est faux


# 12. Une liste vide est "fausse", donc "not panier" est vrai si elle est vide :
def decrire_panier(panier):
    if not panier:
        print("Panier vide")
    else:
        print(len(panier), "article(s)")


decrire_panier([])                    # => Panier vide
decrire_panier(["pain", "fromage"])   # => 2 article(s)

# 13. "if stock:" est faux quand le stock vaut 0 : on confond "zéro" et
#     "inconnu". On teste explicitement None (la valeur "inconnue") :
stock = 0
if stock is not None:
    print("Stock :", stock)   # => Stock : 0
else:
    print("Stock inconnu")


##############################################
#  Ce que retournent vraiment "and" et "or"  #
##############################################

# 14. "or" retourne le 1er opérande "vrai" (ou le dernier) ; "and" retourne le
#     1er opérande "faux" (ou le dernier) :
print(0 or 7)              # => 7
print(4 or 7)              # => 4
print(0 and 7)             # => 0
print(4 and 7)             # => 7
print("" or "vide")        # => vide
print([] or [0])           # => [0]
print(repr(None or 0 or ""))  # => '' (aucun n'est vrai : on retourne le
#                                 dernier ; repr() montre la chaîne vide)
print("a" and "b" and "c")  # => c (tous vrais : on retourne le dernier)
print(not "abc")           # => False ("not" retourne toujours un booléen)


# 15. Si nom est vide, "nom or …" retourne la valeur de droite :
def saluer(nom):
    print("Bonjour", nom or "inconnu·e")


saluer("Ada")  # => Bonjour Ada
saluer("")     # => Bonjour inconnu·e

# 16. 0 est "faux" : la valeur par défaut REMPLACE un 0 pourtant valide.
places = 0
places_affichees = places or 2
print(places_affichees)  # => 2 (alors que la personne a réservé 0 place !)
"""
"or" ne convient que si toutes les valeurs "fausses" signifient "pas de
valeur". Pour un nombre, on teste explicitement None (avec un if, ou une
expression conditionnelle, cf. chap. 12) :
"""
places = 0
places_affichees = places if places is not None else 2
print(places_affichees)  # => 0


########################################
#  Égalité et identité : "==" et "is"  #
########################################

# 17.
a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b, a is c)  # => True False True
c.append(3)
print(a, b)                    # => [1, 2, 3] [1, 2]
b = a
print(a is b)                  # => True
"""
a et b ont le même contenu, mais ce sont deux listes distinctes. c désigne LA
MÊME liste que a : la modifier via c modifie a. Après "b = a", b désigne à
son tour cette même liste (l'ancienne liste [1, 2] de b est "oubliée").
"""

# 18. Valeurs de test :
resultat = None
est_admin = True
nom = "Ada"
if resultat is None:   # None : toujours avec "is"
    print("pas de résultat")  # => pas de résultat
if est_admin:          # un booléen se teste directement
    print("admin")            # => admin
if nom == "Ada":       # une chaîne : toujours "==" ("is" compare l'identité)
    print("bonjour Ada")      # => bonjour Ada
"""
Note : écrire 'nom is "Ada"' provoque d'ailleurs un SyntaxWarning
("is" with a literal) depuis Python 3.8 : Python lui-même le déconseille.
"""


####################
#  all() et any()  #
####################

print(all([True, True, False]))   # => False
print(any([False, False, True]))  # => True
print(all([1, 2, 3]))             # => True (aucun zéro)
print(any(["", 0, None]))         # => False (toutes ces valeurs sont fausses)
print(all([]))                    # => True (aucun élément n'est faux)
print(any([]))                    # => False (aucun élément n'est vrai)
print(all("abc"))                 # => True (chaque caractère est une chaîne
#                                    non vide)

# 20. On construit d'abord une liste de booléens avec une boucle :
temperatures = [12, 5, -2, 8, 15]
gel = []
raisonnables = []
for t in temperatures:
    gel.append(t < 0)
    raisonnables.append(-50 <= t <= 60)
print(any(gel))           # => True : il a gelé au moins une fois (-2)
print(all(raisonnables))  # => True : toutes sont entre -50 et 60


# 21. On cherche "au moins un" chiffre et "au moins une" majuscule : any().
def mot_de_passe_valide(mdp):
    chiffres = []
    majuscules = []
    for caractere in mdp:
        chiffres.append(caractere.isdigit())
        majuscules.append(caractere.isupper())
    return len(mdp) >= 8 and any(chiffres) and any(majuscules)


print(mot_de_passe_valide("python"))       # => False (trop court)
print(mot_de_passe_valide("pythonista1"))  # => False (pas de majuscule)
print(mot_de_passe_valide("Pythonista1"))  # => True


##############################
#  Les opérateurs bit à bit  #
##############################

"""
22. On pose les calculs colonne par colonne :
        1100            1100            1100
      & 1010          | 1010          ^ 1010
      ------          ------          ------
        1000 = 8        1110 = 14       0110 = 6
"""
print(0b1100 & 0b1010)  # => 8
print(0b1100 | 0b1010)  # => 14
print(0b1100 ^ 0b1010)  # => 6
print(5 << 2)           # => 20 (5 * 2 ** 2 ; 101 devient 10100)
print(40 >> 3)          # => 5 (40 // 2 ** 3)
print(~7)               # => -8 (~x vaut toujours -x - 1)

"""
23. "&" est plus prioritaire que les comparaisons : Python lit
    x > (1 & x) < 5, càd 10 > 0 < 5 (car 1 & 10 vaut 0), ce qui est vrai !
    Le message s'affiche donc à tort. Il faut utiliser "and" :
"""
x = 10
if x > 1 & x < 5:
    print("x est entre 1 et 5")  # => x est entre 1 et 5 (FAUX !)
if x > 1 and x < 5:
    print("x est entre 1 et 5")  # (n'affiche rien : c'est correct)
if 1 < x < 5:
    print("x est entre 1 et 5")  # (n'affiche rien : version la plus lisible)

# 24. Droits Linux :
LECTURE = 0b100
ECRITURE = 0b010
EXECUTION = 0b001
# a) "|" combine les bits :
droits = LECTURE | EXECUTION
print(droits, bin(droits))       # => 5 0b101
# b) "&" isole un bit : le résultat est non nul si le bit est présent.
droits = 6                        # 0b110 : lecture + écriture
print(droits & ECRITURE != 0)     # => True : écriture autorisée
print(droits & EXECUTION != 0)    # => False : exécution interdite
"""
Attention, "!=" est MOINS prioritaire que "&" (contrairement à "and") : on lit
bien (droits & ECRITURE) != 0. Dans le doute, ajoutez les parenthèses.
"""
# c) "^" inverse le bit d'écriture (ici, il était à 1 : il passe à 0) :
droits = 7                        # 0b111 : tous les droits
droits = droits ^ ECRITURE
print(droits, bin(droits))        # => 5 0b101
