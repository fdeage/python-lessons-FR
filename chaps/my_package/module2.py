################################################################################
#                                                                              #
#  Module d'exemple du package my_package (cf. chap. 22)                       #
#                                                                              #
################################################################################

"""
Second module du package my_package. Un module d'un package peut importer un
autre module du même package : ici, on réutilise module1.
"""

from my_package import module1


def another_function():
    """Retourne un message, en s'appuyant sur module1."""
    return "module2.another_function() utilise : " + module1.some_function()
