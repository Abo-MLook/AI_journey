import turtle


window = turtle.Screen()

sam = turtle.Turtle()
sam.shape("turtle")
sam.speed(8
          )
distance = 5
sam.up() # remove the line drawing
sam.stamp()  # leave an impression on the canvas
sam.forward(300)
for _ in range(30):
    sam.stamp()  # leave an impression on the canvas
    sam.forward(distance)
    sam.right(25)
    distance +=5

window.exitonclick()

