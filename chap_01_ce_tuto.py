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
#  Chap. 1      #  Utiliser ce tutoriel                                        #
#               #                                                              #
################################################################################
#
#  - Que faut-il ?
#  - Comment utiliser ce tutoriel ?
#  - Comment travailler ?
#  - Maîtriser son éditeur de texte
#
#####################################

# Que faut-il ?
################

"""
Ce tutoriel a vocation a être lu sur un ordinateur, pour pouvoir exécuter et
tester directement le code proposé. Il vous faut donc un ordinateur, idéalement
sous Linux, BSD ou Mac.

Le tutoriel est aussi pensé pour être ouvert depuis un éditeur de texte
proposant une coloration syntaxique (vim, Emacs, Sublime Text, PyCharm, VS
Code, Notepad++, gedit, etc.). Nous recommandons Sublime Text.

Nous rappelons que Microsoft Word n'est pas un éditeur de texte, mais un
éditeur de MISE EN FORME de texte. Vous ne pouvez pas vous en servir pour
écrire du code.

Les fichiers de ce cours sont exécutables, càd que vous pouvez les lancer avec
un interpréteur Python (voir le mode 2 plus haut) via la commande :
?> python ce_fichier.py

Enfin, tout ce cours utilise Python 3.6+ (c'est-à-dire la version 3, et au moins
la sous-version 6).
"""


# Comment utiliser ce tutoriel ?
#################################

"""
La meilleure façon est de lire le cours et de retaper le code proposé dans un
shell Python.

Cela semble long, mais c'est taper du code qui vous donnera de la pratique :
rapidité, fluidité et acquisition d'automatismes. À la fin de ce cours, les
meilleurs ne seront pas les plus doués, mais… ceux qui auront le plus pratiqué.

Taper les exemples dans une console vous permettra de vérifier les appels à
print(). Vous pourrez ensuite exécuter le fichier du cours pour comparer ce qui
est imprimé.

Note 1 : La fonction intégrée print() de Python permet d'afficher à l'écran le
résultat d'un calcul (voir chap. 7). Nous l'utiliserons dans tout ce cours.
Vous pouvez ainsi vérifier la plupart des calculs passés à print() : les
résultats des appels sont mis en commentaires en fin de ligne, après "=>" :
"""
print(1 + 2)             # => 3
print("abc")             # => abc
print(["une", "liste"])  # => ['une', 'liste']

"""
Note 2 : dans certains fichiers, des erreurs intentionnelles ont été laissées
dans le code. Elles sont signalées dans le code. On utilise un mécanisme de
gestion d'erreurs ("try … except …") pour empêcher ces erreurs
d'interrompre le programme. Ce mécanisme n'est pas à connaître au début : il
sera abordé en détail au chap. 26.
"""
try:
    1 / 0   # la division par 0 va créer une erreur…
except ZeroDivisionError as err:
    # … mais cette erreur est "interceptée" : le programme continue.
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Notez que les affichages d'erreurs sont numérotés : vous pourrez donc les
identifier plus tard dans la console.

Note 3 : les points importants sont notés "IMPT" et vous devez absolument les
connaître. Certains points ne sont pas indispensables, mais ils sont laissés
pour votre curiosité.
"""


# Comment travailler ?
#######################

"""
Vous aurez souvent besoin de vous repasser mentalement le "film" du programme,
pas à pas. Prenez l'habitude de simuler DANS VOTRE TÊTE son fonctionnement :

    - Identifiez le flux du programme : y a-t-il des conditionnels (chap. 12) ?
      des boucles (chap. 13) ? des appels de fonctions (chap. 14) ?
    - Déterminez la valeur de chaque variable utilisée à chaque ligne du
      programme, y compris pour des types construits (chap. 16-18).
    - Demandez-vous, à chaque appel de fonction, ce que valent ses paramètres :
      remplacez mentalement ses paramètres par les valeurs utilisées.
    - Après être passé dans la fonction, déterminez sa valeur de retour. Cette
      valeur est-elle conservée par la fonction appelante ?
    - Au besoin, modifiez le programme proposé : testez avec d'autres valeurs,
      d'autres combinaisons, et exécutez le nouveau programme. Testez, testez,
      testez !

Cela vous prendra beaucoup de temps et d'efforts au début, puis de moins en
moins. Un·e bon·ne programmeur·se doit pouvoir remplacer l'ordinateur et faire
"tourner" un programme de tête !

Concernant le cours : prenez l'habitude de piocher au cas par cas dans chaque
chapitre, en prenant ce dont vous avez besoin. N'hésitez pas à lire le cours en
diagonale, tester un morceau de code, puis revenir au cours pour revoir un
détail ou un exemple.

Python a beaucoup de fonctionnalités : n'essayez pas de tout apprendre tout de
suite, et concentrez-vous sur ce dont vous avez besoin. Vous apprendrez plus
vite et avec moins d'efforts.
"""


# Maîtriser son éditeur de texte
#################################

"""
Utiliser sa souris pour programmer est lent et inefficient : utilisez votre
clavier autant que possible !

Quel que soit l'éditeur que vous choisissez, il est indispensable de le
maîtriser. Par "maîtriser", on entend "pouvoir traiter toutes les tâches simples
de façon efficiente", ce qui implique de savoir le faire au clavier grâce à une
combinaison de touches. On appelle ces combinaisons des "raccourcis clavier".
Connaître beaucoup de raccourcis clavier fera de vous un.e meilleur.e
programmeur.se.

Vous devriez petit à petit avoir des raccourcis clavier pour TOUTES les tâches
suivantes :
-   déplacer le curseur en début/fin de mot,
-   déplacer le curseur en début/fin de ligne,
-   déplacer le curseur en début/fin de fichier,
-   supprimer le texte avant ou après le curseur jusqu'à la fin du mot,
-   supprimer le texte après le curseur jusqu'à la fin de la ligne,
-   déplacer verticalement une ligne ou un ensemble de ligne,
-   sélectionner du texte et étendre la sélection dans toutes les directions,
-   étendre une sélection jusqu'au curseur,
-   ajouter une sélection à la sélection courante,
-   faire une sélection multiple (avec plusieurs curseurs),
-   commenter/décommenter la sélection ou la ligne courante,
-   changer l'indentation d'un bloc de code (cf. chap. 12).
-   exécuter le code du fichier courant,
-   afficher/masquer la console pour voir les erreurs d'exécution,
-   rechercher du texte dans le fichier courant,
-   rechercher du texte dans un projet entier,
-   remplacer du texte par un autre texte, dans le fichier courant ou dans tout
    le projet.

C'est un minimum, vous êtes bien sûr invités à y ajouter vos propres raccourcis.

Plus vous maitriserez de raccourcis, plus vous serez rapides et vous prendrez
confiance en vous. L'objectif est de ne pas être limité par vos mains, mais par
votre vitesse de réflexion. Codez à la vitesse de votre pensée, pas de votre
souris !

Notez enfin que l'environnemet Jupyter n'offre pas autant de raccourcis qu'un
véritable éditeur : pour cette raison, il est peu pratique pour éditer du code
long et complexe, où il sera préférable d'utiliser votre éditeur.
"""
