
#ex1 ---
class Bike:

    def __init__(self,color:str,price:float):
        self.color = color
        self.price = price


testOne  = Bike("blue",89.99)
testTwo = Bike("purple",25.0)



#ex2 ---

class AppleBasket :

    def __init__(self, color: str, quantity : int):
        self.apple_color  = color
        self.apple_quantity = quantity
    def increase(self):
        self.apple_quantity +=1
    def __str__(self):
        return f"A {self.apple_color} of {self.apple_quantity} blue apples."




#ex3 ---
class BankAccount  :

    def __init__(self, name : str, money  : int):
        self.name   = name
        self.amt = money
    def increase(self):
        self.apple_quantity +=1
    def __str__(self):
        return f"Your account, {self.name}, has {self.amt} dollars."
b = BankAccount("Bob",100)