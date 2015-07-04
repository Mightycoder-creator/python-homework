import turtle

import colorsys

jagger = turtle.Turtle()
window = turtle.Screen()

turtle.title("She's A Rainbow")


def drawRainbow():

  for i in range(1000):

      color = colorsys.hsv_to_rgb(i/1000.0, 1.0, 1.0)
      jagger.color(color)
      jagger.forward(i)
      jagger.right(98)

drawRainbow()

window.exitonclick()