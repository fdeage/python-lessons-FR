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
#  Chap. 3      #  Commentaires : corrigés                                     #
#               #                                                              #
################################################################################

##########################
#  Commentaires simples  #
##########################

"""
1. Quelles lignes affichent quelque chose ?
"""
# print("A")
print("B")  # print("C")
print("D # E")
#print("F")
"""
Seules deux lignes affichent quelque chose :
    - B : le print("B") est exécuté ; ce qui suit le # est un commentaire, donc
      print("C") n'est PAS exécuté ;
    - D # E : le # est À L'INTÉRIEUR d'une chaîne de caractères, ce n'est donc
      pas un commentaire mais un caractère comme un autre.
Les lignes A et F sont entièrement commentées (l'espace après le # n'est pas
obligatoire, mais recommandé).
"""
# => B
# => D # E

# 2. Un commentaire sur plusieurs lignes :
# Ce fichier contient les corrigés des exercices du chap. 3.
# Chaque exercice reprend l'énoncé, puis donne le code et des explications.
# On peut l'exécuter pour vérifier les résultats affichés.


##################################
#  Commentaires en fin de ligne  #
##################################

# 3. Le résultat attendu est noté après "=>" :
print(6 * 7)  # => 42

# 4. print(2 + 2)#=>4 fonctionne, mais ne respecte pas la PEP 8 : il faut au
# moins DEUX espaces avant le #, puis une espace après :
print(2 + 2)  # => 4


#######################
#  Commenter du code  #
#######################

# 5. Seule la ligne du milieu est commentée :
print(3)  # => 3
# print(2)
print(1)  # => 1

# 6. Une fois commentée, la ligne fautive n'est plus lue comme du code : le
# fichier peut s'exécuter. C'est une bonne technique pour isoler une erreur.
# print("Il manque une parenthèse"


######################################
#  Commentaires longs et docstrings  #
######################################

"""
7. Qu'affiche le programme ?
"""
'''print("Bonjour")'''
print('''Au revoir''')  # => Au revoir
"""
La première ligne est une CHAÎNE (qui contient le texte print("Bonjour")),
créée puis oubliée : le print() qu'elle contient n'est jamais exécuté.
La deuxième ligne affiche une chaîne écrite avec trois apostrophes : on peut
utiliser les triples guillemets pour n'importe quelle chaîne, pas seulement
pour des commentaires.

8. Différences entre # et les triples guillemets :
    - un commentaire # est totalement IGNORÉ par Python ; une chaîne à triples
      guillemets est une vraie valeur, créée puis oubliée ;
    - conséquences :
        * la chaîne doit être correctement fermée (sinon, erreur de syntaxe) ;
        * elle ne peut pas être placée en fin de ligne de code ;
        * elle doit respecter l'indentation du code qui l'entoure.

9. Le code n'est PAS valide : on ne peut pas placer une chaîne juste après
   une instruction, sur la même ligne. Python lève une SyntaxError (et le
   fichier entier refuserait de se lancer). En fin de ligne, il faut utiliser
   un # :
"""
print(5)  # affiche cinq
# => 5


# 10. La docstring est la première ligne sous le "def" :
def tripler(nombre):
    """Retourne le triple du nombre passé en paramètre."""
    return nombre * 3


print(tripler.__doc__)  # => Retourne le triple du nombre passé en paramètre.
print(tripler(5))  # => 15


###########################
#  Commentaires spéciaux  #
###########################

"""
11. #!/usr/bin/env python3 est le "shebang" : sur Linux et macOS, il indique au
    système quel programme doit exécuter le fichier, ce qui permet de le lancer
    avec ./mon_script.py (après chmod +x). Il doit être sur la TOUTE PREMIÈRE
    ligne du fichier.

12. # -*- coding: utf-8 -*- est inutile en Python 3 (l'UTF-8 est déjà
    l'encodage par défaut). # TODO : vérifier les arrondis est utile : il
    signale un travail restant, et les éditeurs savent retrouver les TODO.
"""


#############################
#  Bien commenter son code  #
#############################

"""
13. Commentaires utiles ou inutiles ?
    - "multiplie 60 par 60 par 24" : INUTILE, il répète ce que dit le code.
    - "nombre de secondes dans une journée" : UTILE, il explique le SENS du
      calcul (60 secondes × 60 minutes × 24 heures).
    - "poids (en newtons)…" : UTILE, il explique d'où vient 9.81 (la gravité
      terrestre) et l'unité du résultat.
    - "affiche 3" : NUISIBLE, il est faux ! Un commentaire faux est pire que
      pas de commentaire du tout.
"""
print(60 * 60 * 24)  # => 86400
print(9.81 * 2)  # => 19.62

# 14. On explique le POURQUOI du calcul :
# 1 km = 1000 m et 1 h = 3600 s : on convertit 100 km/h en m/s
print(100 * 1000 / 3600)  # => 27.77777777777778
