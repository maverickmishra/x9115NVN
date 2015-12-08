"""
Core module from:
Think Python by Allen B. Downey
http://thinkpython.com
Copyright 2012 Allen B. Downey

"""

from __future__ import division
from think_poker import *

def run_iterations(handDict,cardPerHand,players,deck):
    for index in range(players):
        pHand = PokerHand()       
        deck.move_cards(pHand, cardPerHand)
        pHand.sort()
        pHand.suit_classify()
        handDict[pHand.label] = handDict[pHand.label] + 1

class PokerHand(Hand):

    def suit_hist(self):
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    # Histogram of the deck based on Rank
    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    # Classification based on: https://en.wikipedia.org/wiki/List_of_poker_hands
    def suit_classify(self):
        if (self.has_straightflush()):
            self.label = 'straight flush'
        elif (self.has_fourkind()):
            self.label = '4 of kind'
        elif (self.has_fullhouse()):
            self.label = 'full house'
        elif (self.has_flush()):
            self.label = 'flush'
        elif (self.has_straight()):
            self.label = 'straight'
        elif (self.has_threekind()):
            self.label = '3 of kind'
        elif (self.has_twopair()):
            self.label = '2 pair'
        elif (self.has_pair()):
            self.label = 'pair'
        else:
            self.label = 'high card'
           
    def has_flush(self):
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    #Check if a pair is present
    def has_pair(self):
        if (len(self.cards) < 2):
            return False
        self.rank_hist()
        for val in self.ranks.values():
            if (val == 2):
                return True
        return False
 
    #Check if 2 pairs are present
    def has_twopair(self):
        if (len(self.cards) < 4):
            return False
        self.rank_hist()
        indicatorFlag = False
        for val in self.ranks.values():
            if (val == 2):
                if (indicatorFlag):
                    return True
                else:
                    indicatorFlag = True
        return False
            
    #Check if 3 pairs are present
    def has_threekind(self):
        if (len(self.cards) < 3):
            return False
        self.rank_hist()
        for val in self.ranks.values():
            if (val >= 3):
                return True
        return False
    
    #Check for 4 kind         
    def has_fourkind(self):
        if (len(self.cards) < 3):
            return False
        self.rank_hist()
        for val in self.ranks.values():
            if (val >= 4):
                return True
        return False


    def has_fullhouse(self):
        if (len(self.cards) < 5):
            return False
        self.rank_hist()
        threeFlag = False
        twoFlag = False
        for val in self.ranks.values():
            if (val >= 3):
                threeFlag = True
            elif (val >= 2):
                twoFlag = True 
        return (threeFlag and twoFlag)


    def has_straight(self):
        if (len(self.cards) < 5):
            return False
        self.sort()
        tempVal = self.cards[0].rank
        for card in self.cards:
            if (tempVal == card.rank):
                tempVal = tempVal + 1
                if (tempVal == 14):
                    tempVal = 0
            else:
                return False
        return True
  
    def has_straightflush(self):
        if (len(self.cards) < 5):
            return False
        if (self.has_flush()):
            if (self.has_straight()):
                return True                         
        return False
 
        
      
if __name__ == '__main__':
    # number of iterations
    n = 10000
    # cards per player
    players = 7
    #cards per hand
    cardList = [5,7]
    for cardPerHand in cardList:
        handDict = {'straight flush':0, '4 of kind':0, 'full house': 0, 'flush':0, 'straight':0,'3 of kind':0,\
                    '2 pair':0, 'pair':0,'high card':0}
        print_order = ('straight flush', '4 of kind', 'full house', 'flush', 'straight', '3 of kind', '2 pair', 'pair', 'high card')
        totalRuns = n*players 
        # for each iteration
        print "Running iterations :"	
        for index in range (0,n):
            deck = Deck()
            deck.shuffle()         
            run_iterations(handDict,cardPerHand,players,deck) 

        print "Number of iterations: ",(totalRuns)
        print "Number of Players per iteration: ",players
        print "Number of cards per player: ",cardPerHand
        print "Frequency of -"
        for values in print_order:
            relFreq = handDict[values]
            relFreq = relFreq/totalRuns
            relFreq = relFreq*100
            indent = 14 - len(values)
            print "%s" %(values),
            print " "*indent,":",
            print "%8.5f%%" %(relFreq)

        print ''   











