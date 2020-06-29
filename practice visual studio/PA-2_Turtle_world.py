"""
1. Write a void function to draw a star, where the length of each side is 100 units. (Hint: You should turn the turtle by 144 degrees at each point.) 
void function이란 결과를 return 하지 않는 function
"""

def make_star(t):
        for i in range(5) :
                t.forward(100)
                t.right(144)

"""
2. Extend your program above. Draw five stars, but between each, pick up the pen, move forward by 350 units, turn right by 144, put the pen down, and draw the next star. You’ll get something like this:
"""
import turtle

def make_star(t):
        for i in range(5) :
                t.forward(100)
                t.right(144)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

p_star = turtle.Turtle()
p_star.color("hotpink")
p_star.penup()

for i in range(5):
    p_star.forward(350)
    p_star.right(144)
    p_star.pendown()
    make_star(p_star)
    p_star.penup()

#wn.mainloop()

#3. Write a program to draw a face of a clock that looks something like this.
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

b_turtle  = turtle.Turtle()
b_turtle.shape("turtle")
b_turtle.color("blue")
b_line = turtle.Turtle()
b_line.color("blue")

b_turtle.penup()
b_line.penup()

b_turtle.stamp()
degree = 0
b = (b_line,b_turtle)
for i in range (12):
    degree += 30
    b_line.forward(200)
    b_turtle.forward(250)
    b_line.pendown()
    b_line.forward(10)
    b_line.penup()
    b_turtle.stamp()
    b_line.home()
    b_turtle.home()
    b_line.right(degree)
    b_turtle.right(degree)

wn.mainloop()
