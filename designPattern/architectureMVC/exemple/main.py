"""Entry point."""

from models.card import Card
from models.deck import Deck
from models.player import Player

from controllers.base import Controller
from controllers.evaluate import CheckerRankAndSuitIndex

from views.base import Views
from views.player import PlayerView
from views.broadcast import BroadcastView
from views.internet import InternetStreamingView


def main():
    card1 = Card("diamonds", "cinq")
    card2 = Card("coeurs", "cinq")
    card3 = Card("coeurs", "valet")
    print(card1 < card2)
    print(card3 > card2)

    deck = Deck()
    print(deck)

    player = Player("John")
    player.hand.append(deck.draw_card())
    print(player.hand)

    active_view = PlayerView()
    passive_views = (active_view, BroadcastView(), InternetStreamingView())
    views = Views(active_view, passive_views)

    checker = CheckerRankAndSuitIndex()

    game = Controller(deck, views, checker)
    game.run()


if __name__ == "__main__":    
    main()
