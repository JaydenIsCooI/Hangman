import turtle


class HangmanTurtle:
    def __init__(self, canvas):
        super().__init__()
        self.pen = turtle.RawTurtle(canvas)
        self.pen.speed("fastest")
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.goto(-150, -75)
        self.pen.pendown()

    def draw_gallows(self):
        self.pen.pensize(3)
        self.pen.goto(-50, -75)
        self.pen.goto(-100, -75)
        self.pen.goto(-100, 150)
        self.pen.goto(50, 150)
        self.pen.goto(50, 100)
        self.pen.penup()

    def draw_man(self, num_wrong_guesses):
        if num_wrong_guesses == 1:
            self.pen.goto(50, 50)
            self.pen.pendown()
            self.pen.circle(25)
            self.pen.penup()
        if num_wrong_guesses == 2:
            self.pen.goto(50, 50)
            self.pen.pendown()
            self.pen.goto(50, -15)
        if num_wrong_guesses == 3:
            self.pen.goto(25, -65)
            self.pen.goto(50, -15)
        if num_wrong_guesses == 4:
            self.pen.goto(75, -65)
            self.pen.penup()
            self.pen.goto(50, 15)
            self.pen.pendown()
        if num_wrong_guesses == 5:
            self.pen.goto(25, 40)
            self.pen.goto(50, 15)
        if num_wrong_guesses == 6:
            self.pen.goto(75, 40)
            self.pen.goto(50, 15)
