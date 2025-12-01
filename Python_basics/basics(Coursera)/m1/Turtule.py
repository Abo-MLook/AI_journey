import turtle


window = turtle.Screen()

sam = turtle.Turtle()
for _ in range(4):
    sam.forward(50)
    sam.left(90)
distance = 10
sam.speed(10)
for _ in range(100):
    sam.forward(distance)
    sam.right(90)
    distance +=5

window.exitonclick()


