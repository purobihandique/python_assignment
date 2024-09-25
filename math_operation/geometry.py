import math

def area_of_circle(r):
    if r<0:
        print("radius cannot be negative")
        
    return math.pi *r**2

def peri_of_rec(l,b):
    if l<0 or b<0:
        print("Length and Breadth cannot be negative")
        
    return 2*(l+b)