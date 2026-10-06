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
#  Chap. 25     #  Les ensembles : exercices                                   #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", déroulez le programme dans votre
tête (cf. chap. 1) avant de vérifier.

Rappel : l'ordre d'affichage d'un ensemble n'est pas garanti. Pour comparer
vos résultats, affichez-les triés avec sorted() (cf. chap. 24).

Les corrigés sont dans le fichier corr_25_sets.py.
"""


#########################
#  Usage et propriétés  #
#########################

"""
1. Sans exécuter, que vaut chaque expression ?
       len({1, 2, 2, 3, 3, 3})
       len(set("mississippi"))
       type({})
       type(set())
       {1, 2, 3} == {3, 1, 2}
       len({1, True, 1.0})

2. Sans exécuter, lesquelles de ces lignes soulèvent une erreur ? Laquelle et
   pourquoi ? Vérifiez en protégeant chaque ligne avec try: … except …:.
       a = {(1, 2), "abc", 3.5}
       b = {[1, 2], 3}
       c = {1, 2, 3}[0]
       d = set([[1], [2]])

3. Créez un ensemble vide nommé lettres_vues, puis ajoutez-y une par une les
   lettres du mot "banane" avec une boucle for. Affichez sa taille et ses
   éléments triés.
"""


##################################
#  Opérations sur les ensembles  #
##################################

"""
4. Sans exécuter, que vaut s après chaque ligne ? Qu'affichent les print() ?
       s = {10, 20}
       s.add(30)
       s.add(10)
       s.update([40, 20, 50])
       s.discard(99)
       s.remove(50)
       print(len(s))
       print(25 in s, 25 not in s)

5. Quelle est la différence entre .remove() et .discard() ? Écrivez deux
   lignes qui le montrent (la première doit être protégée par un try).

6. Avec une compréhension d'ensemble (cf. chap. 23), créez l'ensemble des
   longueurs des mots de la phrase "le petit chat boit du lait chaud".
   Affichez-le trié.

7. Écrivez une fonction initiales(mots) qui retourne l'ensemble des premières
   lettres (en minuscules) d'une liste de mots.
       initiales(["Pomme", "poire", "Kiwi", "abricot"])  → {'p', 'k', 'a'}
"""


#########################################################
#  Cas d'usage : dédoublonner et tester l'appartenance  #
#########################################################

"""
8. Une liste d'adresses e-mail contient des doublons :
       emails = ["ana@mail.fr", "bob@mail.fr", "ana@mail.fr",
                 "chloe@mail.fr", "bob@mail.fr"]
   Affichez le nombre d'adresses différentes, puis la liste triée de ces
   adresses.

9. Écrivez une fonction a_des_doublons(liste) qui retourne True si la liste
   contient au moins un élément en double, False sinon (en une ligne, avec
   len() et set()).

10. Écrivez une fonction dedoublonner(liste) qui retourne une nouvelle liste
    sans doublons, mais en CONSERVANT l'ordre de première apparition :
        dedoublonner([3, 1, 3, 2, 1])  → [3, 1, 2]
    Indice : parcourez la liste en retenant dans un ensemble les éléments
    déjà vus.

11. On veut filtrer les "mots vides" d'une phrase :
        mots_vides = {"le", "la", "les", "de", "du", "un", "une", "et"}
        phrase = "le chat et la souris jouent dans le jardin de la maison"
    Construisez la liste des mots de la phrase qui ne sont pas des mots vides
    (dans l'ordre de la phrase). Pourquoi est-il judicieux que mots_vides soit
    un ensemble plutôt qu'une liste ?
"""


#################################
#  Exemple avec les anagrammes  #
#################################

"""
12. Sans exécuter, que retournent ces appels (fonctions du chapitre) ?
        ont_memes_lettres("ironique", "onirique")
        sont_anagrammes("ironique", "onirique")
        ont_memes_lettres("pas", "spa")
        ont_memes_lettres("papa", "pa")
        sont_anagrammes("papa", "pa")

13. Écrivez une fonction est_pangramme(phrase) qui retourne True si la phrase
    contient toutes les lettres de l'alphabet (en ignorant majuscules,
    espaces et ponctuation). Testez avec :
        "Portez ce vieux whisky au juge blond qui fume"   → True
        "Bonjour tout le monde"                           → False
    Indice : l'alphabet s'obtient avec set("abcdefghijklmnopqrstuvwxyz").
"""


#########################
#  Logique ensembliste  #
#########################

"""
On considère :
    a = {1, 2, 3, 4}
    b = {3, 4, 5}
    c = {1, 2}

14. Sans exécuter, que vaut chaque expression ?
        a & b
        a | b
        a - b
        b - a
        a ^ b
        c <= a
        c < c
        a >= b
        c.isdisjoint(b)

15. Deux amis listent les films qu'ils ont vus :
        films_ana = {"Alien", "Amélie", "Brazil", "Coco", "Dune"}
        films_bob = {"Brazil", "Dune", "Fargo", "Heat"}
    Affichez (triés) :
        a) les films qu'ils ont vus tous les deux,
        b) les films vus par au moins l'un des deux,
        c) les films que Bob pourrait conseiller à Ana,
        d) les films vus par un seul des deux.

16. Sans exécuter, que vaut x à la fin ?
        x = {1, 2, 3}
        x |= {3, 4}
        x &= {2, 3, 4, 5}
        x -= {4}

17. Écrivez une fonction competences_manquantes(requises, candidat) qui
    retourne la liste triée des compétences requises que le candidat n'a pas,
    et une fonction est_qualifie(requises, candidat) qui retourne True si le
    candidat a toutes les compétences requises (utilisez l'inclusion).
        requises = {"python", "sql", "git"}
        competences_manquantes(requises, {"python", "excel"})  → ['git', 'sql']
        est_qualifie(requises, {"git", "python", "sql", "java"})  → True
"""


############################
#  Bonus : les frozensets  #
############################

"""
18. Sans exécuter, lesquelles de ces lignes soulèvent une erreur ?
        f = frozenset("abc")
        f.add("d")
        g = f | {"d"}
        d = {f: "lettres"}
        e = {{1, 2}: "ensemble"}

19. On veut compter combien de paires d'amis différentes apparaissent dans
    une liste de rencontres, sachant que ("ana", "bob") et ("bob", "ana")
    désignent la même paire :
        rencontres = [("ana", "bob"), ("bob", "ana"), ("ana", "chloé"),
                      ("chloé", "ana"), ("bob", "chloé")]
    Indice : un frozenset ne tient pas compte de l'ordre, et peut être mis
    dans un ensemble.
"""
