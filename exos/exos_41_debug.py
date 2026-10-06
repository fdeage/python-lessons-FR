################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.1.0        #
# ██   ██ ██                ██   ██    © Claude Opus 5.5 - 2026                #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 41     #  Débogage : exercices                                        #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Dans ce chapitre, beaucoup d'exercices consistent à TROUVER un bug :
appliquez la démarche du cours (reproduire, isoler, hypothèse, vérifier)
plutôt que de corriger au hasard. Copiez le code de l'énoncé sous l'énoncé,
puis déboguez-le.

Les corrigés sont dans le fichier corrs/corr_41_debug.py.
"""


#########################
#  Lire un traceback    #
#########################

"""
1. Voici un traceback :

       Traceback (most recent call last):
         File "/home/ada/rapport.py", line 18, in <module>
           afficher_rapport(ventes)
         File "/home/ada/rapport.py", line 12, in afficher_rapport
           print(f"Panier moyen : {panier_moyen(v):.2f}")
                                   ~~~~~~~~~~~~^^^
         File "/home/ada/rapport.py", line 5, in panier_moyen
           return v["total"] / v["nb_commandes"]
                  ~^^^^^^^^^
       KeyError: 'total'

   a) Quel est le type de l'erreur ? Que signifie le message ?
   b) Dans quel fichier, quelle fonction et à quelle ligne s'est-elle
      produite ?
   c) Dans quel ordre les fonctions ont-elles été appelées ?
   d) Formulez une hypothèse sur la cause du bug.

2. Le programme analyse.py contient, aux lignes 7 et 8 :

       villes = lire_villes("villes.csv").sort()
       print(villes[0])

   et produit ce traceback :

       Traceback (most recent call last):
         File "/home/ada/analyse.py", line 8, in <module>
           print(villes[0])
                 ~~~~~~^^^
       TypeError: 'NoneType' object is not subscriptable

   Que signifie le message ? La ligne 8 est-elle vraiment fautive ? Corrigez.
   (Indice : que renvoie la méthode .sort() ? cf. chap. 24)

3. Que signifient les messages d'erreur suivants ? Pour chacun, donnez une
   cause probable.
       a) NameError: name 'totl' is not defined
       b) TypeError: can only concatenate str (not "int") to str
       c) IndexError: list index out of range
       d) AttributeError: 'list' object has no attribute 'split'
       e) ValueError: invalid literal for int() with base 10: '12,5'
       f) TypeError: 'int' object is not callable

4. Écrivez une fonction diviser(a, b) qui renvoie a / b. Appelez-la avec
   b = 0 dans un bloc try/except, et affichez :
       - seulement la dernière ligne du traceback (avec le module traceback),
       - la liste des noms de fonctions traversées (avec extract_tb).
"""


###############################
#  Les trois familles de bugs #
###############################

"""
5. Pour chaque extrait, dites s'il contient une erreur de syntaxe, une
   erreur d'exécution ou une erreur de logique (sans exécuter) :

       a) prix = [12, 15, 9]
          print(prix[3])

       b) def aire_rectangle(longueur, largeur):
              return longueur + largeur

       c) for i in range(5)
              print(i)

       d) moyenne = sum([]) / len([])

       e) note = 15
          if note > 10:
              print("Recalé")

6. Pourquoi les erreurs de logique sont-elles les plus dangereuses ? Citez
   deux moyens de les détecter.
"""


##########################
#  Déboguer avec print() #
##########################

"""
7. Cette fonction doit calculer une moyenne pondérée (par exemple des notes
   avec des coefficients) : ((12 * 2) + (15 * 1)) / (2 + 1) = 13.0. Elle
   renvoie un mauvais résultat. Ajoutez des print(f"{…=}") pour trouver le
   bug, puis corrigez-le.

       def moyenne_ponderee(notes, coefs):
           total = 0
           for note, coef in zip(notes, coefs):
               total += note * coef
           return total / len(coefs)

       print(moyenne_ponderee([12, 15], [2, 1]))   # devrait afficher 13.0

8. Ce programme devrait afficher "Ville trouvée", mais il affiche "Ville
   inconnue". Utilisez repr() pour comprendre pourquoi, puis corrigez.

       ligne = "Paris\n"          # une ligne lue dans un fichier (chap. 28)
       villes_connues = ["Lyon", "Paris", "Lille"]
       if ligne in villes_connues:
           print("Ville trouvée")
       else:
           print("Ville inconnue")

9. Ce programme devrait afficher le prix le plus élevé (100), mais il
   affiche 9. Trouvez la cause en affichant les types, puis corrigez.

       prix = ["9", "100", "25"]     # lus dans un fichier CSV
       print(max(prix))
"""


#############################
#  assert comme garde-fou   #
#############################

"""
10. Écrivez une fonction pourcentage(partie, total) qui renvoie le
    pourcentage partie / total * 100, arrondi à 1 décimale. Ajoutez deux
    assert avec un message clair : total doit être strictement positif, et
    partie doit être comprise entre 0 et total. Testez avec (3, 12), puis
    avec (15, 12) dans un try/except.

11. Une fonction lit l'âge saisi par un utilisateur. Faut-il vérifier qu'il
    est positif avec un assert ou avec un raise ValueError ? Pourquoi ?
"""


###################################
#  Cas minimal et bisection       #
###################################

"""
12. Ce programme affiche un total faux (le total devrait être 45). Réduisez-le
    au plus petit programme possible qui montre encore le bug, puis
    expliquez le bug.

        import math
        donnees = {"lundi": "12", "mardi": "15", "mercredi": "18"}
        jours = list(donnees.keys())
        print("Nombre de jours :", len(jours))
        total = 0
        for jour in jours:
            valeur = donnees[jour]
            print("Traitement de", jour.upper())
            total = total + int(valeur) if jour != "mercredi" else total
        print("Racine du total :", math.sqrt(total))
        print("Total :", total)

13. On cherche un bug par bisection dans un programme de 1000 lignes. À
    chaque étape, on divise la zone suspecte par deux.
    a) Combien d'étapes faut-il au maximum pour trouver la ligne fautive ?
    b) Et pour un programme de 1 000 000 de lignes ?
    c) Écrivez une petite boucle qui calcule ces deux nombres.
"""


######################
#  Le débogueur pdb  #
######################

"""
14. Quelle commande pdb utiliser pour :
    a) afficher la valeur de la variable total ?
    b) exécuter la ligne courante sans entrer dans la fonction qu'elle
       appelle ?
    c) entrer dans la fonction appelée par la ligne courante ?
    d) reprendre l'exécution jusqu'au prochain point d'arrêt ?
    e) afficher la pile d'appels ?
    f) quitter ?

15. Voici une session pdb sur une fonction qui doit compter les mots de plus
    de 3 lettres. Quel est le bug ?

        > /home/ada/mots.py(4)compter_longs()
        -> breakpoint()
        (Pdb) l
          1     def compter_longs(mots):
          2         compte = 0
          3         for mot in mots:
          4  ->         breakpoint()
          5             if len(mot) > 3:
          6                 compte += 1
          7             return compte
        (Pdb) p mots
        ['chat', 'souris', 'ours']
        (Pdb) n
        > /home/ada/mots.py(5)compter_longs()
        -> if len(mot) > 3:
        (Pdb) n
        > /home/ada/mots.py(6)compter_longs()
        -> compte += 1
        (Pdb) n
        > /home/ada/mots.py(7)compter_longs()
        -> return compte
        (Pdb) n
        --Return--
        > /home/ada/mots.py(7)compter_longs()->1
        -> return compte
        (Pdb) p compte
        1

16. a) Que fait la commande : PYTHONBREAKPOINT=0 python3 analyse.py ?
    b) Votre programme analyse.py plante sur une erreur. Quelle commande
       permet d'ouvrir pdb au moment du plantage, pour inspecter les
       variables ?
    c) Pourquoi ne faut-il jamais laisser un breakpoint() dans un programme
       que l'on livre ?
"""


###################################
#  Les bugs classiques            #
###################################

"""
17. Sans exécuter, qu'affiche ce programme ? Corrigez la fonction pour que
    chaque appel sans liste reparte d'une liste vide.

        def ajouter_ville(ville, liste=[]):
            liste.append(ville)
            return liste

        print(ajouter_ville("Lyon"))
        print(ajouter_ville("Nantes"))
        print(ajouter_ville("Brest", ["Rennes"]))
        print(ajouter_ville("Nice"))

18. Ce code doit supprimer les mots vides (de longueur 0) d'une liste.
    Sans exécuter, qu'affiche-t-il ? Corrigez-le de deux façons.

        mots = ["le", "", "", "chat", "", "dort"]
        for mot in mots:
            if mot == "":
                mots.remove(mot)
        print(mots)

19. Cette fonction doit renvoyer la liste des températures de la semaine
    (les 7 dernières valeurs d'une liste). Trouvez l'erreur "off-by-one" et
    corrigez-la.

        def derniere_semaine(temperatures):
            return temperatures[len(temperatures) - 6:]

        print(derniere_semaine([10, 11, 12, 13, 14, 15, 16, 17, 18]))
        # devrait afficher [12, 13, 14, 15, 16, 17, 18]

20. Sans exécuter, qu'affiche ce programme ? Corrigez-le.

        def appliquer_remise(prix, taux):
            nouveau_prix = prix * (1 - taux)

        prix_final = appliquer_remise(100, 0.2)
        print(prix_final)

21. Ce programme plante à la dernière ligne. Pourquoi ? Corrigez-le.

        list = ["a", "b", "c"]
        print(len(list))
        lettres = list("abc")

22. (Problème) Cette fonction analyse des ventes : elle doit renvoyer un
    dictionnaire avec le total des ventes, la meilleure vente et le nombre
    de ventes supérieures à 100 €. Elle contient TROIS bugs. Trouvez-les avec
    la méthode de votre choix (print, assert, débogueur…), corrigez-les,
    puis écrivez des assert qui vérifient le résultat attendu :
        {'total': 450.0, 'meilleure': 200.0, 'nb_grosses': 1}

        def analyser_ventes(ventes):
            total = 0
            meilleure = 0
            nb_grosses = 0
            for vente in ventes:
                montant = vente
                total = montant
                if montant > meilleure:
                    meilleure = montant
                if montant >= 100:
                    nb_grosses += 1
            return {"total": total, "meilleure": meilleure,
                    "nb_grosses": nb_grosses}

        print(analyser_ventes(["50", "200", "100", "100"]))
"""
