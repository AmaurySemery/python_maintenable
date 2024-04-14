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