from arithmatic import add,sub,mul,div
from geometry import area_of_circle, peri_of_rec



print("Choose one:\n 1.Arithmetic operation\n2.Geometric Operation\n")
n=int(input("Select: "))

if n==1:
    print("Choose operation to perform: \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    m=int(input())
    if m==1:
        a=int(input("Enter value of a: "))
        b=int(input("Enter value of b: "))
        print(f"{a} + {b} = {add(a,b)}")
    
    elif m==2:
        a=int(input("Enter value of a: "))
        b=int(input("Enter value of b: "))
        print(f"{a} - {b} = {sub(a,b)}")
        
    elif m==3:
        a=int(input("Enter value of a: "))
        b=int(input("Enter value of b: "))
        print(f"{a} x {b} = {mul(a,b)}")
    elif m==4:
        a=int(input("Enter value of a: "))
        b=int(input("Enter value of b: "))
        print(f"{a} x {b} = {div(a,b)}")
        
    else:
        print("Invalid choice")
        
elif n==2:
    print("Choose operation to perform: \n1.Area of circle\n2.Perimeter of rectangle")
    m=int(input())
    if m==1:
        r=int(input("Enter value of radius: "))
        print(f"The area of the circle is {area_of_circle(r)}")
    
    elif m==2:
        l=int(input("Enter value of length: "))
        b=int(input("Enter value of breadth: "))
        print(f"The perimeter of the rectangle is {peri_of_rec(l,b)}")


