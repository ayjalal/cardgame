from enum import Enum
import pygame
import random

# Farben als Enum

class Farben(Enum):
    Pick = 0
    Kreuz = 1
    Herz = 2
    Karo = 3

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
    
    def misch(self):
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
    
    # idk how to choose the cards that im attacking with

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
        # Variable i should be the index of the attacking card and should be incremented after each successful defense
        i = 0


        # this function is not complete
        # it is written to defend only one card at a time
    
        # Check if the attacking card can be transferred to the defending player's right neighbor

        if pile[i].value in self.card.values:
                self.canTransfer = True
        # need to program how to choose between defending and transferring

        # Sort the player's hand so that cards of the same value are grouped together
        self.hand.sort(key=lambda card: card.value)

        # Neighbor defends against the attacking card
        for card in self.hand:
            if __gt__(card,pile[i]):
                # how to iterate through the attacking cards if there are more than one ? 

                # need to program how to choose a defending card  
                              
                defending_card = self.hand.pop(self.hand.index(card))
                # Remove pile and make an attacker pile
                DefendedPile.add_card(defending_card)
                print(f"{self.name} defends with {defending_card}")
                # increment i to move to the next attacking card
                i += 1
                return defending_card
            
        return None
    
    def can_defend(self, attacking_cards):
        # Check if player can play or if they have to take the cards
        # If the DefendedPile contains all attacking cards, the player can defend
        if len(Pile) == len(DefendedPile):
            isAttacked = False
            # Defending player can attack the next player
            next_player = self
            # Clear the DefendedPile and the Pile   
            Pile.clear()
            DefendedPile.clear()
        else:
            # Defending player has to take the cards
            for card in Pile:
                self.hand.append(card)
                Pile.remove_card(card)
            for card in DefendedPile:
                self.hand.append(card)
                DefendedPile.remove_card(card)
            # Right neighbor of the defending player can attack
            next_player = nachbar_recht(players, self)
        i = 0
        # Check if all players have 6 cards in their hand
        for player in players:
            while len(player.hand) < 6:
                player.hand.append(deck.fre9())

        return next_player
    

    
    def transfer(self, card):
        # Function is written to transfer only one card at a time
        # Check if the attacking card can be transferred to the defending player's right neighbor
        if self.canTransfer:
            self.canTransfer = False
            # Transfer the attacking card to the defending player's right neighbor
            self.hand.remove(card)
            Pile.add_card(card)
            print(f"{self.name} transfers a card to {nachbar_recht.name}")
            nachbar_recht.isAttacked = True
            return True
        return False

    def second_attack(self, defending_player, trump_suit):
        # Function is written to attack only one card at a time
        # Check if self is one of the neighbours of the defending player
        if self == nachbar_recht(defending_player) or self == nachbar_left(defending_player):
            # Check if self can second attack
            for card in self.hand:
                if card.value in Pile or card.value in DefendedPile:
                    # Attack the defending player 
                    # attack with the same value in the defended pile or pile
                    attacking_card = self.attack(defending_player, [card.value])
                    if attacking_card:
                        # Defend the attacking card
                        defending_card = defending_player.defend(attacking_card, trump_suit)
                        if defending_card:
                            print(f"{defending_player.name} defended with {defending_card}")

        return None
    
# Game Logic

# Defended pile to store cards that have been successfully defended
# Pile stores cards that are attacking the player
# if the defended pile doesn't contain all attacking cards, the defending player takes all cards in the pile into his deck