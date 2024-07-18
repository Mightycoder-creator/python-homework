import turtle
import colorsys
jagger = turtle.Turtle()
window = turtle.Screen()
turtle.bgcolor("black")
jagger.speed(0)
turtle.title("She's A Rainbow")
def drawRainbow():

  for i in range(1000):
      color = colorsys.hsv_to_rgb(i/1000.0, 1.0, 1.0)
      jagger.color(color)
      jagger.forward(i)
      jagger.right(98)
  jagger.color("#ecf0f1")
  jagger.hideturtle()
  jagger.penup()
  jagger.setpos((20,0))
  jagger.write("Have you seen her dressed in blue?",True, align="center", font=("Sans", 26, "normal"))
drawRainbow()
window.exitonclick()
