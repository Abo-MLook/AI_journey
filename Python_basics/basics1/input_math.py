import math as M
# prog1----------------

print(M.pow(4,2))
width = int(input("Enter the width of length of square : "))
area = width * width
Perimeter = width * 4

print(f"area is :{area}\nPerimeter is : {Perimeter}")
"""

# prog2----------------
"""
item = input("Enter what item to buy : ")
price = float(input("Enter its price : "))
quantity = int(input("Enter how many want to buy : "))

total = price * quantity

print(f"You have bought  {item} X {quantity} \n total price : {round(total,2)}$")
"""

# prog3----------------
"""
r = float(input("Enter a radius : "))
circumference = r * M.pi * 2
area = (r**2) * M.pi
print(f"The circumference is : {round(circumference,2)}\nThe area is : {round(area,2)}")


# prog4----------------
a = float(input("Enter  a : "))
b = float(input("Enter  b : "))
c = M.sqrt(a**2 + b**2)
print(f"c is : {c:.2f}")