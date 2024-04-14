"""
Donc, dans notre exemple, notre fonction de voyage ne contiendra plus que le code propre au voyage, mais les procédures de décollage et d’atterrissage seront reléguées dans la fonction “wrapper” du décorateur.
"""

def decorate_function(function):
    """Cette fonction va générer le décorateur."""
 
    def wrapper():
        """Voici le "vrai" décorateur.
 
        C'est ici que l'on change la fonction de base
        en rajoutant des choses avant et après.
        """
        print("Do something at the start")
 
        result = function()
 
        print("Do something at the end")
 
        return result
 
    return wrapper
 
 
def travelling_through_the_stars():
    """Voyage à travers les étoiles."""
    print("C'est parti pour un long voyage !")
 
 
# ici, nous allons récupérer le retour de "decorate_function",
# qui n'est autre que la fonction "wrapper" !
# Notez que nous pouvons très bien renommer une fonction en
# l'assignant dans une nouvelle variable (ici "wrapper" devient "decorated").
decorated = decorate_function(travelling_through_the_stars)
decorated()  # nous executons la fonction "wrapper"