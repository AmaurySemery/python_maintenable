 S » désigne la responsabilité unique (« Single responsibility »).

Chaque classe ou fonction doit faire une seule chose, et la faire bien. Elle ne doit avoir qu’une seule raison de changer.

« O » désigne le principe ouvert/fermé (« Open/Closed »).

Les classes doivent être ouvertes à l’extension, mais fermées à la modification. Il doit être facile d’ajouter un nouveau concept au système en étendant la fonctionnalité d’origine, sans dupliquer tout un tas de code. De plus, dans l’idéal, vous ne devriez pas avoir à apporter de modifications au code existant, dans l’aventure.

« L » désigne la substitution de Liskov.

Les sous-classes doivent pouvoir faire tout ce que font leurs classes parentes. Si vous remplacez une classe parente par l’une de ses sous-classes, cela ne doit pas casser votre système !

« I » désigne la ségrégation des interfaces (« Interface Segregation »).

Cela correspond essentiellement au principe de responsabilité unique, appliqué aux interfaces.

« D » désigne l’inversion des dépendances (« Dependency Inversion »).

Les classes parentes ne doivent pas avoir à changer lorsque l’une de leurs sous-classes est modifiée.