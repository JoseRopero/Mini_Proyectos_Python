from turtle import Turtle, Screen


def move_forward():
    t.fd(10)


def move_backward():
    t.bk(10)


def move_left():
    t.left(10)


def move_right():
    t.rt(10)


def clear_screen():
    t.reset()


t = Turtle()
s = Screen()
s.listen()
s.onkey(key="w", fun=move_forward)
s.onkey(key="s", fun=move_backward)
s.onkey(key="a", fun=move_left)
s.onkey(key="d", fun=move_right)
s.onkey(key="c", fun=clear_screen)
s.exitonclick()
