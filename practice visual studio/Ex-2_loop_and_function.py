import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

#Q1. 절대값을def absolute_value(n):   # Buggy version
def absolute_value(n):   # Buggy version
    if n < 0:
        return n*(-1)
    elif n > 0:
        return n
    elif n == 0:
        return 0
    
test(absolute_value(17) == 17)
test(absolute_value(-17) == 17)
test(absolute_value(0) == 0)
test(absolute_value(3.14) == 3.14)
test(absolute_value(-3.14) == 3.14)

#Q2. 정수를 매개 변수로 받아 각 자리를 제곱한 뒤 모두 더하는 sum_of_digit_square function을 작성하라.
#Parameter: 789 -> Output: 49+64+81=194
def sum_of_digit_square(n):
    str_n = str(absolute_value(n))
    sum = 0
    for i in range(len(str_n)):
        sum += int(str_n[i])**2
    return sum
test(sum_of_digit_square(789) == 7**2 + 8**2 + 9**2)
test(sum_of_digit_square(-123) == 1**2 + 2**2 + 3**2 )

#Q3. 2이상의 자연수를 매개 변수로 받아 소수인지 검사하는 is_prime function을 작성하라.
def is_prime(n):
    for i in range (2,n):
        if(n%i == 0):
            return False
    return True
    
test(is_prime(2) == True)
test(is_prime(5) == True)
test(is_prime(12) == False)
test(is_prime(13) == True)
test(is_prime(1033) == True)

#Q4. 2이상의 자연수를 인자로 받아, 아래와 같은 문양을 출력하는 star_pattern void function을 작성하라.
#void function이란 결과를 return하지 않는 함수다.
def star_pattern(n):
    for i in range(1,n):
        print('*'*(i))
    for i in range(n,0,-1):
        print('*'*(i))
        
star_pattern(5)
star_pattern(6)

#Q5. 자연수를 매개 변수로 받아 가장 가까운 완전 제곱수를 출력하는 perfect_square function을 작성하라.
def perfect_square(n):
    n_extra = n**(1/2)
    num = int(n_extra)
    num_plus = num+1
    if(absolute_value(num**2-n) > absolute_value(num_plus**2 - n)):
        return num_plus
    else:
        return num

test(perfect_square(15) == 4)
test(perfect_square(31) == 6)
test(perfect_square(41) == 6)
test(perfect_square(99) == 10)

#Q6. 자연수를 매개 변수로 받아 각 자리의 수를 더하여 새로운 수를 구하고, 이를 반복하여 한 자리 수를 만들어 출력하는 unit_place_value function을 작성하라.
#(e.g., 75 -> 7+5=12 -> 1+2=3).
def unit_place_value(n):
    str_n = str(n)
    if(len(str_n) == 1 ):
        return n
    else :
        sum = 0
        for i in range(len(str_n)):
            sum += int(str_n[i])
        return unit_place_value(sum)
    
test(unit_place_value(75) == 3)
test(unit_place_value(3942) == 9)
test(unit_place_value(32) == 5)
test(unit_place_value(9) == 9)

#Q7. 자연수를 매개 변수로 받아 해당 숫자까지의 팩토리얼을 계산하는 recursive_factorial recursive function을 작성하라.
def recursive_factorial(n):
    if(n<=0):
        return 1
    else:
        return n*recursive_factorial(n-1)
    
import math
test(recursive_factorial(5) == math.factorial(5))
test(recursive_factorial(8) == math.factorial(8))
test(recursive_factorial(2) == math.factorial(2))
test(recursive_factorial(10) == math.factorial(10))

#Q8. 자연수를 매개 변수로 받아 해당 숫자까지의 팩토리얼을 계산하는 non_recursive_factorial non recursive function을 작성하라.
def non_recursive_factorial(n):
    sum = 1
    for i in range(1,n+1):
        sum *= i
    return sum
    
import math
test(non_recursive_factorial(5) == math.factorial(5))
test(non_recursive_factorial(8) == math.factorial(8))
test(non_recursive_factorial(2) == math.factorial(2))
test(non_recursive_factorial(10) == math.factorial(10))

#Q9. 두 자연수를 매개 변수로 받아 최대공약수를 구하는 my_gcd function을 작성하라.
def my_gcd(a, b):
    a = absolute_value(a)
    b = absolute_value(b)
    min_num = min(a,b)
    for i in range(min_num,0,-1):
        if(a %i ==0 and b%i ==0):
            return i

import math
test(my_gcd(12, 16) == math.gcd(12,16))
test(my_gcd(16, 12) == math.gcd(16, 12))
test(my_gcd(9, 6) == math.gcd(9, 6))
test(my_gcd(-12, -38) == math.gcd(-12, -38))

#Q10. 임의의 정수가 들어있는 set을 input으로 입력받아, 가장 큰 세 숫자만을 가지고 있는 set을 반환하는 max_of_three function을 작성하라.
def max_of_three(l):
    count = len(l)-3
    list_l = list(l)
    for i in range(count):
        list_l.remove(min(list_l))
    return set(list_l)

test(max_of_three({1, 2, 3, 4, 5}) == {3, 4, 5})
test(max_of_three({-100, 42, 32, -4, -1}) == {42, 32, -1})

#Q11. 임의의 정수가 들어있는 리스트를 input으로 입력받아, 전부 곱한 결과를 반환하는 mult_of_list function을 작성하라.
def mult_of_list(l):
    mul_num = 1
    for i in l:
        mul_num *= i
    return mul_num

test(mult_of_list([1, 2, 3, 4]) == 24)
test(mult_of_list([1, 20, -3, 4]) == -240)
test(mult_of_list([1, 0, -33, 9999]) == 0)

#Q12. 임의의 정수가 들어있는 리스트를 input으로 입력받아, 그 중 짝수만을 가진 리스트를 반환하는 even_filter function을 작성하라.
def even_filter(l):
    even = []
    for i in l:
        if(i%2 == 0):
            even.append(i)
    return even

test(even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 4, 6, 8])
test(even_filter([1, 3, 5, 7, 9]) == [])