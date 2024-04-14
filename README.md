https://peps.python.org/pep-0008/
https://peps.python.org/pep-0257/
https://peps.python.org/pep-0008/#id51

Les variables, classes et modules doivent porter des noms utiles et écrits selon le style suggéré.

Les commentaires doivent être utilisés avec modération, maintenus à jour, et indentés de la même façon que la ligne de code suivante.

Les docstrings sont des commentaires spéciaux, auxquels on peut accéder avec  __doc__  .

À l’inverse des commentaires, usez et abusez des docstrings 

Pour que le code Python soit cohérent et facile à lire, la PEP a différentes recommandations sur la présentation du code.

Le code doit être indenté avec 4 espaces (et non des tabulations).

Le code doit utiliser des espaces et sauts de lignes adaptés pour aérer le code sans trop le gonfler.

Les lignes de code ne doivent pas excéder 79 caractères, et il faut être prudent si l’on découpe de longues expressions en plusieurs lignes.

Les fichiers doivent être écrits en commençant par les commentaires qui concernent le fichier, puis les imports, puis les constantes, et ensuite tout le reste du code.

La PEP 8 comprend différentes recommandations de programmation pour vous aider à écrire du code antibug.

Les fonctions doivent retourner un seul type (entier, chaîne, booléen, etc.) et/ou None.

On préfère  str.startswith  et  str.endswith  au tranchage de chaînes, car vous n’avez qu’un élément de votre code à changer lorsque vous les modifiez.

Les blocs try doivent être placés de façon à couvrir le moins de code possible.

Les clauses except doivent toujours attraper un type spécifique d’exception.

Les linters sont des outils automatisés qui vous préviennent lorsque votre code n’est pas conforme à la PEP 8.

Les linters ne trouveront pas toutes vos erreurs de programmation, mais uniquement les principales recommandations de style de la PEP 8.