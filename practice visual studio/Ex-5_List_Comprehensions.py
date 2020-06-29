""" 
Q1.
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: Consider use range(begin, end) method
"""
l = [i for i in range(2000,3201) if(i%7 ==0)]
print(l)

"""
Q2.
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple 
which contains every number. Suppose the following input is supplied to the program:

34, 67, 55, 33, 12, 98
Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
Hints: In case of input data being supplied to the question, it should be assumed to be a console input. 
tuple() method can convert list to tuple

"""
num_str = input()
num_list = num_str.split(', ')
print(num_list)
print(tuple(num_list))

"""
Q3.
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,∼Y-1.

Suppose the following inputs are given to the program:

3,5
Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
Hints: Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

"""
xy_str = input()
x,y = xy_str.split(',')
x = int(x)
y = int(y)
xy_list = [[0 for col in range (y)] for row in range(x)]
for i in range(x):
    for j in range(y):
        xy_list[i][j] = i*j
print(xy_list)

"""
Q4.
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3
Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
"""
word_list = input()
count_letter = 0
count_digit = 0
for i in range(len(word_list)):
    if(word_list[i].isdigit()):
        count_digit += 1
    if(word_list[i].isalpha()):
        count_letter += 1
print('LETTERS ',count_letter)
print('DIGITSS ',count_digit)

"""
Q5.
Write a program which can filter even numbers in a list by using range() for loops and list.append().

The list is:

[1,2,3,4,5,6,7,8,9,10]
Hint: Use range() for loops. Use list.append() to add values into a list.
"""
list = []
for i in range(10):
    if((i+1)%2 != 0):
        list.append((i+1))
print(list)

"""
Q6.
Write a program which can filter even numbers in a list by using list comprehension. The list is:

[1,2,3,4,5,6,7,8,9,10]
Hint: Use list comprehension
"""
list = [i+1 for i in range(10) if((i+1)%2 != 0)]
print(list)

"""

Q7.
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
 write a program to make a list whose elements are intersection of the above given lists.

Hints: Use set() and &= to do set intersection operation.
"""
set1 = set([1,3,6,78,35,55])
set1 &= set([12,24,35,24,88,120,155])
print(set1)

"""


Q8.
Write a program that accepts a sequence of whitespace separated words as input and prints the words 
after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
Then, the output should be:

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
 We use set container to remove duplicated data automatically and then use sorted() to sort the data.
"""
w_list = input().split()
set_w = set(w_list)
list_w = sorted([i for i in set_w])
for i in list_w:
    print(i, end=' ')