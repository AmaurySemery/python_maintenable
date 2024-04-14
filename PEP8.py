"""Écrivez les noms de variables en minuscules, avec des underscores (tirets bas). 
C'est ce qu'on appelle la convention « snake_case » :"""

name = "Jeanne"
fuel_level = 100
famous_singers = ["Céline Dion", "Michael Jackson", "Edith Piaf"]

"""Écrivez les variables constantes en majuscules, avec des underscores :"""

DAYS_PER_WEEK = 7
PERSONAL_EMAIL = "myemail@email.com"

"""Écrivez les noms de classe avec une majuscule au début de chaque mot, sans ponctuation (la convention « CapitalizedCase ») :"""

class JukeBox:
    pass

class SpaceShip:
    pass

"""Écrivez les noms de modules en minuscules, en évitant au maximum l’utilisation des underscores :"""

import os
import sys
import shutil  # contraction de “sh” (langage bash) et “util”
import pathlib  # contraction de “path” et “lib”

"""Mettez les commentaires à jour lorsque le code change.

Évitez les commentaires sur la même ligne que le code, ils font négligé.

Mettez un seul espace entre le symbole dièse et le texte (pour différencier du code qui a été commenté).

Utilisez le même niveau d’indentation que la ligne de code qui suit, pour une bonne lisibilité :"""

# Commentaire correctement indenté
def foo(arg):
    # Commentaire correctement indenté
    pass

    # Commentaire mal indenté
def foo(arg):
# Commentaire mal indenté
    pass

# Bon code, selon la PEP 8.
def protect_animals(animals, sanctuary="little farm", max_places=4):
    """Place les animaux donnés dans un sanctuaire."""
    is_little = "little" in sanctuary
 
    if max_places < 5 or is_little:
        print("C'est petit, mais c'est mieux que rien !")
 
    protected = animals[:max_places]
    print(f"Nous avons protégés ces animaux : {protected}")
 
animals = ["cochon", "poule", "cerf", "lapin", "chien"]
protect_animals(animals)

# Mauvais code, selon la PEP 8.
def protect_animals(animals,sanctuary = "little farm",max_places = 4):
    is_little="little" in sanctuary
 
    if max_places<5 or(is_little):
        print( "C'est petit, mais c'est mieux que rien !" )
 
    protected=animals[ : max_places]
    print( f"Nous avons protégés ces animaux : { protected }" )
 
animals = [ "cochon","poule","cerf","lapin","chien" ]
protect_animals( animals )

"""
Mettez un seul espace autour des opérateurs d’affectation (  is_little = "little" in sanctuary  ) et des opérateurs logiques (  max_places  < 5  ). La seule exception intervient lorsque l’on fixe des valeurs par défaut en paramètres de fonctions et méthodes, telles que  max_places=4  .

Ne laissez jamais d’espaces tout de suite à l’intérieur de parenthèses ou de crochets. Écrivez  (expression)  et  [0]  , pas  ( expression )   ou  [ 0 ]  .

Ne laissez pas de blanc entre une fonction, comme  print()  , et ses arguments.

Laissez un espace entre  if  et toute parenthèse. La même règle s’applique à  for  . Ceci vise à être cohérent avec les situations où il n’y a pas de parenthèses.
"""

def my_function(parameter_number_1):
    print("bla")

# Aligne les paramètres sur la verticale
def function_with_a_rather_long_name(parameter_number_1, parameter_number_2,
                                     parameter_number_3):
    my_function(parameter_number_1)
    return parameter_number_2

# Même chose, mais avec un paramètre par ligne
def function_with_a_rather_long_name(parameter_number_1,
                                     parameter_number_2,
                                     parameter_number_3):
    my_function(parameter_number_1)
    return parameter_number_2

# Un paramètre par ligne, et la parenthèse au même niveau d’indentation que la fonction
def function_with_a_rather_long_name(
    parameter_number_1,
    parameter_number_2,
    Parameter_number_3
):
    my_function(parameter_number_1)
    return parameter_number_2

super_long_password = (
    "erfzfefrzvterbytnrezrtvbytyruetrgtrth"
    "zeergvzreafz'((-'eg'((yhvgbrz'trvytrh"
    "zerbetrtzbrtyezegbyebzrtbrebrtberbtrg"
    "zevrebtniukoy;i;yu,yt,trntehtrgegretr"
)