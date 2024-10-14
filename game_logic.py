from models import Deck, Player, Card

def initialize_game(num_players):
    deck = Deck()
    players = [Player(f"Player {i+1}") for i in range(num_players)]

    # Draw first card to determine strongest suit
    trumpf_karte = deck.fre9()
    # Trumpf is the suit of the first card
    trumpf = trumpf_karte.farbe
    print(f"Der Trumpf ist: {trumpf_karte}")

    # Set the strongest suit
    Card.strongest_suit = trumpf


    # distribute cards to players

    i = 6
    # 6 cards per player
    while i>0:
        for player in players:
            player.receive_card(deck.fre9())
        i = i-1

    return players, trumpf

def nachbar_recht(players,player):
    # Find the player in the list of players and return the next player
    return players[(players.index(player)+1) % len(players)]


def nachbar_left(players, player):
    # Find the player in the list of players and return the previous player
    return players[(players.index(player)-1) % len(players)]


def play_turn(players, current_player_index, trump_suit):
    
    # Get the current player and their neighbors
    current_player = players[current_player_index]
    right_neighbor = nachbar_recht(current_player)
    defending_neighbor = nachbar_recht(players, right_neighbor)

    # Player attacks the right neighbor
    attacking_card = current_player.attack(right_neighbor)
    if attacking_card:
        # Right neighbor defends
        right_neighbor.isAttacked = True
        # If the right neighbor can defend, print the defending card
        defending_card = right_neighbor.defend(attacking_card, trump_suit)
        if defending_card:
            print(f"{right_neighbor.name} defended with {defending_card}")
        else:
            print(f"{right_neighbor.name} could not defend and takes the card")

    # Check if attacking player or right neighbor can attack again
        pile = attacking_card + ([defending_card] if defending_card else [])
        pile = current_player.second_attack(right_neighbor,defending_neighbor,pile,trump_suit)

    
    

    # Move to the next player
    next_player_index = (current_player_index+1) & len(players)
    return next_player_index
