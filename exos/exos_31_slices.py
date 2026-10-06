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
#  Chap. 31     #  Slices : exercices                                          #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", déroulez le programme dans votre
tête (cf. chap. 1) : écrivez d'abord les indices sous chaque élément.

Dans tout ce fichier (sauf mention contraire) :
    l = [10, 20, 30, 40, 50, 60, 70]

Les corrigés sont dans le fichier corr_31_slices.py.
"""


#############
#  Syntaxe  #
#############

"""
1. Sans exécuter, que valent :
       a) l[2:5]       b) l[:3]       c) l[4:]
       d) l[:]         e) l[1:6:2]    f) l[5:2]

2. Sans exécuter : combien d'éléments contient l[1:5] ? Et l[3:7] ? Donnez
   une formule générale pour le nombre d'éléments de l[debut:fin] (quand
   0 <= debut <= fin <= len(l)).
"""


#########################
#  Indexation négative  #
#########################

"""
3. Sans exécuter, que valent :
       a) l[-1]        b) l[-3:]      c) l[:-2]
       d) l[-5:-2]     e) l[1:-1]     f) l[-2:2]
"""


########################
#  Exemples de slices  #
########################

"""
4. Écrivez les slices qui donnent :
       a) les 3 premiers éléments de l,
       b) les 3 derniers,
       c) tous les éléments sauf le premier et le dernier,
       d) la première moitié de l (utilisez len() et "//"), puis la seconde.

5. Sans exécuter, lesquelles de ces expressions soulèvent une erreur ?
   Vérifiez (en protégeant ce qui doit l'être) :
       a) l[10]        b) l[5:100]    c) l[100:]

6. Écrivez une fonction apercu(liste, n) qui retourne les n premiers éléments
   de la liste, suivis de "…" si la liste contient plus de n éléments.
       apercu([1, 2, 3, 4, 5], 3)  =>  [1, 2, 3, '…']
       apercu([1, 2], 3)           =>  [1, 2]
"""


###################
#  Le pas (step)  #
###################

"""
7. Sans exécuter, que valent :
       a) l[::2]       b) l[1::3]     c) l[::-1]
       d) l[5:1:-2]    e) l[1:5:-1]

8. Avec nombres = list(range(1, 21)), calculez avec des slices et sum() :
       a) la somme des éléments d'indice pair (1 + 3 + 5 + …),
       b) la somme des éléments d'indice impair (2 + 4 + 6 + …).

9. Écrivez une fonction est_palindrome(phrase) qui retourne True si la phrase
   se lit dans les deux sens, en ignorant les majuscules et les espaces.
   Testez-la avec "Kayak" et "Esope reste ici et se repose".
"""


########################################
#  Modifier une liste avec les slices  #
########################################

"""
10. Avec jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"], et
    uniquement avec des slices (sans .insert(), .pop(), .remove()…) :
        a) remplacez "mardi" et "mercredi" par le seul élément "MILIEU",
        b) insérez "dimanche" au début de la liste,
        c) supprimez les deux derniers éléments.
    Affichez la liste après chaque étape.

11. Sans exécuter, que vaut x après chacune de ces lignes ?
        x = [1, 2, 3, 4, 5]
        x[1:3] = []
        x[:0] = [0]
        x[len(x):] = [6, 7]

12. Une string ne se modifie pas. À partir de mot = "chat", construisez avec
    des slices :
        a) "chut" (on remplace la 3e lettre),
        b) "chateau" (on ajoute à la fin),
        c) "tcha" (on déplace la dernière lettre au début ; "chat"[-1] vaut
           "t").
"""


###########################################
#  Slices avec d'autres types construits  #
###########################################

"""
13. Avec la string date_iso = "2024-03-15", extraisez avec des slices
    l'année, le mois et le jour (sans .split()), puis affichez la date au
    format 15/03/2024.

14. Sans exécuter, que valent :
        a) (1, 2, 3, 4)[1:3]
        b) "Bonjour"[::2]
        c) range(0, 100, 5)[3:6]
        d) list(range(0, 100, 5)[3:6])

15. On a capitales = {"France": "Paris", "Italie": "Rome",
    "Espagne": "Madrid"}. Pourquoi capitales[:2] ne fonctionne-t-il pas ?
    Affichez quand même les 2 premiers PAYS (cf. chapitre).
"""


####################################
#  Copie de séquences avec slices  #
####################################

"""
16. Sans exécuter, que valent a, b et c à la fin ?
        a = [1, 2, 3]
        b = a
        c = a[:]
        a.append(4)

17. Sans exécuter, que vaut m à la fin ? Pourquoi ?
        m = [[1, 2], [3, 4]]
        n = m[:]
        n[0].append(99)
        n[1] = "remplacé"
"""


##########################
#  Pour aller plus loin  #
##########################

"""
18. Écrivez une fonction rotation(liste, k) qui "fait tourner" la liste de k
    crans vers la gauche : rotation([1, 2, 3, 4, 5], 2) => [3, 4, 5, 1, 2].
    Que doit-il se passer si k est plus grand que la longueur de la liste ?

19. Écrivez une fonction paquets(liste, taille) qui découpe la liste en
    sous-listes de la taille donnée (la dernière peut être plus courte) :
        paquets([1, 2, 3, 4, 5, 6, 7], 3)  =>  [[1, 2, 3], [4, 5, 6], [7]]
"""
