suits = 'CDHS'
ranks = '23456789TJQKA'
values = dict(zip(ranks, range(2, 2+len(ranks))))

def is_flush(cards):
    suit = cards[0][1]
    for i in cards:
        if(i[1] != suit):
            return False
    return True
    
def is_straight(cards):
    sort_card = sorted(cards, key = lambda x: x[0], reverse = True)
    num = values[sort_card[0][0]]
    for i in sort_card:
        if(num != values[i[0]]):
            return False
    return True
    
def classify_by_rank(cards):
    dic_card = {}
    for i in cards:
        if(i[0] not in dic_card):
            dic_card[i[0]] = [i]
        else:
            temp = dic_card[i[0]]
            temp.append(i)
            dic_card[i[0]] = temp
    return dic_card

def find_a_kind(cards):
    s_by_ranks = classify_by_rank(cards)
    v_list = [len(i) for i in list(s_by_ranks.values())]
    if(v_list.count(2)==2):
        return 'Two pairs'
    elif(v_list.count(3)==1 and v_list.count(2)==1):
        return 'Full house'
    elif(v_list.count(4) ==1):
        return 'Four of a kind'
    elif(v_list.count(3)==1):
        return 'Three of a kind'
    elif(v_list.count(2)== 1):
        return 'One pair'
   

def tell_hand_ranking(cards):
    if(find_a_kind(cards) != None):
        return find_a_kind(cards)
    elif(is_flush(cards) and is_straight(cards)):
        return 'Straight fluse'
    elif(is_flush(cards)):
        return 'Flush'
    elif(is_straight(cards)):
        return 'Straight'
    else:
        return 'High card'
    
if __name__ == "__main__": 
    hands = [[('J','S'),('T','S'),('9','S'),('8','S'),('7','S')],
    [('5','C'),('5','D'),('5','H'),('5','S'),('2','D')],[('6','S'),('6','H'),('6','D'),('K','C'),('K','H')],
    [('J','D'),('9','D'),('8','D'),('4','D'),('3','D')],[('T','D'),('9','S'),('8','H'),('7','D'),('6','C')],
    [('Q','C'),('Q','S'),('Q','H'),('9','H'),('2','S')],[('J','H'),('J','S'),('3','C'),('3','S'),('2','H')],
    [('T','S'),('T','H'),('8','S'),('3','S'),('2','H')],[('K','D'),('Q','H'),('7','S'),('4','S'),('3','H')]]
    for i in hands:
        print('What is your hands ?',i)
        print(tell_hand_ranking(i))
        print('-'*20)                  # test code here will run.