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
#  Chap. 12     #  if, then, else et elif : corrigés                           #
#               #                                                              #
################################################################################

##############
#  FizzBuzz  #
##############

"""
0. écrire du code qui affiche si un nombre est pair, et sinon ne fait rien.
"""
n = 7
if n % 2 == 0:
    print(n, "est pair")
# (rien n'est affiché ici : 7 est impair. Essayez avec n = 8 !)

"""
1. écrire du code qui teste si un nombre est un multiple de 3 ou de 5, et
affiche le texte correspondant.
"""
n = 7
if n % 3 == 0:
    print(n, "est multiple de 3")
elif n % 5 == 0:
    print(n, "est multiple de 5")
else:
    print(n, "n'est multiple ni de 3 ni de 5")
    # => 7 n'est multiple ni de 3 ni de 5


"""
2. écrire du code qui teste si un nombre est un multiple de 3, de 5 ou de 15.
Pour le texte affiché :
  - au lieu de "est multiple de 3", on affiche "Fizz"
  - au lieu de "est multiple de 5", on affiche "Buzz"
  - au lieu de "est multiple de 15", on affiche "FizzBuzz"

De combien de conditions avez-vous besoin ?
"""

# On peut fonctionner avec une seule condition :
n = 7
if n % 15 == 0:
    # L'ordre est capital ! Sinon on passe dans la condition 3 ou 5
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    # Cette ligne ne change pas, pourquoi ?
    print(n, "n'est multiple ni de 3 ni de 5")
    # => 7 n'est multiple ni de 3 ni de 5

# Alternative beaucoup moins élégante, avec deux "if" imbriqués :
n = 7
if n % 3 == 0:
    # Si n est multiple de 3, il peut AUSSI être multiple de 15
    if n % 15 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
elif n % 5 == 0:
    # Si n est multiple de 5, il peut AUSSI être multiple de 15
    if n % 15 == 0:
        print("FizzBuzz")
    else:
        print("Buzz")
else:
    print(n, "n'est multiple ni de 3 ni de 5")
    # => 7 n'est multiple ni de 3 ni de 5


"""
3. Écrire du code qui, pour tous les entiers de 1 à 100, affiche :
    - Fizz si le nombre est multiple de 3,
    - Buzz si le nombre est multiple de 5,
    - FizzBuzz si le nombre est multiple de 15,
    - le nombre lui-même dans les autres cas.
"""

# Cette partie et la suivante utilisent une boucle "for", qui ne sera vue
# qu'au chap. 13 : revenez-y après l'avoir lu.
# range(1, 101) parcourt les entiers de 1 à 100 : le premier paramètre évite
# de commencer à 0, et la borne de fin (101) est EXCLUE (cf. chap. 13).
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


"""
4. écrire du code qui calcule la somme des nombres inférieurs ou égaux à 100 qui
sont multiples de 3, 5 ou 15.
"""
s = 0
for i in range(1, 101):
    # Dans les deux cas, on ajoutera le nombre au total : plus besoin de
    # différencier !
    if i % 3 == 0 or i % 5 == 0:
        s += i
    # pas de clause else, car on ne fait rien s'il n'est pas multiple

print(s)  # => 2418


#########################
#  La structure "if"    #
#########################

"""
5. Qu'affiche ce programme ?
"""
temperature = 25
if temperature > 30:
    print("Il fait très chaud")
print("Bonne journée")  # => Bonne journée
"""
La condition 25 > 30 est fausse : le bloc indenté est ignoré. Le dernier
print() n'est PAS indenté : il ne fait pas partie du "if" et s'exécute
toujours.
"""

# 6. "Mot court" si le mot contient moins de 5 lettres :
mot = "python"
if len(mot) < 5:
    print("Mot court")
# (rien n'est affiché : "python" a 6 lettres)
mot = "go"
if len(mot) < 5:
    print("Mot court")  # => Mot court

# 7. Comparaison "encadrée" : les deux bornes sont incluses avec <=
age = 34
if 0 <= age <= 120:
    print("Âge valide")  # => Âge valide
# C'est équivalent à : if age >= 0 and age <= 120:

"""
8. Quels "if" affichent quelque chose ?
   Une condition qui n'est pas un booléen est convertie implicitement :
   0, 0.0 et "" (la chaîne vide) sont considérés comme faux ; tous les autres
   nombres et toutes les autres chaînes sont vrais, y compris la chaîne
   "False" (qui n'est pas vide !).
   Seuls B et D sont donc affichés.
"""
if 0:
    print("A")
if 42:
    print("B")  # => B
if "":
    print("C")
if "False":
    print("D")  # => D
if 0.0:
    print("E")
# (On a remis chaque print() sur sa propre ligne, comme le recommande la
# PEP 8.)


#######################
#  Le mot-clé "else"  #
#######################

# 9. Majeur ou mineur :
age = 16
if age >= 18:
    print("majeur")
else:
    print("mineur")  # => mineur

# 10. Livraison offerte à partir de 50 € :
montant = 42.5
if montant >= 50:
    print("Livraison offerte")
else:
    print(f"Il manque {50 - montant} € pour la livraison offerte")
    # => Il manque 7.5 € pour la livraison offerte
"""
"au moins 50 €" signifie que 50 € pile donne droit à la livraison : on utilise
donc >=, et non >.
"""

# 11. Valeur absolue sans abs() :
x = -12
if x >= 0:
    print(x)
else:
    print(-x)  # => 12
# Pour un nombre négatif, -x est positif : -(-12) vaut 12.


#######################
#  Le mot-clé "elif"  #
#######################

# 12. État de l'eau selon la température :
temperature = 37
if temperature < 0:
    print("glace")
elif temperature < 100:
    print("eau")  # => eau
else:
    print("vapeur")
"""
Grâce à elif, on n'a pas besoin d'écrire 0 <= temperature < 100 : si on
arrive au "elif", c'est que la première condition était fausse, donc que la
température est déjà supérieure ou égale à 0.

13. Les conditions sont testées DANS L'ORDRE, et seule la première condition
    vraie est exécutée. Or 17 >= 10 est vrai : on affiche "passable" et on
    ignore tout le reste. Il faut tester les seuils du plus HAUT au plus BAS :
"""
note = 17
if note >= 16:
    print("très bien")  # => très bien
elif note >= 14:
    print("bien")
elif note >= 12:
    print("assez bien")
elif note >= 10:
    print("passable")
else:
    print("recalé")

# 14. Avec "elif", seul le premier bloc vrai est exécuté :
x = 5
if x > 3:
    x = x + 10
elif x > 10:  # jamais testé, car la première condition était vraie
    x = x * 2
print(x)  # => 15

# Avec deux "if" séparés, la seconde condition est testée APRÈS la
# modification de x (qui vaut alors 15) :
x = 5
if x > 3:
    x = x + 10
if x > 10:
    x = x * 2
print(x)  # => 30


#####################################
#  Indentation et "if" imbriqués    #
#####################################

# 15. Pour a = 5 : la première condition est vraie, mais pas la seconde.
a = 5
if a > 0:
    print("positif")  # => positif
    if a > 10:
        print("grand")
print("fin")  # => fin
# Pour a = -5 : seul "fin" est affiché, car il est en dehors du "if".
a = -5
if a > 0:
    print("positif")
    if a > 10:
        print("grand")
print("fin")  # => fin

# 16. Année bissextile, avec des "if" imbriqués :
annee = 1900
if annee % 4 == 0:
    if annee % 100 == 0:
        if annee % 400 == 0:
            print(annee, "est bissextile")
        else:
            print(annee, "n'est pas bissextile")  # => 1900 n'est pas bissextile
    else:
        print(annee, "est bissextile")
else:
    print(annee, "n'est pas bissextile")

# Avec une seule condition : divisible par 4 ET pas par 100, OU divisible
# par 400.
annee = 2000
if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
    print(annee, "est bissextile")  # => 2000 est bissextile
else:
    print(annee, "n'est pas bissextile")
"""
La seconde version est plus courte, mais il faut bien la tester : changez la
valeur de annee (2024, 1900, 2000, 2023) et vérifiez chaque cas. Les
parenthèses ne sont pas obligatoires ("and" passe avant "or", cf. chap. 5),
mais elles rendent la condition beaucoup plus lisible.
"""

# 17. Deux "if" imbriqués sans "else" se combinent avec "and" :
age = 20
pays = "France"
if age >= 18 and pays == "France":
    print("Vous pouvez voter en France")  # => Vous pouvez voter en France


########################################
#  Le mot-clé "pass" et pièges         #
########################################

# 18. "pass" ne fait rien : il permet d'écrire un bloc vide, que Python
# refuserait sinon (IndentationError).
commande = ""
if commande == "":
    pass  # TODO : décider quoi faire pour une commande vide
else:
    print("Traitement de la commande", commande)
# (rien n'est affiché)

"""
19. Les erreurs :
    a. il manque les ":" à la fin de la ligne du "if" (SyntaxError) ;
    b. "=" est l'affectation : pour tester l'égalité, il faut "=="
       (SyntaxError) ;
    c. Python lit (fruit == "pomme") or ("poire") : la chaîne "poire" n'est
       pas vide, donc toujours vraie. La condition est vraie pour N'IMPORTE
       QUEL fruit ! Il faut répéter la comparaison ;
    d. input() retourne toujours une string : on ne peut pas la comparer à un
       int avec >= (TypeError). Il faut d'abord la convertir avec int().
Versions corrigées :
"""
x = 3
if x == 3:
    print("trois")  # => trois

fruit = "cerise"
if fruit == "pomme" or fruit == "poire":
    print("fruit à pépins")
# (rien n'est affiché : la cerise n'est pas un fruit à pépins)

saisie = "20"  # comme si cette valeur venait de input()
try:
    if saisie >= 18:
        print("majeur")
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
if int(saisie) >= 18:
    print("majeur")  # => majeur


################################
#  Les "one-liner" avec if     #
################################

# 20. Avec une expression conditionnelle :
note = 9
resultat = "admis" if note >= 10 else "ajourné"
print(resultat)  # => ajourné

# 21. 7 % 2 vaut 1, donc la condition x % 2 == 0 est fausse :
x = 7
y = "pair" if x % 2 == 0 else "impair"
print(y)  # => impair

# 22. Le "s" n'est ajouté que si nb_chats est supérieur à 1 :
nb_chats = 1
print(nb_chats, "chat" if nb_chats == 1 else "chats")  # => 1 chat
nb_chats = 4
print(nb_chats, "chat" if nb_chats == 1 else "chats")  # => 4 chats
