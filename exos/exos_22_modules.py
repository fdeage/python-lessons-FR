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
#  Chap. 22     #  Modules : exercices                                         #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", déroulez le programme dans votre
tête (cf. chap. 1) avant de vérifier.

N'utilisez que la bibliothèque standard de Python (rien à installer), sauf
mention contraire. Les corrigés sont dans le fichier corr_22_modules.py.
"""


####################
#  Fonctionnement  #
####################

"""
1. Qu'est-ce qu'un module ? Quelle est la différence entre une fonction
   intégrée (comme len()) et une fonction d'un module (comme math.sqrt()) ?

2. Sans exécuter, quelle erreur provoque ce programme, et pourquoi ?
   Corrigez-le.
       print(math.floor(3.7))
       import math
"""


#######################################
#  Les différentes façons d'importer  #
#######################################

"""
3. Calculez la racine carrée de 81 de quatre façons différentes :
     a) avec "import math"
     b) avec "import math as m"
     c) avec "from math import sqrt"
     d) avec "from math import sqrt as racine"

4. Sans exécuter, après chacune de ces lignes (prises séparément, dans un
   programme neuf), lesquels de ces noms sont utilisables : math, pi,
   math.pi, m, m.pi ?
     a) import math
     b) from math import pi
     c) import math as m

5. Sans exécuter, qu'affiche ce programme ? Quel est le problème ?
       from math import *
       print(pow(2, 3))
   Indice : la fonction intégrée pow(2, 3) retourne l'entier 8, mais
   math.pow(2, 3) retourne toujours un float.
"""


############################
#  Conventions de nommage  #
############################

"""
6. Remettez ces imports dans l'ordre recommandé par la PEP 8 (cf. chap. 20),
   et donnez les alias usuels de numpy et pandas :
       import pandas
       import my_module
       import sys
       import numpy
       import math
"""


##########################################
#  Explorer un module : help() et dir()  #
##########################################

"""
7. Avec dir(), affichez la liste des noms du module math. Combien de noms
   contient-elle ? Affichez uniquement ceux qui commencent par "is" (boucle et
   .startswith(), cf. chap. 8).

8. Affichez la documentation de la fonction math.hypot() sans utiliser help()
   (qui bloque le programme en attendant qu'on appuie sur "q"). Que calcule
   cette fonction ? Utilisez-la pour calculer l'hypoténuse d'un triangle
   rectangle de côtés 3 et 4.
"""


################################
#  Écrire ses propres modules  #
################################

"""
9. Le fichier my_module.py se trouve à la racine du cours, et non dans le
   dossier exos/. Pourquoi "import my_module" échoue-t-il quand on lance
   python3 exos/exos_22_modules.py ? Ajoutez le dossier parent à sys.path,
   puis importez my_module et utilisez sa fonction doubler() et sa variable
   VERSION.
   Indice : os.path.abspath(__file__) donne le chemin complet du fichier en
   cours, et os.path.dirname() le dossier qui le contient.

10. Sans exécuter, qu'affiche "import my_module" ? Et la commande
    ?> python3 my_module.py ? Expliquez le rôle de :
        if __name__ == "__main__":

11. Un élève crée un fichier random.py pour tester le module random, et y
    écrit "import random" puis "print(random.randint(1, 6))". Le programme
    plante avec une AttributeError. Pourquoi ?
"""


#########################
#  Modules et packages  #
#########################

"""
12. Quelle est la différence entre un module et un package ? À quoi sert le
    fichier __init__.py ?

13. Appelez la fonction some_function() du module module1 du package
    my_package de trois façons différentes. Affichez aussi la variable
    NOM_DU_PACKAGE, définie dans __init__.py.
"""


####################################
#  Installer des paquets externes  #
####################################

"""
14. Remettez ces commandes dans l'ordre pour créer un environnement virtuel,
    y installer pandas, puis sauvegarder la liste des paquets installés :
      a) ?> python3 -m pip install pandas
      b) ?> source .venv/bin/activate
      c) ?> python3 -m pip freeze > requirements.txt
      d) ?> python3 -m venv .venv
    Avec quelle commande un·e collègue installera-t-il·elle les mêmes paquets ?

15. Écrivez un import "protégé" de numpy : si numpy n'est pas installé, le
    programme affiche "numpy n'est pas installé : python3 -m pip install
    numpy" au lieu de planter.
"""


######################
#  Le module random  #
######################

"""
16. Simulez 10 lancers d'un dé à 6 faces avec randint(), et affichez-les sur
    une ligne. Fixez la graine à 1 avec seed(1) avant les lancers : relancez
    le programme, qu'observez-vous ?

17. Avec seed(2), simulez 6000 lancers de dé, et comptez combien de fois
    chaque face sort (dans une liste de 6 compteurs). Les résultats sont-ils
    proches de 1000 ?

18. Avec les fonctions de random :
      a) tirez au sort un élève dans la liste ["Ada", "Alan", "Grace",
         "Linus"] ;
      b) tirez 6 numéros différents entre 1 et 49 (loto) ;
      c) mélangez une copie de la liste d'élèves (avec list(), cf. chap. 17)
         pour faire un ordre de passage, sans modifier la liste d'origine.

19. Sans exécuter, quelle valeur peut retourner randrange(0, 10, 2) ? Et
    randint(0, 10) ?
"""


###################
#  Le module sys  #
###################

"""
20. Affichez la version de Python, et vérifiez avec sys.version_info qu'elle
    est au moins 3.6.

21. Écrivez un programme qui additionne tous les nombres passés en paramètre
    sur la ligne de commande :
        ?> python3 exos/exos_22_modules.py 4 5 6
    doit afficher 15. Sans paramètre, il affiche 0. (Rappel : les paramètres
    sont des strings, et sys.argv[0] est le nom du programme.)
"""


##################################################
#  D'autres modules de la bibliothèque standard  #
##################################################

"""
22. Avec le module statistics, calculez la moyenne, la médiane et l'écart-type
    de ces notes : [8, 12, 15, 10, 18, 12].

23. Avec collections.Counter, trouvez les 3 lettres les plus fréquentes de la
    phrase "le python est un langage de programmation" (sans compter les
    espaces).

24. Avec le module json, transformez ce dictionnaire en texte, puis
    retransformez le texte en dictionnaire. Les deux dictionnaires sont-ils
    égaux ?
        eleve = {"nom": "Ada", "notes": [15, 18], "inscrit": True}

25. Avec timeit, comparez la durée de 10 000 exécutions de "sum(range(1000))"
    et de la même somme faite avec une boucle "for". Laquelle est la plus
    rapide ?
"""
