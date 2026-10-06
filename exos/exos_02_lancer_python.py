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
#  Chap. 2      #  Lancer Python : exercices                                   #
#               #                                                              #
################################################################################

"""
Ces exercices se font surtout DANS UN TERMINAL : lisez l'énoncé, essayez, puis
notez votre réponse en commentaire sous l'énoncé. Quand un exercice demande du
code, écrivez-le directement dans ce fichier et exécutez-le pour vérifier.

Les corrigés sont dans le fichier corrs/corr_02_lancer_python.py.
"""


##################################
#  Via l'interpréteur Python     #
##################################

"""
1. Ouvrez un terminal et lancez l'interpréteur Python. Quelle commande avez-vous
   utilisée (python, python3 ou py) ? Quelle version de Python s'affiche ?

2. Comment reconnaît-on qu'on est dans l'interpréteur Python et non dans le
   shell de l'ordinateur ? Que signifie le prompt "..." ?

3. Dans l'interpréteur, tapez successivement :
       >>> 7 * 6
       >>> print(7 * 6)
       >>> "bonjour"
       >>> print("bonjour")
   Notez ce qui s'affiche pour chaque ligne. Quelle différence voyez-vous
   entre la 3e et la 4e ligne ?

4. Comment quitte-t-on l'interpréteur ? Donnez deux façons de faire.

5. Dans l'interpréteur, tapez help(print). Comment sort-on de l'aide ?
"""


##########################################
#  En lançant un fichier depuis le shell #
##########################################

"""
6. Créez un fichier bonjour.py (dans le dossier de votre choix) qui affiche
   "Bonjour, je m'appelle <votre prénom> !". Quelle commande tapez-vous dans
   le terminal pour l'exécuter ?

7. Placez votre terminal dans un AUTRE dossier, puis relancez bonjour.py.
   Quelle erreur obtenez-vous ? Comment la corriger (deux solutions) ?

8. Que fait l'option -i dans la commande `python -i bonjour.py` ?

9. Exécutez CE fichier (exos_02_lancer_python.py) depuis le terminal.
   Qu'est-ce qui s'affiche ? Pourquoi ?
"""


#####################################
#  Mode interactif vs fichier       #
#####################################

"""
10. Sans exécuter : qu'affichera ce programme s'il est lancé comme un FICHIER
    (`python programme.py`) ? Et si on tape ces lignes une à une dans
    l'interpréteur ?
        10 + 5
        print(10 - 5)
        "Python"
        print("Python")

11. Recopiez les quatre lignes de l'exercice 10 ci-dessous, sans les
    commentaires, puis exécutez ce fichier pour vérifier votre réponse.

12. Modifiez les lignes de l'exercice 11 pour que les QUATRE résultats
    s'affichent quand on exécute le fichier.
"""


##########################################
#  Éditeurs, notebooks et sites Web      #
##########################################

"""
13. Dans votre éditeur de texte, trouvez le raccourci clavier qui exécute le
    fichier courant. Notez-le ici.

14. Dans un notebook Jupyter, on exécute une cellule contenant `x = 2`, puis
    une cellule contenant `print(x + 1)`, puis on modifie la première cellule
    en `x = 10` SANS la réexécuter, et on réexécute la seconde.
    Qu'affiche-t-elle ?
    Pourquoi est-ce un piège ?

15. Citez un avantage et un inconvénient d'un site Web (Replit, Google Colab…)
    par rapport à une installation de Python sur votre ordinateur.
"""
