"""
임의의 text file에 있는 word들의 빈도수를 구하려 한다. word는 대소문자 구분없고 숫자, 특수 문자들은 단어에서 배제된다. 
따라서, word들의 list를 만들기 전에 file을 읽고 난 후

대문자는 소문자로 변환
숫자, 특수문자는 ' ' 로 변환해야 할 것이다.
Hint:
주어진 text를 한 번 scan으로 효율적으로 변환해 주는 string method를 사용하면 될 것이다. 
maketrans method는 변환시키는 dictionany를 정의해 주고, translate method는 이를 가지고 변환한 새로운 string을 generate한다.
"""

the_text = '"Well, I never!", said Alice.'
my_substitutions = the_text.maketrans(
  # If you find any of these
  "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
  # Replace them by these
  "abcdefghijklmnopqrstuvwxyz                                          ")

# Translate the text now.
cleaned_text = the_text.translate(my_substitutions)
print(cleaned_text)

#Input:
#인터넷에 있는 Alice in Wonderland 동화책 내용을 다음과 같이 fetch한다.
import urllib

url = "http://openbookproject.net/thinkcs/python/english3e/_downloads/alice_in_wonderland.txt" 
with urllib.request.urlopen(url) as f:
    contents = f.read().decode()
print(contents[:500])

#Q1. How many different words are used in the Alice in Wonderland?
my_substitution = contents.maketrans(
  # If you find any of these
  "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_{|}~\\",
  # Replace them by these
  "abcdefghijklmnopqrstuvwxyz                                        ")

# Translate the text now.
changed = contents.translate(my_substitution)
word = changed.split()

for i in range(len(word)):
    if(word[i][0] == "'"):
        word[i] = word[i][1:]
    elif(word[i][-1] == "'"):
        word[i] = word[i][:-1]
set_word = set(word)
set_word.remove("")
print(len(set_word))

#Q2. List top 20 frequently used words and their frequencies in the Alice in Wonderland.
Q2. List top 20 frequently used words and their frequencies in the Alice in Wonderland.

"""
Q3.
As children learn to read, there are expectations that their vocabulary will grow. 
So a child of age 14 is expected to know more words than a child of age 8. 
When prescribing reading books for a grade, an important question might be “which words in this book are not in the expected vocabulary 
at this level?”

Find the words in the book Alice in the Wonderland are not in the vocabulary given in the file 
http://openbookproject.net/thinkcs/python/english3e/_downloads/vocab.txt.

(어린이가 수준 이상이 되는 단어들을 찾아내는 문제다. 적절한 수준의 단어들로 채워진 단어장에 없으면 적정 수준을 초과한 어려운 단어라는 의미다.)
"""
child = "http://openbookproject.net/thinkcs/python/english3e/_downloads/vocab.txt" 
with urllib.request.urlopen(child) as f:
    wlist = f.read().decode()
vol = wlist.split()
alice_word = list(set_word)
for i in vol:
    if(i in alice_word):
        alice_word.remove(i)
print(len(alice_word))
print(alice_word)