import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# Number of colors in the rainbow
colors = 360
hue = 0

# Draw colorful spiral
for i in range(360):
    # Convert HSV to RGB
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    pen.color(color)
    
    # Draw the spiral pattern
    pen.forward(i * 3 / colors + i)
    pen.left(59)
    pen.circle(i * 0.1, 60)
    
    # Change hue
    hue += 1 / colors

pen.hideturtle()
turtle.done()
