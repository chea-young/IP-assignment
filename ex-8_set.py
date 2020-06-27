class Set:
    def __init__(self, value = []):    # Constructor
        self.data = []                 # Manages a list
        self.concat(value)

    def intersection(self, other):        # other is any sequence
        res = []                       # self is the subject
        for x in self.data:
            if x in other:             # Pick common items
                res.append(x)
        return Set(res)                # Return a new Set

    def union(self, other):            # other is any sequence
        res = self.data[:]             # Copy of my list
        for x in other:                # Add items in other
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:                
            if not x in self.data:     # Removes duplicates
                self.data.append(x)

    def __len__(self):          return len(self.data)        # len(self)
    def __getitem__(self, key): return self.data[key]        # self[i], self[i:j]
    def __and__(self, other):   return self.intersection(other) # self & other
    def __or__(self, other):    return self.union(other)     # self | other
    def __repr__(self):         return 'Set({})'.format(repr(self.data))  
    def __iter__(self):         return iter(self.data)       # for x in self:
    
    def issubset(self, other):
        if(len(self.data) <= len(other.data)):
            for element in self.data:
                if(element not in other.data):
                    return False
            return True
        return False

    def __le__(self, other):
        return self.issubset(other)
    
    def __lt__(self, other):
        if(len(self.data) < len(other.data)):
            return True
        return False

    def issuperset(self, other):
        if(len(self.data) >= len(other.data)):
            for element in other.data:
                if(element not in self.data):
                    return False
            return True
        return False
    
    def __ge__(self, other):  
        return self.issuperset(other)

    def ior (self,other):
        for element in other.data:
            if(element not in self.data):
                self.data.append(element)

    def __ior__ (self,other):
        self.ior(other)
        return self
        
    def intersection_updata(self, other):
        for element in other.data:
            if(element not in self.data):
                self.data.append(element)
        
    def __iand__(self, other): 
        self.intersection_updata(other)
        return self
    
    def difference_updata(self, other):
        for element in other.data:
            if(element  in self.data):
                self.data.remove(element)
    
    def __isub__(self, other):
        self.difference_updata(other)
        return self
    
    def symmetric_difference_updata(self, other):
        inter = list(self.intersection(other))
        for element in other.data:
            if(element not in self.data):
                self.data.append(element)
        for element in inter:
            if(element in self.data):
                self.data.remove(element)

    def __ixor__(self, other):
        self.symmetric_difference_updata(other)   
        return self
    
    def add(self, elem):
        self.data.append(elem)

    def remove(self, elem):
        try:
            self.data.remove(elem)
        except ValueError:
            raise KeyError

x = Set([1,3,5,7, 1, 3])
y = Set([2,1,4,5,6])
print(x, y, len(x))
print(x.intersection(y), y.union(x))
print(x & y, x | y)
print(x[2], y[:2])
for element in x:
    print(element, end=' ')
print()
print(3 not in y)  # membership test
print(list(x))   # convert to list because x is iterable
print()

a = Set([1,2,3,4,5])
b = Set([1,2,4])
c = Set([1,2,4])
d = Set([3,4,5])
print(a.issubset(b), b.issuperset(c))
print(a <= b, b >= c)
print(a<b, b>c)
c.add(9)
print(c)
c.remove(9)
f = Set([1,2,4,5])
f |=(d)
print(f)
b.intersection_updata(d)
print(b)
c &= d
print(c)
g1 = Set([3,4,9,4,5])
g2 = Set([3,4,9,4,5])
g1.difference_updata(d)
print(g1)
g2 -= d
print(g2)
h1 = Set([1,9,3])
h2 = Set([1,9,3])
h1.symmetric_difference_updata(d)
print(h1)
h2 ^= d
print(h2)
c.remove(6)