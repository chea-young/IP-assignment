import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

class Point:    
    """2D Point class"""
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5
    
    def midpoint(self, other):
        """ Return the midpoint of points p1 and p2 """
        mx = (self.x + other.x)/2
        my = (self.y + other.y)/2
        return Point(mx, my)
    
    def __eq__(self, other):
        if(self.x ==other.x):
            if(self.y ==other.y):
                return True
        return False
    
    def __ne__(self, other):
        if(self.x ==other.x):
            if(self.y ==other.y):
                return False
        return True
    
    def reflect_x(self):
        return (self.x*(-1), self.y)
    
    def slope_from_origin(self):
        line = 0
        try: 
            line = self.y/self.x
        except ZeroDivisionError as err:
            print(err)
        finally:
            return line
        
    def get_line_to(self, other):
        a = 0
        try:
            a = (other.y - self.y)/(other.x - self.x)
            if(a == int(a)):
                a = int(a)
        except ZeroDivisionError as err:
            print(err)
            return (self.x,0)
        else:
            b= self.y - self.x *a
            return(a,b)

print(Point(3, 5).reflect_x()) #Point(3,-5)
print(Point(4, 10).slope_from_origin()) #2.5
print(Point(4, 11).get_line_to(Point(6, 15))) #(2,3)
point1 = Point(1,2)
point2 = Point(1,2)
point3 = Point(2,1)
print(point1 == point2)
print(point1 != point3)
print(Point(4,0).slope_from_origin())
print(Point(3,4).get_line_to(Point(3,5))) # x = 3
print(Point(3,6).get_line_to(Point(5,6)))

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at Point posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(
            self.corner, self.width, self.height)
    
    def __repr__(self):
        return  "Rectangle({0}, {1}, {2})".format(
            repr(self.corner), self.width, self.height)
    
    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2*(self.width + self.height)
    
    def flip(self):
        temp = self.width
        self.width = self.height
        self.height = temp
        
    def contains(self, other):
        if(self.corner.x <= other.x and other.x < self.corner.x + self.width):
            if(self.corner.y <= other.y and other.y <self.corner.y+self.height):
                return True
        return False

r = Rectangle(Point(100, 50), 10, 5)
test(r.area() == 50)
test(r.perimeter() == 30)
r.flip()  
test(r.width == 5 and r.height == 10) #ok
print('-'*15)
r = Rectangle(Point(0, 0), 10, 5)
test(r.contains(Point(0, 0)))
test(r.contains(Point(3, 3)))
test(not r.contains(Point(3, 7)))
test(not r.contains(Point(3, 5)))
test(r.contains(Point(3, 4.99999)))
test(not r.contains(Point(-3, -3)))