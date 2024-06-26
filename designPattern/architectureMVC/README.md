Le MVC est une approche d’architecture de logiciel. Il divise les responsabilités du système en 3 parties distinctes :

Modèle : Le modèle contient les informations relatives à l’état du système. Ce sont les fonctionnalités brutes de l’application.

Vue : La vue présente les informations du modèle à l’utilisateur. Elle sert d’interface visuelle et/ou sonore pour l’utilisateur.

Contrôleur : Le contrôleur garantit que les commandes utilisateurs soient exécutées correctement, modifiant les objets du modèle appropriés, et mettant à jour l’application. C’est finalement les rouages de l’application, et c’est la couche qui apporte une interaction avec l’utilisateur. 

Modèle (M)
```
PRICE_PER_SONG = 1.20
 

class Song:
    """Modèle représentant un son."""
 
    def __init__(self, name, artist, genre, artwork):
        """Initialise les détails relatifs au son."""
        self.artist = artist
        self.name = name
        self.genre = genre
        self.artwork = artwork
 

class Library:
    """Modèle qui stocke les sons."""
 
    def __init__(self):
        """Initialise une liste de sons."""
        self.songs = []
 

class ServiceInfo:
    """Modèle qui gère la maintenance de la jukebox."""

    def __init__(self, status, engineer_name):
        """Initialise les détails du service."""
        self.service_date = datetime.now()
        self.status = status
        self.engineer = engineer_name
```

Vue (V)
```
class Touchscreen:
    """Vue qui gère l'interface de la jukebox."""
 
    def select_song(self):
        """Sélectionne un son."""
        pass
 
    def prompt_for_next_song(self, songs):
        """Demande un nouveau son."""
        for song in songs:
            # affiche les sons
            pass
        return "Dark Chest of Wonders"
 
 
class Speakers:
    """Vue qui gère le son."""
 
    def __init__(self):
        """Initialise le volume."""
        self.volume = 5
 
    def get_louder(self):
        """Augmente le volume."""
        self.volume += 1
 
    def get_quieter(self):
        """Baisse le volume."""
        self.volume -= 1
 
    def play_song(self, song):
        """Joue la musique."""
        pass
 
 
class CoinSlot:
    """Vue qui gère la reception de l'argent."""
 
    def __init__(self, amount):
        """Initialise le montant."""
        self.amount = amount
 
    def request_money(self, amount):
        """Attend un montant de l'utilisateur."""
        # attend l'argent
        # donne le change
        self.amount += amount
        return True
```

Contrôleur (C)
```
class Controller:
    """Contrôleur principal."""
 
    def __init__(self):
        """Initialise les modèles et les vues."""
        self.bank = CoinBox()
        self.library = Library()
        self.service_history = []
 
        self.ui = Touchscreen()
        self.audio_output = Speakers()
 
    def play_next_song(self):
        """Joue le prochain son."""
        songs_to_suggest = []
        for song in self.library:
            # filter logic
            songs_to_suggest.append(song)
 
        chosen_song = self.ui.prompt_for_next_song(songs_to_suggest)
        request_money(PRICE_PER_SONG)
        self.audio_output.play_song(chosen_song)
 
    # Beaucoup plus de méthodes ici...
```

Le fait de séparer ainsi des parties de l’architecture en morceaux différents, avec des responsabilités distinctes, rend le système beaucoup plus facile à :

comprendre ;

modifier ;

tester ;

réparer.

Le MVC assure que votre code est facile à maintenir, en séparant les responsabilités :

Le modèle contient les informations sur l’état.

La vue contient les éléments qui interagissent avec l’utilisateur.

Le contrôleur s’assure que la séquence des étapes se déroule correctement.

Le modèle est constitué des éléments avec lesquels vous avez des interactions. Ceux-ci contiennent les informations sur l’état du système.

Pour trouver vos objets de modèle, consultez la liste des prérequis.

Dans notre application, nous avons défini que :

○      Le modèle est constitué d’un joueur, d’une main, d’une carte à jouer, d’un jeu, d’un rang et d’une couleur.

○      Un joueur possède une main. Une main contient des cartes à jouer. Un jeu contient des cartes à jouer.

Le contrôleur est responsable du séquençage du cas d’usage, et valide les événements envoyés par la vue.

La vue est responsable de la présentation du modèle, de l’information de la séquence, et de la récolte des inputs de l’utilisateur.

Les responsabilités du contrôleur sont définies en regardant les étapes de l’application. Les responsabilités de la vue sont définies par ce que le contrôleur doit montrer à l’utilisateur.

https://folk.universitetetioslo.no/trygver/index.html