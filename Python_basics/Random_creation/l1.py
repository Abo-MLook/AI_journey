while True:
    n = input("enter a number to convert to hex (E to Exit): ")

    if n == "E":
        print("Exiting...")
        break

    try:
        n = int(n)   # convert to integer
    except:
        print("you did not enter an integer")
        continue

    print("number in hex is:", hex(n))
    print("number in binary is:", bin(n))