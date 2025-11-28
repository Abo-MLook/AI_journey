
# simple class
class Person:
    # similar to a constructor (__init__ runs when creating an object)
    def __init__(self, name=0, age=0, gender=0):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        print(f"Hello my name is {self.name} , I am {self.age} old")

    def get(self):
        print(f"name : {self.name}\nage : {self.age}\ngender : {self.gender}")


ob1 = Person("Mrwan", 18, "male")
ob2 = Person("Salah", 51, "male")
ob3 = Person()

ob1.greet()
ob1.get()
ob2.greet()
ob2.get()

# ===========================
# 🔍 What is Inheritance?
# Inheritance means that a child class (subclass) can reuse the code from a parent class (superclass).
# ➡️ The child class inherits all methods and attributes of the parent class.
# ➡️ The child class can also add new methods or override existing ones.


class Student(Person):
    def __init__(self, name, age, gender, id, GPU):
        super().__init__(name, age, gender)   # use the Inherit class to declare them
        self.id = id
        self.GPU = GPU

    def get(self):
        print("\n\nStudent info :\n")
        super().get()                      # print the get from parent class (Person)
        print(f"id : {self.id}\nGPU : {self.GPU}")


ob3 = Student("Mrwan Alayed", 21, "MALE", 431107769, 4.98)
ob3.greet()
ob3.get()
