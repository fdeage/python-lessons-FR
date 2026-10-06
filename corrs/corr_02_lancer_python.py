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
#  Chap. 2      #  Lancer Python : corrigés                                    #
#               #                                                              #
################################################################################

##################################
#  Via l'interpréteur Python     #
##################################

"""
1. Comment lancer l'interpréteur ? Quelle version ?
    La commande dépend de votre système : `python3` sur Linux/macOS (où
    `python` désigne parfois encore Python 2), `python` ou `py` sur Windows.
    La version s'affiche sur la première ligne, par exemple :
        Python 3.12.3 (main, …) [GCC 13.2.0] on linux
    On peut aussi la demander sans lancer l'interpréteur :
        > python3 --version
    Si la version commence par 2, ce n'est PAS la bonne : utilisez python3.

2. Comment reconnaître l'interpréteur Python ?
    À son prompt ">>> ". Le shell de l'ordinateur a un prompt différent
    (souvent "$" ou ">", précédé du dossier courant).
    Le prompt "..." indique que l'interpréteur attend la SUITE d'une
    instruction sur plusieurs lignes (un bloc "if", une fonction…).

3. Que s'affiche-t-il ?
        >>> 7 * 6
        42
        >>> print(7 * 6)
        42
        >>> "bonjour"
        'bonjour'
        >>> print("bonjour")
        bonjour
    Dans l'interpréteur, une expression tapée seule est affichée
    automatiquement, sous sa forme de "représentation" : les chaînes de
    caractères apparaissent donc AVEC leurs guillemets. print(), lui, affiche
    le texte lui-même, SANS guillemets.

4. Comment quitter l'interpréteur ?
    - avec quit() (ou exit()),
    - avec Ctrl + D sur Linux/macOS, ou Ctrl + Z puis Entrée sur Windows.

5. Comment sortir de help(print) ?
    En appuyant sur la touche "q" (pour "quit").
"""

##########################################
#  En lançant un fichier depuis le shell #
##########################################

"""
6. Le fichier bonjour.py contient une seule ligne :
        print("Bonjour, je m'appelle Camille !")
   On l'exécute en se plaçant dans son dossier, puis :
        > python3 bonjour.py
        Bonjour, je m'appelle Camille !
"""
# La même instruction, exécutée ici :
print("Bonjour, je m'appelle Camille !")  # => Bonjour, je m'appelle Camille !

"""
7. Lancé depuis un autre dossier, on obtient une erreur du type :
        python3: can't open file '/home/moi/bonjour.py': [Errno 2] No such
        file or directory
   Python cherche le fichier dans le dossier COURANT du terminal. Deux
   solutions :
       - se déplacer dans le bon dossier :  > cd /home/moi/cours
       - donner le chemin complet :         > python3 /home/moi/cours/bonjour.py

8. L'option -i exécute le fichier, PUIS ouvre l'interpréteur interactif au
   lieu de quitter : on peut alors continuer à taper du code et inspecter ce
   que le programme a calculé.

9. Ce fichier ne contient presque que des chaînes entre triples guillemets et
   des commentaires : Python les lit mais n'affiche rien. Le fichier d'énoncés
   n'affiche donc RIEN (il se termine sans erreur, c'est tout).
"""


#####################################
#  Mode interactif vs fichier       #
#####################################

"""
10. Lancé comme un FICHIER, le programme n'affiche que les résultats des
    print() :
        5
        Python
    Les lignes `10 + 5` et `"Python"` sont calculées, puis oubliées.

    Dans l'INTERPRÉTEUR, les quatre lignes affichent quelque chose :
        >>> 10 + 5
        15
        >>> print(10 - 5)
        5
        >>> "Python"
        'Python'
        >>> print("Python")
        Python
"""

# 11. Les quatre lignes recopiées : seules deux d'entre elles affichent.
10 + 5
print(10 - 5)  # => 5
"Python"
print("Python")  # => Python

# 12. Pour tout afficher depuis un fichier, on ajoute print() partout :
print(10 + 5)  # => 15
print(10 - 5)  # => 5
print("Python")  # => Python
print("Python")  # => Python
"""
Notez qu'on ne retrouve pas les guillemets de 'Python' : pour les voir, il
faudrait afficher la "représentation" de la chaîne avec repr() (cf. chap. 7) :
"""
print(repr("Python"))  # => 'Python'


##########################################
#  Éditeurs, notebooks et sites Web      #
##########################################

"""
13. Exemples de raccourcis pour exécuter le fichier courant :
        - Sublime Text : Ctrl + B (Cmd + B sur macOS)
        - VS Code (extension Python) : bouton ▷ en haut à droite, ou
          Ctrl + F5 (exécuter sans débogage)
        - PyCharm : Maj + F10
    Si le raccourci n'existe pas, créez-le : vous l'utiliserez des centaines
    de fois.

14. La seconde cellule affiche 3, et non 11 : la cellule `x = 10` a été
    MODIFIÉE mais pas RÉEXÉCUTÉE, donc x vaut toujours 2 en mémoire.
    Dans un notebook, c'est l'ORDRE D'EXÉCUTION des cellules qui compte, pas
    leur ordre d'apparition à l'écran. En cas de doute : "Restart & Run All".

15. Site Web :
        + rien à installer, accessible depuis n'importe quel ordinateur,
          partage facile ;
        - nécessite une connexion Internet, votre code est stocké chez un
          tiers, et l'installation de certains paquets peut être limitée.
"""
