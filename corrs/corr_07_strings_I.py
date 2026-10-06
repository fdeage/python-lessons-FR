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
#  Chap. 7      #  Strings I : corrigés                                        #
#               #                                                              #
################################################################################

##########################
#  Déclarer des strings  #
##########################

"""
1. Lignes c) et d) : erreurs de syntaxe.
   c) 'Il m'a dit bonjour' : la chaîne commence par une simple quote, donc
      Python la croit finie à l'apostrophe de "m'" ; le reste (a dit…) n'a
      plus de sens.
   d) "Elle a crié "Stop !"" : même problème avec les doubles quotes, la
      chaîne s'arrête juste avant Stop.
   b) et e) fonctionnent : on peut mettre des simples quotes dans une chaîne
   entre doubles quotes, et inversement. a) est une chaîne toute simple.

   Une SyntaxError empêche le fichier entier de se lancer : on ne peut pas
   l'intercepter avec try … except, d'où ces explications en commentaire.
"""

# 2. a) Entre doubles quotes, seuls les guillemets intérieurs sont échappés :
print("L'été sera \"chaud\"")  # => L'été sera "chaud"
#    b) Entre simples quotes, c'est l'apostrophe qu'il faut échapper :
print('L\'été sera "chaud"')    # => L'été sera "chaud"
# Règle : on n'échappe que le type de quote qui sert à délimiter la chaîne.

# 3. Comparaisons :
print("abc" == 'abc')  # => True : simples et doubles quotes sont équivalentes
print("abc" == "ABC")  # => False : les majuscules sont d'autres caractères
print("" == " ")       # => False : la chaîne vide n'est pas un espace


############################
#  Accéder à un caractère  #
############################

mot = "Python"

"""
     P  y  t  h  o  n
     0  1  2  3  4  5
    -6 -5 -4 -3 -2 -1
"""

# 4. Indices positifs et négatifs :
print(mot[0])   # => P
print(mot[5])   # => n (le dernier : la chaîne a 6 caractères, indices 0 à 5)
print(mot[-1])  # => n (-1 désigne toujours le dernier caractère)
print(mot[-6])  # => P (ici, -6 désigne le premier)

# 5. L'indice 6 n'existe pas :
try:
    mot[6]
except IndexError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# 6. "h" est le 4e caractère : indice 3, ou -3 en partant de la fin.
print(mot[3], mot[-3])  # => h h

# 7. a) Les chaînes sont immuables : on ne peut pas modifier un caractère.
try:
    mot[0] = "J"
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

#    b) On crée donc une NOUVELLE chaîne :
nouveau = "J" + mot[1] + mot[2] + mot[3] + mot[4] + mot[5]
print(nouveau)  # => Jython
print(mot)      # => Python (l'original n'a pas changé)
# (Au chap. 31, on écrira beaucoup plus simplement : "J" + mot[1:])


########################################
#  Caractères spéciaux et échappement  #
########################################

# 8. "\n" est UN caractère, "\\" aussi ; dans une chaîne brute, le
#    backslash n'est plus spécial et compte comme un caractère normal.
print(len("a\nb"))   # => 3 : a, saut de ligne, b
print(len("a\\nb"))  # => 4 : a, \, n, b
print(len(r"a\nb"))  # => 4 : pareil, avec une chaîne brute

# 9. Les sauts de ligne "\n" découpent l'affichage :
print("Nom : Lovelace\nPrénom : Ada\nNée en : 1815")
# => Nom : Lovelace
# => Prénom : Ada
# => Née en : 1815

# 10. a) En doublant chaque backslash :
print("C:\\Users\\ana\\notes.txt")  # => C:\Users\ana\notes.txt
#     b) Avec une chaîne brute :
print(r"C:\Users\ana\notes.txt")    # => C:\Users\ana\notes.txt
r"""
Sans précaution, "\n" (dans "\notes") deviendrait un saut de ligne, et pire,
"\U" (dans "\Users") est le début d'un code Unicode long (\UXXXXXXXX) : Python
refuserait même de lancer le fichier (SyntaxError). Les chaînes brutes sont
donc très pratiques pour les chemins Windows.
"""

# 11. "\t" insère une tabulation, qui aligne les colonnes :
print("Fruit\tPrix\nPomme\t2\nKiwi\t3")
# => Fruit	Prix
# => Pomme	2
# => Kiwi	3

# 12. \u suivi de 4 chiffres hexadécimaux insère un caractère Unicode :
print("No\u00ebl")  # => Noël


###########################
#  Imprimer avec print()  #
###########################

# 13.
print("a", "b", "c", sep="")          # => abc (séparateur vide)
print("a", "b", sep=" - ", end="!\n")  # => a - b!
print(1, 2.5, True)                    # => 1 2.5 True
# Dans le 2e cas, end remplace le saut de ligne final : on remet donc "\n"
# nous-mêmes après le "!", sinon le print() suivant continuerait sur la même
# ligne.

# 14. Le 1er print() ne va pas à la ligne, grâce à end :
print("Calcul en cours...", end=" ")
print("terminé !")
# => Calcul en cours... terminé !

# 15. sep="/" est inséré ENTRE les valeurs :
print("05", "10", "2026", sep="/")  # => 05/10/2026


###############################################
#  Opérations de base : len(), +, * et str()  #
###############################################

# 16.
print(len("Bonjour"))  # => 7
print(len(" "))        # => 1 (un espace est un caractère comme un autre)
print("ab" + "cd")     # => abcd
print("ab" * 3)        # => ababab
print("-" * 0)         # => (une ligne vide : la chaîne vide)

# 17. a), c) et e) fonctionnent :
print("3" + "4")  # => 34 (concaténation de deux strings, PAS une addition !)
print("3" * 4)    # => 3333 (string * int : répétition)
print(3 * "ab")   # => ababab (l'ordre int * string marche aussi)
#     b) et d) échouent :
try:
    "3" + 4  # on ne peut concaténer qu'une string avec une string
except TypeError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    "3" * "4"  # on ne peut répéter une string qu'un nombre ENTIER de fois
except TypeError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")

# 18. On convertit l'entier avec str() avant de concaténer :
age = 17
print("J'ai " + str(age) + " ans")  # => J'ai 17 ans
# (Sans str(), on aurait l'erreur de l'exercice 17 b.)

# 19. Le cadre fait len(mot) + 2 tirets de large (un espace de chaque côté) :
mot = "Python"
bord = "+" + "-" * (len(mot) + 2) + "+"
print(bord)                  # => +--------+
print("| " + mot + " |")     # => | Python |
print(bord)                  # => +--------+
# Essayez avec mot = "Data Science" : le cadre s'agrandit tout seul.


#################################################
#  Une première méthode : .upper() et .lower()  #
#################################################

# 20. Le programme affiche Bonjour : s.upper() RETOURNE une nouvelle chaîne,
#     mais ne modifie pas s (les chaînes sont immuables) ; et comme on ne fait
#     rien de cette nouvelle chaîne, elle est perdue.
s = "Bonjour"
s.upper()
print(s)  # => Bonjour
# Correction : on stocke le résultat (ici, dans la même variable).
s = s.upper()
print(s)  # => BONJOUR

# 21. On met les deux chaînes en minuscules AVANT de les comparer :
print("PyThOn".lower() == "python".lower())  # => True
print("PyThOn" == "python")                  # => False (sans .lower())
