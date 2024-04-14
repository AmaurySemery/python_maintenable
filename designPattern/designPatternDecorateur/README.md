En Python, les fonctions sont des objets comme les autres : elles peuvent donc être passées à d’autres fonctions et en sortir comme n’importe quelle autre valeur.

Le design pattern Décorateur fournit une façon de modifier une fonction, souvent en ajoutant des fonctionnalités avant et après son exécution.

Il peut être utile lorsque plusieurs fonctions similaires ont des fonctionnalités centrales différentes, mais des fonctionnalités partagées significatives.

Il peut aussi être utile lorsque vous ne souhaitez pas modifier le code interne d’une fonction, pour pouvoir la réutiliser de différentes manières.

La syntaxe  @decorate_function  simplifie l’écriture de code impliquant des décorateurs.