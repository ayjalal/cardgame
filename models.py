from enum import Enum
import pygame
import random

# Farben als Enum

class Farben(Enum):
    Zrawet = 0
    Tbeg = 1
    Flous = 2
    Syouf = 3

class Card:
    farbe = None
    value = None
    image = None

    def __init__(self,farbe,value):
        self.farbe = farbe
        self.value = value
        self.image = pygame.image.load('images/' + self.farbe.name + '-' + str(self.value) + '.svg')

    def __str__(self):
        return f"{self.farbe.name} {self.value}"
    
    def __gt__(self, other):
        # Compare the value of the cards
        if self.farbe == other.farbe:
            return self.value > other.value
        if self.farbe == Card.strongest_suit:
            return True
        if other.farbe == Card.strongest_suit:
            return False
        # If the suits are different, you can't compare them
        return False
    

class Deck:
    cards = None

    def __init__(self):
        self.cards = []
        for farbe in Farben:
            for value in range(1,11):
                self.cards.append(Card(farbe,value))
    
    def dmes(self):
        random.shuffle(self.cards)

    def fre9(self):
        return self.cards.pop()
    
    def length(self):
        return len(self.cards)

class Pile:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def length(self):
        return len(self.cards)

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)


class DefendedPile(Pile):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"Defended: {self.defended}, Cards: {super().__str__()}"    
    

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.isAttacked = False
        self.canTransfer = False
    

    def receive_card(self, card):
        self.hand.append(card)

def attack(self, neighbor, card_values):
    # Helper function to select cards from the player's hand that match the chosen values
    def select_cards(hand, values):
        selected = []
        for value in values:
            for card in hand:
                if card.value == value:
                    selected.append(card)
                    break
        return selected

    # Sort the player's hand so that cards of the same value are grouped together
    self.hand.sort(key=lambda card: card.value)

    # Use the helper function to find the cards that match the chosen values
    attacking_cards = select_cards(self.hand, card_values)

    # Ensure the number of chosen cards does not exceed the number of cards in the neighbor's hand
    if len(attacking_cards) > len(neighbor.hand):
        raise ValueError("Cannot attack with more cards than the neighbor has in hand")

    # Remove the chosen cards from the player's hand
    for card in attacking_cards:
        self.hand.remove(card)
        Pile.add_card(card)

    # Print the attack details
    print(f"{self.name} attacks {neighbor.name} with {attacking_cards}")

    return attacking_cards

    def defend(self, pile, trump_suit, defending_card):
        # Check if the attacking card can be transferred to the defending player's right neighbor

        if pile[0].value in self.card.values:
                self.canTransfer = True
        # Sort the player's hand so that cards of the same value are grouped together
        self.hand.sort(key=lambda card: card.value)

        # Neighbor defends against the attacking card
        for card in self.hand:
            if __gt__(card,pile[0]):
                defending_card = self.hand.pop(self.hand.index(card))
                Pile.add_card(defending_card)
                DefendedPile.add_card(pile[0])
                print(f"{self.name} defends with {defending_card}")
                return defending_card

        return None
    
    def can_defend(self, attacking_cards):
        # Check if player can play or if they have to take the cards
        # If the DefendedPile contains all attacking cards, the player can defend
        if len(Pile) == 2*len(DefendedPile):
            isAttacked = False
            # Defending player can attack the next player
            next_player = self
        else:
            # Defending player has to take the cards
            for card in Pile:
                self.hand.append(card)
            # Clear the Pile
            Pile.clear()
            # Right neighbor of the defending player can attack
            next_player = nachbar_recht(players, self)

        return next_player
    

    
    def transfer(self, defending_neighbor, card):
        # Check if the attacking card can be transferred to the defending player's right neighbor
        if self.canTransfer:
            self.canTransfer = False
            # Transfer the attacking card to the defending player's right neighbor
            self.hand.remove(card)
            Pile.add_card(card)
            print(f"{self.name} transfers a card to {defending_neighbor.name}")
            defending_neighbor.isAttacked = True
            return True
        return False

    

# Defended pile to store cards that have been successfully defended
# if the defended pile doesn't contain all attacking cards, the defending player takes all cards in the pile into his deck