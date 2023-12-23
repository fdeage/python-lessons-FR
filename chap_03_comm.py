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
#  Chap. 3      #  Commentaires                                                #
#               #                                                              #
################################################################################
#
#  - Commentaires simples
#  - Commentaires longs et docstrings
#
######################################

# Commentaires simples
#######################

# Un commentaire de ligne commence par un dièse ou hashtag (#), souvent suivi
# d'une espace. On peut commenter une ligne de code en insérant un "#" au début.
# La ligne ne sera alors plus considérée comme du code, mais comme du texte.
# Elle ne sera plus exécutée.

# Ainsi, ce fichier de tutoriel est du code Python, mais toute la mise en
# forme du texte est réalisée avec des commentaires !

# Il peut être pratique de laisser du code sous forme commentée, pour pouvoir
# le décommenter plus tard si besoin.

# La plupart des éditeurs proposent un raccourci clavier pour commenter son
# code.

# Bien commenter son code est souvent utile, mais rarement indispensable.
# En général, si on écrit du code clair et qui utilise des noms de variables et
# de fonctions explicites, on pourra (presque) se passer de commentaires.

# Commenter peut néanmoins être utile pour rappeler une difficulté que l'on a
# rencontrée en codant (et que l'on a peur d'oublier).


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
