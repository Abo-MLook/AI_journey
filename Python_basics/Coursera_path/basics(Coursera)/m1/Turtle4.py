import turtle

# Set up the turtle
t = turtle.Turtle()

# Number of sides for a star
sides = 5
angle = 144  # The angle between lines for a star

# Draw the star
for _ in range(sides):
    t.forward(100)  # Move forward by 100 units
    t.right(angle)   # Turn right by 144 degrees

print(type(t))

# Finish drawing
