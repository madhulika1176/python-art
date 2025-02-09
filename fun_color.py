import colorsys
import turtle

screen=turtle.Screen()
screen.bgcolor("black")

t=turtle.Turtle()
t.speed(1000)
t.hideturtle()
num_colors = 36
steps = 1000
side_length = 500
angle = 155

hue = 0
for i in range(steps):
    color = colorsys.hsv_to_rgb(hue,1,1.0)
    hue += 1/num_colors
    t.color(color)
    t.left(angle)

    for _ in range(5):
        t.forward(side_length)
        t.left(150)


