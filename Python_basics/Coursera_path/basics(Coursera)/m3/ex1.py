rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
num = rainfall_mi.split(", ")
print(num)
num_three = [x for x in num if float(x)>3]
print(num_three)


sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
lsentence = sentence.split(" ")
print(lsentence)

numsentecne = [x for x in lsentence if x[0] == x[-1]]
print(numsentecne)
same_letter_count =len(numsentecne)
print(same_letter_count)



items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0
for x in items:
    if 'w' in x:
        acc_num +=1

print(acc_num)

s = "hello"
#s[0] = "H"  # This will raise an error because strings are immutable
t = (1, 2, 3)
#t[0] = 4  # This will raise an error because tuples are immutable