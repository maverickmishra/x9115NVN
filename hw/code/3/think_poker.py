import os
import random

os.system("clear")

### Card Class ###
class Card(object):
    #Class Attributes:
    suit_class = {0:"Clubs",1:"Diamonds",2:"Hearts",3:"Spades"}
    suit_rank = {1:'Ace',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'Jack',\
                 12:'Queen',13:'King'}

    def __init__(self,suit=0,rank=1):
    #Instance Attributes:
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return '%s of %s' %(Card.suit_rank[self.rank], Card.suit_class[self.suit])

    def __lt__(self,other):
        if (self.suit < other.suit):
            return True
        elif (self.suit > other.suit):
            return False
        else:
            if (self.rank < other.rank):
                return True
            else:
                return False

    def __eq__(self,other):
        if (self.suit == other.suit and self.rank == other.rank):
            return True
        else:
            return False

### Deck Class ###
class Deck(object):
  
    def __init__(self):
        self.cards = []
        for dSuit in range(4):
            for dRange in range(1,14):
                card = Card(dSuit,dRange)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def add_card(self,card):
        self.cards.append(card)
   
    def remove_card(self,card):
        self.cards.remove(card)

    def sort(self):
        self.cards.sort()

    def pop_card(self):
        return self.cards.pop()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def shuffle(self):
        random.shuffle(self.cards)    

    def move_cards(self,hand,num):
        for index in range(num):
            hand.add_card(self.pop_card())

class Hand(Deck):
    def __init__(self,label=''):
        self.cards = []
        self.label = label
    

    def find_defining_class(obj, method_name):
        for ty in type(obj).mro():
            if method_name in ty.__dict__:
                return ty
        return None

if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    print find_defining_class(hand, 'shuffle')

    deck.move_cards(hand, 5)
    hand.sort()
    print hand
