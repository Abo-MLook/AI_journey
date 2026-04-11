try:
    n1 = int(input("Enter n1: "))
    n2 = int(input("Enter n2: "))
    n3 = int(input("Enter n3: "))
    print(f"The max number is {max(n1, n2, n3)}")
    print(f"The min number is {min(n1, n2, n3)}")
    print(f"The the sum number is {sum([n1,n2,n3])}")



except:
    print("You did not enter an integer")



