import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ['Heart', 'Diamond', 'Club', 'Spade']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw_card(self):
        return self.cards.pop() if self.cards else None

# Tạo một bộ bài và kiểm tra các phương thức
deck = Deck()
deck.shuffle()
print("Shuffled deck:", deck.cards)

drawn_card = deck.draw_card()
print("Drawn card:", drawn_card)
print("Remaining deck:", deck.cards)
