L’acronyme STUPID désigne ces éléments :

Singleton.

Couplage fort (« Tight coupling »).

Non-testabilité (« Untestability »).

Optimisation prématurée (« Premature optimization »).

Nommage non descriptif (« Indescriptive naming »).

Duplication.

Les approches STUPID conduisent à des conceptions de codage difficiles à maintenir et à tester.


# Que désigne le « S » ? Le Singleton
Un Singleton est un objet qui garantit d’être la seule instance de son type ! Si vous en avez un, vous ne pouvez pas en créer un deuxième.

Le Singleton est considéré à la base comme un design pattern spécifique (encore un !). Cependant, étant très controversé, il finit par être considéré comme un “anti-pattern”, soit une erreur d’implémentation.

Il est difficile d’écrire des tests unitaires pour un Singleton (voir U pour Untestability – non-testabilité – ci-dessous).

On ne peut pas sous-classer un Singleton.

Il casse le O de SOLID – si les exigences changent et qu’il vous faut en fait une autre instance d’un Singleton, vous devrez modifier tout le code qui dépend du fait qu’il soit unique.

Pour les situations où le Singleton est utile, il existe d’autres solutions plus SOLID.

# Que désigne le « T » ? « Tight Coupling » (le couplage fort)
Le couplage fort se produit lorsque deux classes (ou modules) dépendent tellement l’une de l’autre que si vous apportez des modifications à l’une, vous devez souvent apporter des modifications à l’autre.

C'est ce qui rend votre code moins réutilisable (car vous devez également réutiliser tous les éléments qui accompagnent chaque classe fortement couplée), et en conséquence directe, plus difficile à tester.

# Que désigne le « U » ? « Untestability » (la non-testabilité)
Une classe peut être difficile ou impossible à tester pour de nombreuses raisons. Mais on en revient le plus souvent à un problème de couplage fort avec un autre composant. Si une classe a besoin de nombreuses dépendances pour fonctionner correctement, ça indique qu’il faut la réécrire. Le fait de tester un composant peut également être compliqué s’il viole la responsabilité unique et fait trop de choses.

# Que désigne le « P » ? « Premature Optimization » (l’optimisation prématurée)
L’optimisation prématurée désigne le fait de gérer un problème que l’on anticipe bien avant qu’il ne devienne un problème.

L’optimisation prématurée prend du temps et complexifie le code. Il se peut même que cette implémentation ne serve pas ! À l’inverse, l’acronyme YAGNI (you ain't gonna need it, ou “vous n’en aurez pas besoin”), conseille d’aller au plus simple, et de n’ajouter que les fonctionnalités qui sont absolument nécessaires.

# Que désigne le « I » ? « Indescriptive Naming » (le nommage non descriptif)
Bien que cette pratique semble facile à éviter, elle se produit assez souvent. Pourquoi ça arrive ? Car, au moment où vous écrivez le code, le problème et la solution sont logiques. Imaginez que vous vous occupiez d’un rectangle. Vous nommez donc les variables de l’angle supérieur gauche x1 et y1. C’est logique.

Des mois plus tard, en regardant le code, vous (ou quelqu’un d’autre) voyez ces variables. Qu’est-ce que x1 ? Vous devez lire le code pour le découvrir. Si vous aviez nommé les variables  angle_supérieur_gauche_x  et  angle_supérieur_gauche_y  , vous auriez la réponse tout de suite.

# Que désigne le « D » ? La duplication
La duplication constitue un piège dans lequel il est très facile de tomber. Vous avez besoin d’ajouter une nouvelle fonctionnalité. Elle doit fonctionner comme une fonctionnalité existante, mais un peu différemment. Que faites-vous ? Vous copiez, collez, et modifiez. Si vous adoptez cette approche de façon suivie, vous vous retrouverez avec du code dupliqué en de nombreux endroits. S’il faut modifier quelque chose de fondamental, tous ces emplacements copiés doivent être retrouvés et modifiés.

Vous pouvez copier et coller lorsque vous devez mettre quelque chose en place rapidement. Malgré tout, il vous faudra y revenir et trouver une meilleure solution à long terme. Posez-vous les questions suivantes :

Pourquoi y a-t-il autant de points communs entre ces deux éléments ?

Est-ce que le code dupliqué peut être placé dans une fonction ou classe commune ?

Puis-je extraire une interface et placer les éléments légèrement différents dans des implémentations différentes ?

Il n’y a pas de réponse unique qui fonctionne dans toutes les situations. L’idée principale, ici, est que toutes ces approches STUPID sont faciles à mettre en œuvre. Elles semblent logiques sur le moment. Les problèmes qu’elles créent ne se manifestent que plus tard dans le projet.