import pytest
import random
from pocker import Ranking, Hands, PKCard
#from card import PKCard

non_flush_suit = 'CHSDS'
flush_suit = 'CCCCC'
test_cases = {
    Ranking.STRAIGHT_FLUSH:(
        tuple(zip('QJT98', flush_suit)), tuple(zip('98765', flush_suit))
    ),
    Ranking.FOUR_OF_A_KIND: (
        tuple(zip('KKKK8', non_flush_suit)), tuple(zip('KKKK3', non_flush_suit)), tuple(zip('7777Q',non_flush_suit))
    ),
    Ranking.FULL_HOUSE: (
        tuple(zip('88877',non_flush_suit)), tuple(zip('44499',non_flush_suit))
    ),
    Ranking.FLUSH: (
        tuple(zip('KK773',flush_suit)), tuple(zip('J8432',flush_suit))
    ),
    Ranking.STRAIGHT: (
        tuple(zip('QJT98',non_flush_suit)), tuple(zip('T9876',non_flush_suit)), tuple(zip('65432',non_flush_suit))
    ),
    Ranking.THREE_OF_A_KIND: (
        tuple(zip('888A9',non_flush_suit)), tuple(zip('888A7',non_flush_suit))
    ),
    Ranking.TWO_PAIR: (
        tuple(zip('QQ882',non_flush_suit)), tuple(zip('QQ663',non_flush_suit)), tuple(zip('JJTTK',non_flush_suit))
    ),
    Ranking.ONE_PAIR: (
        tuple(zip('88AT9',non_flush_suit)), tuple(zip('66Q87',non_flush_suit)), tuple(zip('66Q83',non_flush_suit))
    ),
    Ranking.HIGH_CARD: (
        tuple(zip('A7642',non_flush_suit)), tuple(zip('A7532',non_flush_suit)),tuple(zip('QJT97',non_flush_suit))
    ),
}

def cases(*rankings):
    if not rankings:
        rankings = test_cases.keys()
    return \
        [ ([r+s for r, s in case], ranking)
                    for ranking in rankings
                        for case in test_cases[ranking]
        ]

#parameter 로 faces와 expected로 들어가서 본다.
@pytest.mark.parametrize("faces, expected", cases(Ranking.STRAIGHT_FLUSH))
def test_is_straight_flush(faces, expected):
    hand_org = [PKCard(c) for c in faces]
    random.shuffle(faces)
    hand = Hands([PKCard(c) for c in faces])
    result = False
    if(hand.is_straight()):
        if(hand.is_flush()):
            result = True
    assert result ==True
    assert hand.cards == hand_org

@pytest.mark.parametrize("faces, expected", cases(Ranking.STRAIGHT))
def test_is_straight(faces, expected):
    hand_org = [PKCard(c) for c in faces]
    random.shuffle(faces)
    hand = Hands([PKCard(c) for c in faces])
    result = hand.is_straight()
    assert result ==True
    assert hand.cards == hand_org

@pytest.mark.parametrize("faces, expected", cases(Ranking.FLUSH))
def test_is_flush(faces, expected):
    hand_org = [PKCard(c) for c in faces]
    random.shuffle(faces)
    hand = Hands([PKCard(c) for c in faces])
    result = hand.is_flush()
    assert result ==True
    assert hand.cards == hand_org

@pytest.mark.parametrize("faces, expected", cases(Ranking.FOUR_OF_A_KIND, Ranking.THREE_OF_A_KIND,
                                     Ranking.TWO_PAIR, Ranking.ONE_PAIR))
def test_is_find_a_kind(faces, expected):
    hand_org = [PKCard(c) for c in faces]
    random.shuffle(faces)
    hand = Hands([PKCard(c) for c in faces])
    result = hand.find_a_kind()
    assert result == expected
    assert hand.cards == hand_org

@pytest.mark.parametrize("faces, expected", cases(Ranking.HIGH_CARD))
def test_find_a_kind_None(faces, expected):
    hand_org = [PKCard(c) for c in faces]
    random.shuffle(faces)
    hand = Hands([PKCard(c) for c in faces])
    result = hand.find_a_kind()
    assert result == None
    assert hand.cards == hand_org

@pytest.mark.parametrize("faces, expected", cases())
def test_eval(faces, expected):
    random.shuffle(faces)
    hand = Hands([PKCard(c) for c in faces])
    hand.tell_hand_ranking()
    assert hand.ranking == expected

def test_who_wins():
    hand_cases = [Hands(faces) for faces, ranking in cases()]
    for hand in hand_cases:
        hand.tell_hand_ranking()
    sorted_cases = sorted(hand_cases, reverse = True)
    assert sorted_cases == hand_cases
    print('\nHigh to low order:')
    for i, hand in enumerate(hand_cases):
        print(i, hand)