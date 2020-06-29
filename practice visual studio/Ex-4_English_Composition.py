"""
쇼핑 바구니에 쇼핑한 과일 종류별로 몇 개 있는지 묘사하는 완전한 영어 문장을 완성하여 return하는 함수 sentence(basket)을 작성하라.

단수, 복수를 구분하여야 하고, 단수일 경우 'a'와 'an'을 영문법에 맞게 구분해야 한다.
갯수가 4개 이상이면 'many'로 표현하기로 한다.
편의상, 사전식 순서를 따라 과일을 열거하기로 한다. (apple이 banana 보다 먼저

"""

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def sentence(basket):
    dic_basket = {}
    for i in basket:
        dic_basket[i] = dic_basket.get(i,0)+1
    count = ['a','an','two','three','many']
    list = []
    key = sorted(dic_basket)
    
    for x in key:
        y = dic_basket[x]
        if(y == 1):
            if(x[0] in ['a','e','i','o','u']):
                list.append(count[1]+' '+x)
            else:
                list.append(count[0]+' '+x)
        elif(y >= 4):
            list.append(count[4]+ ' '+x+'s')
        else:
            list.append(count[y]+' '+x+'s')
    string =''
    if(len(dic_basket) ==1 ):
        string += 'There is '
    else : 
        string += 'There are '  
    string += ', '.join(list[:-1])+', and '+list[-1]+' in the basket.'                                                                                  
    return string
    
fruits = ['orange', 'pear', 'pear', 'apple', 'orange', 'banana']
test(sentence(fruits) == 'There are an apple, a banana, two oranges, and two pears in the basket.')
many_oranges = ['apple', 'orange', 'orange', 'orange','pear', 'orange']
test(sentence(many_oranges) == 'There are an apple, many oranges, and a pear in the basket.')