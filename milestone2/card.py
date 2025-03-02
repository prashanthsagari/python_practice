import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
card_values = {
"Ace": 14,    # Can also be 1 in some games
"King": 13,
"Queen": 12,
"Jack": 11,
"Ten": 10,
"Nine": 9,
"Eight": 8,
"Seven": 7,
"Six": 6,
"Five": 5,
"Four": 4,
"Three": 3,
"Two": 2
}
    
    
class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = card_values[rank]
    
    def __str__(self):
        return f'{self.rank} of {self.suit} is {self.value}'
    
class Deck:
    
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # create the card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle_deck(self):
        random.shuffle(self.all_cards)
        
    

        

new_deck = Deck() 
new_deck.shuffle_deck()      

# print(two_hearts)
for deck in new_deck.all_cards:
    print(deck)