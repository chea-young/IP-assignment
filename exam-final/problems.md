# Coding Exam: Problems
---
## q1. Square Every Digit
You are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 9<sup>2</sup> is 81 and 1<sup>2</sup> is 1.

Note: The function accepts an integer and returns an integer

## q2. The Supermarket Queue
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

#### input
- customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
- n: a positive integer, the number of checkout tills.
#### output
The function should return an integer, the total time required.

#### Examples
```Python
queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the 
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12
```
### Clarifications
- There is only ONE queue serving many tills, and
- The order of the queue NEVER changes, and
- The front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.

N.B. You should assume that all the test input will be valid, as specified above.

P.S. The situation can be likened to the more-computer-science-related idea of a thread pool, with relation to running multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool

## q3. Regexp Basics - is it IPv4 address?
Implement ipv4_address, which should return true if given object is an IPv4 address - four numbers (0-255) separated by dots.

It should only accept addresses in canonical representation, so no leading 0s, spaces etc.

## q4. Vector Class
Create a class Vector that has simple (3D) vector operators.

In your class, you should support the following operations, given Vector a and Vector b:

```Python
Vector([x, y, z]) # creates a new Vector from the supplied 3D array.
Vector(x, y, z) # same as above
a.x # gets x component
a.y # gets y component
a.z # gets z component
a + b # returns a new Vector that is the resultant of adding them
a - b # same, but with subtraction
a == b # returns true if they have the same magnitude and direction
a.magnitude # returns a number that is the magnitude (geometric length) of vector a.
a.cross(b) # returns a new Vector that is the cross product of a and b 
a.dot(b) # returns a number that is the dot product of a and b
a.to_tuple() # returns a tuple representation of the vector.
str(a) # returns a string representation of the vector in the form "<x, y, z>"
```

See [Vector calculus: cross/dot product](https://betterexplained.com/articles/cross-product/)

## q5. Sequence generator
Write a generator sequence_gen that, given the first terms of a sequence will generate a (potentially) infinite amount of terms, where each subsequent term is the sum of the previous x terms where x is the amount of initial arguments (examples of such sequences are the Fibonacci, Tribonacci and Lucas number sequences).

#### Examples
```Python
fib = sequence_gen(0, 1)
fib.next() = 0 # first term (provided)
fib.next() = 1 # second term (provided)
fib.next() = 1 # third term (sum of first and second terms)
fib.next() = 2 # fourth term (sum of second and third terms)
fib.next() = 3 # fifth term (sum of third and fourth terms)
fib.next() = 5 # sixth term (sum of fourth and fifth terms)
fib.next() = 8 # seventh term (sum of fifth and sixth terms)

trib = sequence_gen(0,1,1)
trib.next() = 0 # first term (provided)
trib.next() = 1 # second term (provided)
trib.next() = 1 # third term (provided)
trib.next() = 2 # fourth term (sum of first, second and third terms)
trib.next() = 4 # fifth term (sum of second, third and fourth terms)
trib.next() = 7 # sixth term (sum of third, fourth and fifth terms)

lucas = sequence_gen(2,1)
[lucas.next() for _ in range(10)] = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
```

Note: You can assume you will get at least one argument and any arguments given will be valid (positive or negative integers) so no error checking is needed.

## q6. Most Frequent Weekdays
What is your favourite day of the week? Check if it's the most frequent day of the week in the year.

You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year. The result has to be a list of days sorted by the order of days in week (e. g. `['Monday', 'Tuesday'], ['Saturday', 'Sunday'], ['Monday', 'Sunday']`). Week starts with Monday.

**Input**: Year as an int.

**Output**: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).

**Preconditions**:

- Week starts on Monday.
- Year is between 1583 and 4000.
- Calendar is Gregorian.

**Example**:
```Python
most_frequent_days(2427) == ['Friday']
most_frequent_days(2185) == ['Saturday']
most_frequent_days(2860) == ['Thursday', 'Friday']
```

## clients.py:  Multiple echo clients - I/O multiplexing version
The code given in https://github.com/jinpyohong/np/blob/master/echo/clients/clients.py runs multiple echo clients in parallel by taking advatage of multi-threading.

Referring to this code, you are requested to implement the same bebavior with the altenative way: I/O multiplexing. The script file name should be `clients.py`.

**Usage**:
```bash
$ python clients.py host:port <# of messages> [n]   # run n(=3, default) clients
```
> 참고: Non-blocking으로 `select`를 사용할 때, file-like socket object (`makefile`)을 사용하면 안된다. `send`, `recv` socket API를 사용해야 함.
