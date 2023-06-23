from turtle import Turtle

class HomeScreen:
    def __init__(self):
        self.title = Turtle()
        self.start_button = Turtle()
        self.instructions = Turtle()

    def setup_main_screen(self):
        self.title.color("white")
        self.title.penup()
        self.title.goto(0, 100)
        self.title.write("-SNAKE-", align="center", font=("Courier", 40, "normal"))

        self.start_button.color("blue")
        self.start_button.shape("square")
        self.start_button.penup()
        self.start_button.goto(0, 0)
        self.start_button.shapesize(stretch_wid=1, stretch_len=4)
        self.start_button.write("Start", align="center", font=("Courier", 24, "bold"))

        self.instructions.color("white")
        self.instructions.penup()
        self.instructions.goto(0, -100)
        self.instructions.write("Use arrow keys to control the snake", align="center", font=("Arial", 12))

    def clear_main_screen(self):
        self.title.hideturtle()
        self.start_button.hideturtle()
        self.instructions.hideturtle()

        self.title.clear()
        self.start_button.clear()
        self.instructions.clear()
