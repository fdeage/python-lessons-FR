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
#  Chap. 13     #  Les boucles : corrigés                                      #
#               #                                                              #
################################################################################


#########################
#  La boucle "while"    #
#########################

"""
1. Sans exécuter : qu'affiche ce programme ? (tableau de trace)
"""
x = 1
y = 0
while x < 5:
    y = y + x
    x = x + 1
print(x, y)  # => 5 10
"""
Tableau de trace (valeurs EN FIN de chaque tour) :

    tour | x | y
    -----+---+----
    avant| 1 | 0
      1  | 2 | 1    (y = 0 + 1)
      2  | 3 | 3    (y = 1 + 2)
      3  | 4 | 6    (y = 3 + 3)
      4  | 5 | 10   (y = 6 + 4)

Au début du 5e tour, x vaut 5 : la condition x < 5 est fausse, la boucle
s'arrête. y contient la somme 1 + 2 + 3 + 4 = 10.
"""

"""
2. Sans exécuter : combien de fois "coucou" est-il affiché ?
"""
n = 10
while n > 0:
    print("coucou")
    n = n - 3
# => coucou
# => coucou
# => coucou
# => coucou
"""
4 fois : n vaut successivement 10, 7, 4, 1 (affichages), puis -2. La
condition n > 0 est alors fausse.
"""

"""
3. Sans exécuter : que se passe-t-il ? Corrigez-le.

Le programme d'origine ne modifie jamais i : la condition i < 5 reste vraie
pour toujours, et la boucle affiche 0 indéfiniment (une "boucle infinie",
qu'on interrompt avec Ctrl + C). Il manque l'incrémentation :
"""
i = 0
while i < 5:
    print(i, end=" ")
    i = i + 1  # sans cette ligne, la boucle ne s'arrête jamais
print()  # => 0 1 2 3 4

"""
4. Les puissances de 2 inférieures à 1000 :
"""
puissance = 1
while puissance < 1000:
    print(puissance, end=" ")
    puissance = puissance * 2
print()  # => 1 2 4 8 16 32 64 128 256 512
"""
On ne sait pas à l'avance combien de tours faire : c'est le cas typique du
while, qui tourne "tant que" la condition est vraie.
"""

"""
5. Au bout de combien d'années le capital dépasse-t-il 2000 € ?
"""
capital = 1000
annees = 0
while capital <= 2000:
    capital = capital * 1.03
    annees = annees + 1
print(annees)              # => 24
print(round(capital, 2))   # => 2032.79
"""
Il faut 24 ans pour doubler un capital placé à 3 %. (Les financiers utilisent
la "règle de 72" : 72 / 3 = 24 ans. Elle donne ici le bon résultat !)
"""


#########################################
#  La boucle "for" avec une collection  #
#########################################

# 6. Chaque lettre de "Python" :
for lettre in "Python":
    print(lettre)
# => P
# => y
# => t
# => h
# => o
# => n

# 7. Les voyelles d'une phrase :
phrase = "les boucles sont partout en programmation"
nb_voyelles = 0
for c in phrase:
    if c in "aeiouy":
        nb_voyelles = nb_voyelles + 1
print(nb_voyelles)  # => 14
"""
nb_voyelles est un COMPTEUR : on l'initialise à 0 AVANT la boucle, et on
l'augmente de 1 à chaque voyelle rencontrée.
"""

# 8. Une boucle sur une liste :
for ville in ["Paris", "Lyon", "Marseille"]:
    print("J'aime", ville)
# => J'aime Paris
# => J'aime Lyon
# => J'aime Marseille

# 9. Inverser une chaîne :
mot = "bonjour"
inverse = ""
for c in mot:
    inverse = c + inverse  # on ajoute chaque lettre DEVANT les précédentes
print(inverse)  # => ruojnob
"""
Trace : "" → "b" → "ob" → "nob" → "jnob" → "ojnob" → "uojnob" → "ruojnob".
Si l'on écrivait inverse = inverse + c, on reconstruirait le mot à l'endroit.
"""


################################################
#  La boucle "for" avec la fonction range()    #
################################################

# 10. Contenu des range() :
print(list(range(6)))         # => [0, 1, 2, 3, 4, 5]
print(list(range(2, 9)))      # => [2, 3, 4, 5, 6, 7, 8]
print(list(range(1, 20, 4)))  # => [1, 5, 9, 13, 17]
print(list(range(10, 0, -2)))  # => [10, 8, 6, 4, 2]
print(list(range(5, 5)))      # => []
"""
Retenez : la borne de fin n'est JAMAIS incluse (9 dans b, 20 dans c, 0 dans
d). range(5, 5) est vide : on part de 5, et on doit s'arrêter avant 5.
"""

# 11. La table de 7 :
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)
# => 7 x 1 = 7
# => 7 x 2 = 14
# => 7 x 3 = 21
# => 7 x 4 = 28
# => 7 x 5 = 35
# => 7 x 6 = 42
# => 7 x 7 = 49
# => 7 x 8 = 56
# => 7 x 9 = 63
# => 7 x 10 = 70
# (range(1, 11) et non range(1, 10) : sinon 7 x 10 manquerait.)

# 12. Somme des nombres pairs de 2 à 100, de deux façons :
somme = 0
for i in range(1, 101):
    if i % 2 == 0:
        somme = somme + i
print(somme)  # => 2550

somme = 0
for i in range(2, 101, 2):  # de 2 en 2 : uniquement les pairs
    somme = somme + i
print(somme)  # => 2550
"""
La 2e version fait deux fois moins de tours de boucle, et n'a pas besoin de
"if" : quand c'est possible, laissez range() faire le travail.
"""

# 13. Que vaut i après la boucle ?
for i in range(3):
    pass
print(i)  # => 2
"""
La variable de boucle continue d'exister après la boucle (cf. chap. 13), et
garde la DERNIÈRE valeur qu'elle a prise : 2 (et non 3, puisque range(3)
s'arrête avant 3).
"""


##########################################
#  Équivalence entre "while" et "for"    #
##########################################

# 14. La même boucle avec for :
for i in range(10, 51, 10):
    print(i, end=" ")
print()  # => 10 20 30 40 50
"""
La condition i <= 50 devient la borne 51 (exclue), et i = i + 10 devient le
pas de range().
"""

"""
15. On peut toujours écrire un for sous forme de while, mais pas l'inverse
facilement : un for parcourt une collection CONNUE à l'avance (une chaîne,
une liste, un range…). Dans l'exercice 5, on ne sait pas combien d'années il
faudra : on veut répéter "tant que" le capital ne dépasse pas 2000 €. C'est
exactement ce qu'exprime while.

Règle pratique :
    - on sait combien de tours faire (ou sur quoi boucler) → for
    - on répète jusqu'à ce qu'une condition change → while
"""


#########################################
#  Les mots-clés "break" et "continue"  #
#########################################

# 16. break et continue :
for i in range(10):
    if i == 4:
        break
    print(i, end=" ")
print()  # => 0 1 2 3
for i in range(10):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()  # => 1 2 4 5 7 8
"""
- break QUITTE la boucle dès que i vaut 4 : 4 n'est même pas affiché.
- continue SAUTE la fin du tour en cours (le print) et passe au suivant :
  les multiples de 3 (0, 3, 6, 9) ne sont pas affichés.
"""

# 17. Le plus petit n tel que n * n dépasse 500 :
for n in range(1, 1000):
    if n * n > 500:
        break
print(n)  # => 23
"""
22 * 22 = 484 et 23 * 23 = 529. Dès qu'on trouve le bon n, break arrête la
boucle : n garde sa valeur, qu'on affiche après. (Une boucle while n * n <= 500
ferait aussi bien l'affaire.)
"""

# 18. Ni multiples de 2, ni multiples de 3 :
for i in range(1, 21):
    if i % 2 == 0 or i % 3 == 0:
        continue
    print(i, end=" ")
print()  # => 1 5 7 11 13 17 19


#################################
#  Compteurs et accumulateurs   #
#################################

# 19. 2 puissance 10 sans ** :
resultat = 1  # surtout pas 0 : 0 * 2 vaudrait toujours 0
for _ in range(10):
    resultat = resultat * 2
print(resultat)  # => 1024
"""
"_" est le nom conventionnel d'une variable de boucle dont on ne se sert pas
(cf. chap. 13) : on veut juste répéter 10 fois.
"""

# 20. Les multiples de 7 entre 1 et 1000 :
compteur = 0
for i in range(1, 1001):
    if i % 7 == 0:
        compteur = compteur + 1
print(compteur)  # => 142
# (Vérification : 1000 // 7 = 142.)

# 21. Somme et maximum des chiffres d'une chaîne :
donnees = "3, 7, 1, 9, 4"
somme = 0
plus_grand = 0
for c in donnees:
    if c.isdigit():  # on ignore les virgules et les espaces
        chiffre = int(c)
        somme = somme + chiffre
        if chiffre > plus_grand:
            plus_grand = chiffre
print(somme, plus_grand)  # => 24 9
"""
La somme vaut 3 + 7 + 1 + 9 + 4 = 24.

plus_grand est un "accumulateur" un peu particulier : on le compare à chaque
nouvelle valeur, et on le remplace si elle est plus grande. On peut
l'initialiser à 0 ici car tous les chiffres sont positifs.
"""

# 22. 28 est-il parfait ?
n = 28
somme_diviseurs = 0
for d in range(1, n):  # tous les diviseurs possibles, sauf n lui-même
    if n % d == 0:
        somme_diviseurs = somme_diviseurs + d
print(somme_diviseurs)       # => 28 (1 + 2 + 4 + 7 + 14)
print(somme_diviseurs == n)  # => True : 28 est parfait


#########################
#  Boucles imbriquées   #
#########################

# 23. Combien de "x" ?
for i in range(3):
    for j in range(4):
        print("x", end="")
print()  # => xxxxxxxxxxxx
"""
12 "x" : la boucle intérieure fait 4 tours, et elle est elle-même exécutée
3 fois. Pour des boucles imbriquées, on MULTIPLIE les nombres de tours.
"""

# 24. Un triangle, avec deux boucles imbriquées :
for ligne in range(1, 6):
    for _ in range(ligne):
        print("*", end="")
    print()  # saut de ligne à la fin de chaque ligne du triangle
# => *
# => **
# => ***
# => ****
# => *****

# … ou avec une seule boucle et l'opérateur * sur les chaînes :
for ligne in range(1, 6):
    print("*" * ligne)
# (même affichage)

# 25. Les tables de 1 à 5 :
for table in range(1, 6):
    for i in range(1, 11):
        print(table * i, end=" ")
    print()
# => 1 2 3 4 5 6 7 8 9 10
# => 2 4 6 8 10 12 14 16 18 20
# => 3 6 9 12 15 18 21 24 27 30
# => 4 8 12 16 20 24 28 32 36 40
# => 5 10 15 20 25 30 35 40 45 50
"""
La boucle extérieure choisit la table, la boucle intérieure parcourt les
multiplicateurs. Le print() vide, placé APRÈS la boucle intérieure (même
indentation que le for intérieur), passe à la ligne une fois par table.
"""
