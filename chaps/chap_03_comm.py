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
#  Chap. 3      #  Commentaires                                                #
#               #                                                              #
################################################################################
#
#  - Commentaires simples
#  - Commentaires en fin de ligne
#  - Commenter du code
#  - Commentaires longs et docstrings
#  - Commentaires spéciaux
#  - Bien commenter son code
#
######################################

# Commentaires simples
#######################

# Un commentaire de ligne commence par un dièse ou hashtag (#), souvent suivi
# d'une espace. On peut commenter une ligne de code en insérant un "#" au début.
# La ligne ne sera alors plus considérée comme du code, mais comme du texte.
# Elle ne sera plus exécutée.

# Ainsi, ce fichier de tutoriel est du code Python, mais toute la mise en
# forme du texte est réalisée avec des commentaires (et des chaînes à triples
# guillemets, cf. plus bas) !

# Python ignore entièrement ce qui suit le #, jusqu'à la fin de la ligne : on
# peut donc y écrire n'importe quoi, même du texte qui ne serait pas du code
# valide (accents, ponctuation, symboles…) !

# Note : un # placé à l'intérieur d'une chaîne de caractères (entre
# guillemets, cf. chap. 7) n'est PAS un commentaire, c'est un caractère comme un
# autre :
print("Le # est un dièse")  # => Le # est un dièse


# Commentaires en fin de ligne
###############################

# Un commentaire peut aussi être placé à la fin d'une ligne de code : le code
# avant le # est exécuté, le texte après est ignoré.
print(1 + 1)  # Ce texte est ignoré, mais le print() est bien exécuté

# Ce cours utilise abondamment cette possibilité pour indiquer le résultat
# attendu d'une ligne, après "=>" (cf. chap. 1) :
print(10 - 3)  # => 7

# Par convention (PEP 8, cf. chap. 20), on laisse au moins DEUX espaces entre
# le code et le #, puis une espace après le # :
print("ok")  # bien
print("ok")# moins lisible


# Commenter du code
####################

# Il peut être pratique de laisser du code sous forme commentée, pour pouvoir
# le décommenter plus tard si besoin. La ligne suivante ne s'exécute pas :
# print("Cette ligne ne sera jamais affichée")

# C'est aussi une technique très utile pour chercher une erreur : on
# "désactive" des lignes une par une pour trouver celle qui pose problème.

# La plupart des éditeurs proposent un raccourci clavier pour commenter ou
# décommenter la ligne courante ou la sélection (souvent Ctrl + / , ou
# Cmd + / sur Mac) : c'est un des raccourcis à connaître (cf. chap. 1).

# Attention toutefois : ne laissez pas traîner trop de code commenté dans un
# programme terminé. On ne sait plus s'il est important ou obsolète, et il
# encombre la lecture. Les outils de gestion de versions (comme git) permettent
# de retrouver les anciennes versions du code : pas besoin de tout garder !


# Commentaires longs et docstrings
###################################

"""
On peut aussi créer des chaînes de caractères avec trois guillemets doubles.

Ces chaînes ne sont pas des commentaires à proprement parler, mais peuvent être
utilisées comme telles, notamment pour expliquer ("documenter") certaines
parties de son programme.

Ce format de commentaire est fréquent en introduction de fonction
(cf. chap. 14), pour annoncer ce que fait le code introduit. On l'appelle alors
une "docstring".

Grâce à ces trois guillemets, on ne sera plus obligé de répéter # à chaque début
de ligne. On finira ensuite le commentaire avec trois guillemets de la même
façon, comme ceci :
"""

"""Une chaîne à triples guillemets peut aussi tenir sur une seule ligne."""

'''
On peut également utiliser trois apostrophes (guillemets simples) : le résultat
est le même. Les triples guillemets doubles restent la convention la plus
répandue (PEP 257).
'''

"""
Différence importante avec # : une chaîne à triples guillemets n'est PAS
ignorée par Python. C'est une vraie valeur (une chaîne de caractères, cf.
chap. 7), qui est créée puis immédiatement oubliée, car on n'en fait rien
(cf. chap. 2, "Mode interactif vs fichier"). Conséquences :
    - elle doit être correctement fermée : si on oublie les trois guillemets de
      fin, tout le reste du fichier fait partie de la chaîne… et Python signale
      une erreur à la fin du fichier ;
    - on ne peut pas la placer n'importe où : en fin de ligne de code, par
      exemple, il faut utiliser # ;
    - elle doit respecter l'indentation du code qui l'entoure (cf. chap. 5 et
      chap. 12).

En pratique : utilisez # pour les commentaires, et réservez les triples
guillemets aux longues explications (comme dans ce cours) et aux docstrings.

Voici un aperçu d'une docstring de fonction. Ne cherchez pas à comprendre le
"def" pour l'instant : les fonctions seront vues au chap. 14. Retenez seulement
que la docstring est la première ligne sous le "def", et qu'elle décrit ce que
fait la fonction.
"""


def doubler(nombre):
    """Retourne le double du nombre passé en paramètre."""
    return nombre * 2


print(doubler(21))  # => 42

# Contrairement à un commentaire avec #, une docstring est conservée par Python
# et accessible pendant l'exécution : c'est ce qu'affiche la fonction help()
# (cf. chap. 2). On peut aussi la lire directement :
print(doubler.__doc__)  # => Retourne le double du nombre passé en paramètre.


# Commentaires spéciaux
########################

"""
Certains commentaires ont un sens particulier pour d'autres programmes que
Python lui-même. Vous les croiserez souvent en début de fichier :

    #!/usr/bin/env python3
        Le "shebang" : sur Linux et macOS, il indique au système quel
        programme utiliser pour exécuter le fichier. Il permet de lancer un
        script directement avec `./mon_script.py` (après l'avoir rendu
        exécutable avec `chmod +x mon_script.py`). Il doit être sur la toute
        première ligne.

    # -*- coding: utf-8 -*-
        Indique l'encodage du fichier (la façon dont les caractères, comme les
        accents, sont stockés). Inutile en Python 3, où l'UTF-8 est déjà
        l'encodage par défaut, mais on le trouve dans du code ancien.

Enfin, des mots-clés comme TODO ("à faire"), FIXME ("à réparer") ou NOTE sont
souvent utilisés dans les commentaires pour signaler du travail restant :
    # TODO : gérer le cas où la liste est vide
Beaucoup d'éditeurs les mettent en couleur et permettent de les rechercher.
"""


# Bien commenter son code
##########################

# Bien commenter son code est souvent utile, mais rarement indispensable.
# En général, si on écrit du code clair et qui utilise des noms de variables et
# de fonctions explicites, on pourra (presque) se passer de commentaires.

# Commenter peut néanmoins être utile pour rappeler une difficulté que l'on a
# rencontrée en codant (et que l'on a peur d'oublier).

# Un bon commentaire explique POURQUOI le code fait quelque chose, pas CE QU'il
# fait (le code le dit déjà). Comparez (les variables seront vues au chap. 10) :

prix = 100
prix = prix * 1.2  # multiplie le prix par 1.2 (inutile : on le voit déjà !)
prix = 100
prix = prix * 1.2  # ajout de la TVA à 20 % (utile : explique le 1.2)
print(prix)  # => 120.0

# Enfin, un commentaire faux est pire que pas de commentaire du tout : quand
# vous modifiez du code, pensez à mettre à jour les commentaires qui
# l'accompagnent !
