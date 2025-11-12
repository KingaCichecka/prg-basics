# draw_figures.py
import turtle
from figures import draw_square

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Draw
draw_square(100)   # <- tu zmieniasz długość boku

# Keep window open
window.mainloop()
