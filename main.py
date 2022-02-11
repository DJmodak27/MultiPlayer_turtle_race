from turtle import Turtle,Screen

timmy=Turtle()
screen=Screen()
timmy.shape("turtle")
timmy.color("blue")
def move_forward():
    timmy.forward(20)
def move_backward():
    timmy.backward(20)
def move_counterclockwise():
    timmy.circle(60,180,50)
def move_clockwise():
    timmy.circle(-60,270,10)
def clear():
    timmy.home()
    timmy.clear()

screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward,key="s")
screen.onkey(fun=move_counterclockwise, key="a")
screen.onkey(fun=move_clockwise,key="d")
screen.onkey(fun=clear,key="c")
screen.exitonclick()