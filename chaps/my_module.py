################################################################################
#                                                                              #
#  Module d'exemple qui accompagne le chap. 22 (Modules, packages et import)   #
#                                                                              #
################################################################################

"""
Ce fichier est un module Python tout à fait ordinaire : n'importe quel fichier
.py peut être importé depuis un autre fichier situé dans le même dossier, avec
"import my_module" (sans l'extension ".py").

Tout ce qui est défini ici (variables, fonctions…) devient accessible avec la
syntaxe my_module.<nom>.
"""

# Une variable du module (ici une constante, en majuscules, cf. chap. 20)
VERSION = "1.0"


def my_function():
    """Retourne un message de salutation (exemple de fonction de module)."""
    return "Bonjour depuis my_module !"


def doubler(nombre):
    """Retourne le double de nombre."""
    return nombre * 2


# Ce code est exécuté UNE SEULE FOIS, au premier import du module
print("(my_module est en train d'être importé)")

# Le bloc ci-dessous n'est exécuté que si on lance CE fichier directement
# (?> python my_module.py), et pas quand on l'importe : cf. chap. 22,
# "Le nom __name__"
if __name__ == "__main__":
    print("my_module a été lancé directement, et non importé.")
    print(my_function())
