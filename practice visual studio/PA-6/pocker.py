import sys
from enum import IntEnum
import logging
import random
from abc import ABCMeta, abstractmethod

# Constants
suits = 'CDHS'
ranks = '23456789TJQKA'
values = dict(zip(ranks, range(2, 2+len(ranks))))

class Ranking(IntEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8

class Card(metaclass=ABCMeta):
    def __init__(self, rank_suit):
        if rank_suit[0] not in ranks or rank_suit[1] not in suits:
            raise ValueError(f'{rank_suit}: illegal card')
        self.card = rank_suit
        
    def __repr__(self):
        if (type(self.card) == tuple):
            return self.card[0]+self.card[1]
        return self.card

    @property
    def rank(self):
        return self.card[0]
    
    @property
    def suit(self):
        return self.card[1]

    #abstractmethod는 꼭 상속 받았을 때 오버라이드 되야 된다.
    @abstractmethod
    def value(self):
        raise NotImplementedError("value method not implemented")

    # card comparison operators
    def __gt__(self, other): return self.value() > other.value()
    def __ge__(self, other): return self.value() >= other.value()
    def __lt__(self, other): return self.value() < other.value()
    def __le__(self, other): return self.value() <= other.value()
    def __eq__(self, other): return self.value() == other.value()
    def __ne__(self, other): return self.value() != other.value()

class PKCard(Card):
    VALUES = dict(zip(ranks, range(2, 2+len(ranks))))
    def value(self):
        return PKCard.VALUES[self.card[0]]
        
class Deck:
    def __init__(self, cls):
        self.cls = cls
        self.card = []
        for x in ranks:
            for y in suits:
                self.card.append(cls(x+y))

    def shuffle(self):
        random.shuffle(self.card)

    def pop(self):
        return self.card.pop()
    
    def __str__(self):
        return "{}".format(repr(self.card))

    def __len__(self):
        return len(self.card)

    def __getitem__(self, index):
        return self.card[index]

class Hands:
    def __init__(self, cards):
        if len(cards) != 5:
            raise ValueError('not 5 cards')
        card_list = []
        for card in cards:
            if(isinstance(card, PKCard)):
                card_list.append(card)
            else:
                card_list.append(PKCard(card))
        self.cards = sorted(card_list,reverse=True)
        self.ranking = None
    
    def __repr__(self):
        return '-'.join([repr(c) for c in self.cards]) + ': '+ repr(self.ranking)
    
    def _check(self,other):
        if self.ranking is None or other.ranking is None:
            raise AttributeError('not evaluted. call eval() method')
    
    def __gt__(self, other):
        self._check(other)
        return (self.ranking,self.cards) > (other.ranking, other.cards) 

    """def __lt__(self, other): 
        self._check(other)
        return (self.ranking,self.cards) < (other.ranking, other.cards) """

    """def __eq__(self, other):
        self._check(other)
        return (self.ranking,self.cards) == (other.ranking, other.cards)"""

    """def __ne__(self, other):
        self._check(other)
        return (self.ranking,self.cards) != (other.ranking, other.cards)"""

    def is_flush(self):
        check_suits = self.cards[0].card[1]
        for i in self.cards:
            if(check_suits != i.card[1]):
                return False
        return True
        
    def is_straight(self):
        self.cards = list(reversed(sorted(self.cards, key=lambda x: values[x.card[0]])))
        num = values[ self.cards[0].card[0]]
        for i in  self.cards:
            if(values[i.card[0]] == num):
                num -= 1
            else:
                return False
        return True
        
    def classify_by_rank(self):
        dic_cards = {}
        for card in self.cards:
            card.card[0]
            if(card.card[0] in dic_cards):
                temp = dic_cards[card.card[0]]
                temp.append(card.card)
                dic_cards[card.card[0]] = temp
            else:
                temp=[]
                temp.append(card.card)
                dic_cards[card.card[0]] = temp
        return dic_cards

    def find_a_kind(self):
        self.cards = sorted(self.cards,reverse=True)
        cards_dict = self.classify_by_rank()
        ranking = None
        if(cards_dict != None):
            count = {}
            for i,j in cards_dict.items():
                count[i] = len(j)
            c_values = list(count.values())
            if(3 in c_values and 2 in c_values ):
                list1_m = [PKCard(y) for x in cards_dict if(len(cards_dict[x]) in [3,4]) for y in cards_dict[x]]
                list2_m = [PKCard(y) for x in cards_dict if(len(cards_dict[x]) in [1,2]) for y in cards_dict[x]]
                list1_m.sort(reverse=True)
                list2_m.sort(reverse=True)
                self.cards = list1_m+list2_m
                ranking = Ranking.FULL_HOUSE
            elif(c_values.count(2) == 2):
                list1_m = [PKCard(y) for x in cards_dict if(len(cards_dict[x])==2) for y in cards_dict[x]]
                list1_m.sort(reverse=True)
                element = [PKCard(y) for x in cards_dict if(len(cards_dict[x])==1) for y in cards_dict[x]]
                list1_m.append(element[0])
                self.cards = list1_m
                ranking = Ranking.TWO_PAIR
            elif(2 in c_values):
                list1_m = [PKCard(y) for x in cards_dict if(len(cards_dict[x])==2) for y in cards_dict[x]]
                list2_m = [PKCard(y) for x in cards_dict if(len(cards_dict[x]) == 1) for y in cards_dict[x]]
                list1_m.sort(reverse=True)
                list2_m.sort(reverse=True)
                self.cards = list1_m+list2_m
                ranking = Ranking.ONE_PAIR
            elif(3 in c_values):
                list1_m = [PKCard(y) for x in cards_dict if(len(cards_dict[x]) in [3,4]) for y in cards_dict[x]]
                list2_m = [PKCard(y) for x in cards_dict if(len(cards_dict[x]) in [1,2]) for y in cards_dict[x]]
                list1_m.sort(reverse=True)
                list2_m.sort(reverse=True)
                self.cards = list1_m+list2_m
                ranking = Ranking.THREE_OF_A_KIND
            elif(4 in c_values):
                list1_m = [PKCard(y) for x in cards_dict if(len(cards_dict[x]) in [3,4]) for y in cards_dict[x]]
                list2_m = [PKCard(y) for x in cards_dict if(len(cards_dict[x]) in [1,2]) for y in cards_dict[x]]
                list1_m.sort(reverse=True)
                list2_m.sort(reverse=True)
                self.cards = list1_m+list2_m
                ranking = Ranking.FOUR_OF_A_KIND
        return ranking

    def tell_hand_ranking(self):
        if self.is_flush() and self.is_straight():
            self.ranking = Ranking.STRAIGHT_FLUSH
        elif self.is_flush():
            self.ranking = Ranking.FLUSH
        elif self.is_straight():
            self.ranking = Ranking.STRAIGHT
        else:
            self.ranking = self.find_a_kind()
            if(self.ranking == None):
                self.ranking = Ranking.HIGH_CARD