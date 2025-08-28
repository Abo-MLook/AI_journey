mark = float(input("Enter your mark : "))
# The spaces in conditons in pytone is important , if you put space it will be inside the if as body , if you remove the space it will be outside
if mark >= 95 :
   grade = "A+"
#space  body
elif mark >=90:
    grade = "A"

elif mark >=85:
    grade = "B+"

elif mark >= 80 :
    grade = "B"

elif mark >= 75:
    grade = "D+"
elif mark >= 70:
    grade = "D"


else:
    grade = "F"

print(f"not valid mark" if mark > 100 or mark < 0 else f"your mark is {grade}")  # ternery condition

