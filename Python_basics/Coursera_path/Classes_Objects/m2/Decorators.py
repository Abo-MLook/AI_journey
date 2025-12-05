def addBeep(cls):
    cls.beep = lambda self: print(f"{self.model} says 'Beep!'")
    return cls

@addBeep
class Car:
    def __init__(self, make, model, color, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.mileage = mileage

mustang = Car("Ford", "Mustang", "blue", 0)
mustang.beep() # Mustang says 'Beep!'


print()
def addLogging(func): # The argument, func is a method of a class

    def wrapper(self, x): # x is the argument that we're going to pass to func
        print(f"About to call the method with argument {x}")
        result = func(self, x) # actually call the method and store the result
        print(f"Done with the method invocation with argument {x} on instance {self}. Result: {result}")
        return result # return whatever our function returned

    return wrapper # return our new function

class Car:
    def __init__(self, make, model, color, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.mileage = mileage

    @addLogging
    def drive(self, miles):
        self.mileage += miles
        return self.mileage

    @addLogging
    def rePaint(self, color):
        self.color = color

    def __str__(self):
        return(f"***{self.color} {self.make} {self.model} with {self.mileage} miles***")

corvette = Car("Chevrolet", "Corvette", "red", 50)

corvette.drive(100)
print("-"*20)
corvette.rePaint("blue")
print("-"*20)
corvette.drive(6)
