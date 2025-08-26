# Python credit card validator program

# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
# (If result is a two-digit number,
# add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid

# replace fun and using list
while True:
    card_num = input("Enter the credit card numbers with - or spaces between every fourd digits please , or q to exit : ")
    if card_num.lower() == "q":
        print("exited..")
        break
    card_num = card_num.replace("-","").replace(" ","")


    if not card_num.isdigit():
        print("Invalid input. Only digits are allowed!")
        continue

    card_num_list = [int(x) for x in card_num]

    total_odds = sum(card_num_list[-1::-2])
    total_evSecond = 0
    for x in card_num_list[-2::-2]:
        doubled = x * 2
        if doubled >=10:
            total_evSecond += 1 + (doubled % 10)
        else:
            total_evSecond += doubled




    isvalid = (total_odds + total_evSecond)
    print(f"The number you enterd is : {card_num}")
    if isvalid % 10 == 0:
        print("It is valid ✅")
    else:
        print("It is not valid 🚫")

