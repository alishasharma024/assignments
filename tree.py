import turtle

# Set up the turtle
tu = turtle.Turtle()
tu.screen.bgcolor("white")
tu.pensize(2)
tu.color("green")
tu.left(90)
tu.speed(200)
tu.shape("turtle")

# Recursive function to draw the tree
def tree(i):
    if i < 10:
        return
    else:
        tu.forward(i)
        tu.color("orange")  # Draw the tip
        tu.dot(5)  # Use dot to represent the tip instead of circle
        tu.color("brown")  # Draw the branches
        tu.left(30)
        tree(3 * i / 4)
        tu.right(60)
        tree(3 * i / 4)
        tu.left(30)
        tu.backward(i)

# Start drawing the tree
tree(100)

# Finish drawing
turtle.done()
