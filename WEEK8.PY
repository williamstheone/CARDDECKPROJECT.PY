
import random
class Card:

def __init__(self, rank, suit):
  self.rank = rank
  self.suit = suit

class Deck:
def __init__(self):
  self.cards = []
  self.reset()
def reset(self):
  self.cards = []
  ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
  suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
  for suit in suits:
  for rank in ranks:
  self.cards.append(Card(rank, suit))
def shuffle(self):
  random.shuffle(self.cards)
def deal_card(self):
  if len(self.cards) > 0:
  return self.cards.pop()
else:
  print("No more cards to deal!")
  return None

class Hand:
def __init__(self):
  self.cards = []
def add_card(self, card):
  self.cards.append(card)
def display(self):
  for card in self.cards:
  print(card.rank, "of", card.suit)
  deck = Deck()
  deck.shuffle()
  hand = Hand()
  print("Card dealer")
  print("I have shuffled a deck of 52 cards")

num_cards = int(input("How many cards do you want to deal? "))

for _ in range(num_cards):

card = deck.deal_card()

if card:

hand.add_card(card)

print("Your Hand:")

hand.display()

print("There are", len(deck.cards), "cards left in the deck")

print("Good Luck!!!")





