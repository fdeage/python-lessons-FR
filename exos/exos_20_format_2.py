################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.0.9        #
# ██   ██ ██                ██   ██    © Félix Déage - 2024                    #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 20     #  Formatage II : exercices                                    #
#               #                                                              #
################################################################################

"""
Les programmes à corriger sont dans des chaînes de caractères : recopiez-les
sous l'énoncé, puis corrigez-les. Le code corrigé doit faire EXACTEMENT la même
chose que le code d'origine : on ne change que la présentation (et les noms).
Quand un programme utilise des variables qui n'existent pas encore, créez-les
avec des valeurs de votre choix avant de l'exécuter.

Pour vérifier votre travail, vous pouvez installer un linter (cf. chap. 20 et
22) et le lancer sur ce fichier :
?> pip install ruff
?> ruff check exos_20_format_2.py

Les corrigés sont dans le fichier corr_20_format_2.py.
"""


##################################
#  Pourquoi formater son code ?  #
##################################

"""
1. Donnez trois raisons de respecter un style commun, même quand on programme
   seul·e.

2. Ces deux programmes font-ils la même chose ? Lequel préférez-vous relire
   dans six mois, et pourquoi ?

    a) def f(a,b):return a*b/2

    b) def aire_triangle(base, hauteur):
           return base * hauteur / 2
"""


########################
#  La PEP 8 : nommage  #
########################

"""
3. Renommez les variables et fonctions de ce programme selon la PEP 8 (noms
   parlants, snake_case pour les variables et les fonctions, MAJUSCULES pour
   les constantes) :

    Taux=0.2
    def CalculPrix(P,q):
        X=P*q
        return X*(1+Taux)
    print(CalculPrix(10,3))

4. Sans exécuter, quels noms ne respectent pas la PEP 8 ? Lesquels sont même
   interdits par Python (SyntaxError) ? Lesquels sont dangereux ?

    nombreEleves    nombre_eleves    NOMBRE_MAX    2eme_note    l
    note_moyenne    list             class         _total       Prix_TTC
"""


########################################
#  La PEP 8 : espaces et lignes vides  #
########################################

"""
5. Corrigez les espaces de ce programme (autour des opérateurs, après les
   virgules, dans les parenthèses, autour du "=" des arguments nommés…) :

    def aire( longueur,largeur ):
        return longueur*largeur
    resultat=aire(3 ,4)
    print( resultat )
    print("a","b",sep = "-")
    liste=[ 1,2 ,3 ]

6. Ajoutez les lignes vides nécessaires (combien avant et après une fonction ?)
   dans ce programme :

    import math
    def perimetre_cercle(rayon):
        return 2 * math.pi * rayon
    def aire_cercle(rayon):
        return math.pi * rayon ** 2
    print(perimetre_cercle(1))
    print(aire_cercle(1))
"""


####################################
#  La PEP 8 : longueur des lignes  #
####################################

"""
7. Cette ligne dépasse 79 caractères. Découpez-la de deux façons : avec des
   parenthèses, puis en passant par des variables intermédiaires.

    prix_total = prix_unitaire_hors_taxes * quantite_commandee * (1 + taux_de_tva) - remise_fidelite

8. Découpez cet appel de fonction trop long en mettant un argument par ligne
   (la fonction construire_message() est à écrire : elle colle ses quatre
   premiers arguments avec des espaces, puis ajoute la ponctuation) :

    message = construire_message("Bonjour", "Ada Lovelace", "votre commande n°1042", "est prête", ponctuation="!")

9. Découpez cette longue chaîne en plusieurs morceaux, sans antislash :

    avertissement = "Attention : ce programme supprime définitivement les fichiers temporaires du dossier courant."
"""


######################################################
#  La PEP 8 : imports, comparaisons et commentaires  #
######################################################

"""
10. Corrigez les imports de ce programme (place, ordre, un import par ligne,
    pas d'import *) :

    print("Début")
    import sys, os
    from math import *
    import random
    print(sqrt(16))

11. Corrigez les comparaisons :

    if est_connecte == True:
        print("ok")
    if resultat == None:
        print("rien")
    if not "x" in mot:
        print("pas de x")
    if (len(liste) == 0) == False:
        print("liste non vide")

12. Corrigez ou supprimez les commentaires inutiles, faux ou mal formatés :

    i = i + 1 # ajoute 1 à i
    #calcul de la TVA
    tva = prix * 0.055  # TVA à 20 %
    x = x * 1.1  # majoration de 10 % demandée par le client en 2023
"""


####################################
#  La PEP 20 : le "Zen of Python"  #
####################################

"""
13. Affichez le Zen of Python avec "import this". Choisissez trois aphorismes,
    et expliquez-les avec vos mots.

14. Lequel de ces deux codes respecte le mieux le Zen ? Citez l'aphorisme
    correspondant.

    a) for x in range(10): print(x) if x%2==0 and x%3!=0 or x==9 else None

    b) for x in range(10):
           est_pair_non_multiple_de_3 = x % 2 == 0 and x % 3 != 0
           if est_pair_non_multiple_de_3 or x == 9:
               print(x)
"""


#########################
#  Outils de formatage  #
#########################

"""
15. Quelle est la différence entre un linter (flake8, pylint, "ruff check")
    et un formatteur (black, "ruff format") ? Lequel des deux :
      a) signale une variable importée mais jamais utilisée ?
      b) remet les bons espaces autour des opérateurs ?
      c) ajoute les deux lignes vides avant une fonction ?
      d) signale un "== None" ?

16. Installez ruff (?> pip install ruff), puis lancez-le sur ce fichier :
        ?> ruff check exos_20_format_2.py
    Le code des énoncés étant dans des chaînes, ruff ne trouve rien. Copiez le
    programme de l'exercice 22 dans un fichier brouillon.py, et lancez :
        ?> ruff check brouillon.py
        ?> ruff format --diff brouillon.py
    Que signifie la ligne "--diff" ? Que fait la commande sans cette option ?

17. Dans un projet, on trouve ces lignes dans le fichier pyproject.toml :

        [tool.ruff]
        line-length = 100

    Qu'est-ce que cela change ? Pourquoi mettre ce réglage dans un fichier du
    projet plutôt que dans les réglages de son propre éditeur ?
"""


############################
#  Configurer son éditeur  #
############################

"""
18. Configurez votre éditeur pour :
      a) afficher une règle verticale à 79 (ou 88) caractères,
      b) afficher le whitespace (cf. chap. 5),
      c) insérer 4 espaces quand on appuie sur Tab,
      d) formater le fichier à chaque enregistrement.
    Notez où se trouve chacun de ces réglages.

19. Écrivez le contenu d'un fichier .editorconfig qui impose, pour tous les
    fichiers .py du projet : l'UTF-8, une indentation de 4 espaces, et une
    ligne vide à la fin du fichier.
"""


##########################
#  Automatiser avec git  #
##########################

"""
20. Qu'est-ce qu'un "hook" git ? Pourquoi est-il utile de lancer le
    formatteur juste avant chaque commit, plutôt que "quand on y pense" ?

21. Dans quel ordre faut-il taper ces commandes pour que ruff s'exécute
    à chaque commit ?
        a) ?> pre-commit install
        b) ?> pip install pre-commit
        c) créer le fichier .pre-commit-config.yaml
        d) ?> git commit -m "Mon message"
    Que se passe-t-il au moment de d) si un fichier est mal formaté ?
"""


#####################################
#  Synthèse : un programme complet  #
#####################################

"""
22. Reformatez entièrement ce programme selon la PEP 8. Il calcule et affiche
    la moyenne des notes au-dessus d'un seuil.

    import math,sys
    SEUIL=10
    def Moyenne(L,s = SEUIL) :
      t=0;n=0
      for x in L :
          if x>=s : t+=x;n+=1
      if n==0 :return None
      return t/n
    notes=[12,8,15,9,18]
    m=Moyenne(notes)
    if m!=None : print("Moyenne : "+str(round(m,2)))
"""
