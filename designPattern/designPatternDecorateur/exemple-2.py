"""
La syntaxe  @decorate_function  dit à l’interpréteur Python que cette fonction doit être décorée par la fonction décorateur  decorate_function  . 
Très concrètement, l’interpréteur Python va exécuter la fonction décorateur lors du lancement du code, et passer la fonction décorée en paramètre de son appel.
Exactement comme pour la première méthode. 
Ici la fonction garde le même nom, mais représente en fait le “wrapper” retourné par le décorateur. 
"""

def decorate_function(function):
    """Cette fonction va générer le décorateur."""
 
    def wrapper():
        """Le "vrai" décorateur."""
        print("Do something at the start")
        result = function()
        print("Do something at the end")
        return result
 
    return wrapper
 
 
@decorate_function  # c'est ici que ça se passe !
def travelling_through_the_stars():
    """Voyage à travers les étoiles."""
    print("C'est parti pour un long voyage !")
 
 
# la fonction est directement décorée, et s'utilise comme telle, comme si rien
# comme si rien n'avait changé ! ;)
travelling_through_the_stars()