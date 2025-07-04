from operator import index

St_ = input("Enter a long string : ")

len_string = len(St_)

upp = St_.upper()
low = St_.lower()

dig = St_.isdigit()
let = St_.isalpha()
dig_let = St_.isalnum()

firstSpace = St_.find(" ") # find index of first space
countSpace = St_.count(" ") # count spaces

replaceSpace = St_.replace(" ","-")

print(f"length :{len_string} \nis it digit ? {dig} \n is it letters ? {let} \n is it mixed ? {dig_let} \n first space in index : {firstSpace} \n numbers of spaces : {countSpace} \n "
      f" The string in upper case : {upp} \n The string in lower case : {low} \n replacing space with (-) : {replaceSpace} ")


#-- print(help(str)) # all fun on strings

#exercise   :
# 1- only 12 and less char   2- no spaces  3-no digit
username = input("Enter a user name : ")
if len(username) > 12:
    print("invaild only 12 and less characters")
elif username.count(" ") > 0 :
    print("invalid no spaces please")
elif not username.isalpha():
    print("Do not enter digits please")
else:
    print("created successfully! ")


#indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]

number = "1234-567-890"
print(number[0:4])
print(number[0:])
print(number[:11])
print(number[::2])
print(number[-4:])
print(number[::-1])


#entering an email :
email = input("Enter an email : ")
Hindex = email.index("@")
username = email[:Hindex]
domain = email[Hindex + 1 :]
print(f"The user name is {username} , The domain is {domain}")