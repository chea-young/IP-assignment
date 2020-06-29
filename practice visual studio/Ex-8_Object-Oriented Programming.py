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
                
    def issubset(self, other):
        for x in self.data:
            if(x not in other.data):
                return False
        return True
            
    def __le__(self,other):
        return self.issubset(other)
    
    def __lt__(self,other):
        if(self.issubset(other)):
            if(self.data != other.data):
                return True
        return False
    
    def issuperset(self,other):
        for x in other.data:
            if(x not in self.data):
                return False
        return True
    
    def __ge__(self,other):
        return self.issuperset(other)
    
    def __gt__(self,other):
        if(self.issuperset(other)):
            if(self.data != other.data):
                return True
        return False
    
    def update(self,other):
        for x in other.data:
            if(x  not in self.data):
                self.data.append(x)
    
    def __ior__(self, other):
        #self.data = self.concat(other.data)
        self.update(other)
        return self
    
    def intersection_update(self, other):
        self.data  = self.intersection(other)
        
    def __iand__(self, other):
        self.intersection_update(other)
        return self
    
    def difference_update(self, other):
        self.data = [x for x in self.data if x not in other.data]
        
    def  __isub__(self,other):
        self.difference_update(other)
        return self
    
    def symmetric_difference_update(self, other):
        union = self.union(other).data
        inter = self.intersection(other).data
        self.data = [x for x in union if x not in inter]
    
    def __ixor__(self,other):
        self.symmetric_difference_update(other)
        return self
    
    def add(self, elem):
        if(elem not in self.data):
            self.data.append(elem)
        
    def remove(self,elem):
        try:
            self.data.remove(elem)
        except ValueError as err:
            print(err)
            print('element not in the set')
            
    
    def __len__(self):          return len(self.data)        # len(self)
    def __getitem__(self, key): return self.data[key]        # self[i], self[i:j]
    def __and__(self, other):   return self.intersection(other) # self & other
    def __or__(self, other):    return self.union(other)     # self | other
    def __repr__(self):         return 'Set({})'.format(repr(self.data))  
    def __iter__(self):         return iter(self.data)       # for x in self:

    
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
print(c)
print('-'*15)

f = Set([1,2,4,5])
f |=(d)
print(f)
print('-'*15)
b.intersection_update(d)
print(b)
c &= d
print(c)
print('-'*15)
g1 = Set([3,4,9,4,5])
g2 = Set([3,4,9,4,5])
g1.difference_update(d)
print(g1)
g2 -= d
print(g2)
print('-'*15)
h1 = Set([1,9,3])
h2 = Set([1,9,3])
h1.symmetric_difference_update(d)
print(h1)
h2 ^= d
print(h2)
print('-'*15)
c.remove(6)