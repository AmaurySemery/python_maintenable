Tout code appelant des méthodes sur des objets d’un type spécifique doit continuer à fonctionner lorsque ces objets sont remplacés par des instances d’un sous-type.

Qu’est-ce qu’un sous-type ?

Un sous-type peut être soit une classe qui étend une autre classe, soit une classe qui implémente une interface.

Le principe de substitution de Liskov s’applique aux hiérarchies d’héritage. Il est enfreint lorsqu’une classe dérivée ne peut pas prendre la place d’une classe de base sans casser le système.

Pour vous assurer de ne pas enfreindre cette règle, essayez de penser d’abord aux abstractions/interfaces de haut niveau, avant d’envisager les implémentations de bas niveau/concrètes.