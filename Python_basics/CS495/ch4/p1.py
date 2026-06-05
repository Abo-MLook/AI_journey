import sqlite3 as sq


conn = sq.connect("student.db")

cur = conn.cursor()


# cur.execute("""
# CREATE TABLE student(
#id INTEGER,
#name TEXT,
#age INTEGER

#)
# """)


cur.execute("INSERT INTO student VALUES (2,'Ahmed',17),(1, 'Ali', 20)")

conn.commit()




## printing the data

cur.execute("SELECT * FROM student")

d = cur.fetchall()
for a in d:
    print(a,end='\n')

for a in d:
    print("ID",a[0])
    print("name", a[1])
    print("age", a[2])
    print()