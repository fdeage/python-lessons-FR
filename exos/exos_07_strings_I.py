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
#  Chap. 7      #  Strings I : exercices                                       #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les questions « sans exécuter », réfléchissez d'abord sur
papier, puis vérifiez avec l'interpréteur ou un print().

Les corrigés sont dans le fichier corrs/corr_07_strings_I.py.
"""


##########################
#  Déclarer des strings  #
##########################

"""
1. Sans exécuter : lesquelles de ces lignes provoquent une erreur de syntaxe ?
   Pourquoi ?
       a) 'Bonjour'
       b) "Il m'a dit bonjour"
       c) 'Il m'a dit bonjour'
       d) "Elle a crié "Stop !""
       e) 'Elle a crié "Stop !"'

2. Affichez avec print() la phrase suivante (apostrophe ET guillemets) :
       L'été sera "chaud"
   a) en écrivant la chaîne entre doubles quotes,
   b) puis entre simples quotes.
   Quels caractères faut-il échapper dans chaque cas ?

3. Sans exécuter : que valent ces comparaisons ?
       a) "abc" == 'abc'
       b) "abc" == "ABC"
       c) "" == " "
"""


############################
#  Accéder à un caractère  #
############################

"""
Pour les exercices 4 à 7, on pose : mot = "Python"

4. Sans exécuter : que valent mot[0], mot[5], mot[-1] et mot[-6] ?

5. Que se passe-t-il avec mot[6] ? Vérifiez en protégeant la ligne avec
   try: … except IndexError: … (comme dans le cours).

6. Donnez l'indice positif ET l'indice négatif de la lettre "h" dans mot.

7. a) Pourquoi l'instruction mot[0] = "J" provoque-t-elle une erreur ?
   b) Fabriquez quand même la chaîne "Jython" : créez une NOUVELLE chaîne en
      concaténant "J" et les caractères mot[1] à mot[5].
"""


########################################
#  Caractères spéciaux et échappement  #
########################################

r"""
8. Sans exécuter : que valent len("a\nb"), len("a\\nb") et len(r"a\nb") ?

9. Avec UN SEUL print(), affichez ces trois lignes :
       Nom : Lovelace
       Prénom : Ada
       Née en : 1815

10. Affichez le chemin Windows C:\Users\ana\notes.txt de deux façons :
    a) en doublant les backslashs,
    b) avec une chaîne brute (r"…").
    Pourquoi "C:\Users\ana\notes.txt" sans précaution serait-il dangereux ?
    (indice : relisez la liste des caractères spéciaux du cours)

11. Avec un seul print() et des tabulations, affichez ce petit tableau :
        Fruit    Prix
        Pomme    2
        Kiwi     3

12. Affichez le mot "Noël" en écrivant le "ë" avec son code Unicode : \u00eb.
"""


###########################
#  Imprimer avec print()  #
###########################

"""
13. Sans exécuter : qu'affichent ces lignes ?
        print("a", "b", "c", sep="")
        print("a", "b", sep=" - ", end="!\n")
        print(1, 2.5, True)

14. Avec DEUX print() et le paramètre end, affichez sur une seule ligne :
        Calcul en cours... terminé !

15. Avec un seul print() et le paramètre sep, affichez la date 05/10/2026 à
    partir des trois chaînes "05", "10" et "2026".
"""


###############################################
#  Opérations de base : len(), +, * et str()  #
###############################################

"""
16. Sans exécuter : que valent
        a) len("Bonjour")
        b) len(" ")
        c) "ab" + "cd"
        d) "ab" * 3
        e) "-" * 0 ?

17. Lesquelles de ces lignes provoquent une erreur ? Que valent les autres ?
        a) "3" + "4"
        b) "3" + 4
        c) "3" * 4
        d) "3" * "4"
        e) 3 * "ab"
    Vérifiez en protégeant les lignes qui échouent avec try: … except …

18. On pose : age = 17
    Construisez par concaténation la chaîne "J'ai 17 ans" et affichez-la.

19. On pose : mot = "Python"
    Affichez ce cadre autour du mot, en calculant la largeur avec len() (le
    cadre doit s'adapter tout seul si on change mot) :
        +--------+
        | Python |
        +--------+
"""


#################################################
#  Une première méthode : .upper() et .lower()  #
#################################################

"""
20. Sans exécuter : qu'affiche ce programme ? Pourquoi ?
        s = "Bonjour"
        s.upper()
        print(s)
    Corrigez-le pour qu'il affiche BONJOUR.

21. Écrivez une comparaison qui vaut True quand les chaînes "PyThOn" et
    "python" sont identiques SANS tenir compte des majuscules.
"""
