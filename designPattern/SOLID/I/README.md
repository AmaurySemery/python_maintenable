# Jeu de cartes

## Les versions

- 591cc67afd26bdaf9226f4ec58e185fb653f92bb : Ajout du jeu de cartes

La ségrégation des interfaces correspond au principe de responsabilité unique pour les interfaces.

Ce principe est facile à enfreindre. Il peut être tentant d’ajouter une nouvelle méthode à une interface existante, vu qu’elle fait déjà quelque chose.

En cas de doute, il vaut mieux avoir deux interfaces avec peu de méthodes à implémenter, qu’une seule interface qui ait trop de responsabilités.