prices = {'apple':1500,'orange': 1000, 'pear': 2000, 'banana' : 500, 'pineapple': 3000}
my_basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

#1. How many fruits in my baskets?
len(prices)

#2. Are there any oranges in my basket?
'orange' in my_basket

#3. Are there any apples or oranges
'apple' in my_basket or 'orange' in my_basket

#4.	Put a pineapple into my basket if it is not in the basket?
if('pineapple' not in my_basket):
    my_basket.append('pineapple')

#5.	What kinds of fruits are in my basket?
len(set(my_basket))

#6.	Show the name of fruits in my basket ending with ‘e’. (Do not show the same names twice)
set_mybasket = set(my_basket)
[i for i in set_mybasket if(i[-1] =='e')]

#7.	How many apples are in my basket?
my_basket.count('apple')

#8.	Count the number for each kind of fruits in my basket. (You may represent them as a dict)
dict_mybasket = { x:my_basket.count(x) for x in set_mybasket}
dict_mybasket

#9.	How much do I pay for the fruits in my basket.
sum(dict_mybasket[i]*prices[i] for i in dict_mybasket)