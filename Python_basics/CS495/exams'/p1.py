

def sortdict(dic):
    l = [i for i in dic.keys() if i[0] =="p"]
    return l



def filedic(f):
    dic = {line:len(line.split()) for line in f}

    return dic



"""

#1
file1 = open("tra.txt","w")
file1.write("Hello")


#2
b1.config(bg = RED)

#3
all = cur.fetchall()


"""
class Product:
    def __init__(self,amount,price):
        self.amount = amount
        self.price = price

    def updateS(self,purch =1):
        self.amount -=purch
        return self.amount

    def disc(self,disprice=0):
        self.price -= disprice
        return  self.price





# 6.1

data = [f1.read()]


def textToDict(text):
    dict = {l:len(l) for l in text.split()}
    return  dict


def DictToTup(dict):
    lis = []
    for i in dict.keys():
        if dict[i]=="str" and  dict[i] not in lis
            lis.append(i)

    lis = tuple(lis)
    return lis


#6.1
t1=(20, )
#6.2
class Admin(User):
    def_init_(self, name):
        self.name = name


#6.4
Button1 = Button (top, text='show',command=display)

#6.5
data = cobj.fetchone()

#6.6
f= open("python.txt", "a")



#3.1
dt.commit()

#3.2
tup[0:3]

#3.3
s = list(s)


#3.4
l1.config(text = "changing")


#3.3
lis.sort(); lis = sorted(lis)

#3.6
f = open("name.txt","r").read()
real = []
for line in f:
    lis = line.split()
    if lis[1]<50:
        real.append(lis[0])

