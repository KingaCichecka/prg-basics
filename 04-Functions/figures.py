# figures.py
import turtle

def draw_square(length: int) -> None:
    """Draw a square with side = length using the active turtle."""
    pen = turtle.Turtle()
    pen.speed(5)
    for _ in range(4):
        pen.forward(length)
        pen.right(90)
    pen.hideturtle()
