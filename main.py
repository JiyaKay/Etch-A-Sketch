from turtle import Turtle, Screen

cookie = Turtle()
screen = Screen()
# Sets focus on TurtleScreen, in order to collect key-events
screen.listen()


def move_forward():
    cookie.forward(10)


def move_backward():
    cookie.backward(10)


def move_counter_clockwise():
    cookie.left(10)


def move_clockwise():
    cookie.right(10)


def clear_screen():
    cookie.setposition(0, 0)
    cookie.clear()


screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_counter_clockwise, key="a")
screen.onkey(fun=move_clockwise, key="d")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()
