import string
import random
from operator import index
# good for College projects
chars = " " + string.punctuation +  string.ascii_letters + string.digits
chars = list(chars)
print(chars)

key = chars.copy()
random.shuffle(key)
print(key)

encrypted =""
decrypted =""

message = input("Enter a message to encrypt : ")

for letter in message:
    index1 = chars.index(letter)
    encrypted+= key[index1]

print(f"encrypted message : {encrypted}")


message = input("Enter a message to decrypt : ")
for letter in encrypted:
    index1 = key.index(letter)
    decrypted+=chars[index1]

print(f"decrypted message : {decrypted}")
