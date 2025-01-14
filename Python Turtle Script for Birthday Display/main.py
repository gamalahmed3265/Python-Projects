import turtle

class BirthdayDisplay:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.screen = turtle.Screen()
        self.screen.bgcolor("#282c34")  # Dark background
        self.screen.title(f"Birthday Celebration for {self.name}!")

    def draw_balloon(self, x, y, color):
        """Draws a balloon at a given position with a given color."""
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(color)
        turtle.begin_fill()
        turtle.circle(20)  # Balloon size
        turtle.end_fill()
        turtle.penup()
        turtle.goto(x, y - 20)
        turtle.pendown()
        turtle.color("black")
        turtle.setheading(-90)
        for _ in range(10):  # String for the balloon
            turtle.forward(5)
            turtle.penup()
            turtle.forward(5)
            turtle.pendown()

    def draw_cake(self):
        """Draws a birthday cake."""
        # Base layer
        turtle.penup()
        turtle.goto(-50, -50)
        turtle.pendown()
        turtle.color("peru")
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
        turtle.end_fill()

        # Top layer
        turtle.penup()
        turtle.goto(-30, 0)
        turtle.pendown()
        turtle.color("lightpink")
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(60)
            turtle.left(90)
            turtle.forward(30)
            turtle.left(90)
        turtle.end_fill()

        # Candles
        turtle.penup()
        turtle.goto(-20, 30)
        turtle.color("yellow")
        for _ in range(4):  # Four candles
            turtle.pendown()
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(5)
                turtle.left(90)
                turtle.forward(20)
                turtle.left(90)
            turtle.end_fill()
            turtle.penup()
            turtle.forward(15)

    def write_text(self):
        """Writes the birthday message."""
        # "Happy [Age]th Birthday!"
        turtle.penup()
        turtle.goto(-150, -250)
        turtle.color("#00ff00")  # Bright green
        turtle.write(f"Happy {self.age}th Birthday!", font=("Courier", 24, "bold"), align="center")

        # Name
        turtle.penup()
        turtle.goto(-150, -300)
        turtle.color("#ff4500")  # Orange-red
        turtle.write(self.name, font=("Courier", 20, "bold"), align="center")

    def run(self):
        """Runs the program to display the birthday celebration."""
        # Draw balloons
        self.draw_balloon(-100, 100, "#61afef")  # Blue
        self.draw_balloon(0, 150, "#98c379")    # Green
        self.draw_balloon(100, 100, "#e06c75")  # Red

        # Draw cake
        self.draw_cake()

        # Write text
        self.write_text()

        turtle.hideturtle()
        self.screen.mainloop()


if __name__ == "__main__":
    # Replace "Gamal Ahmed" and 24 with the desired name and age
    display = BirthdayDisplay(name="Gamal Ahmed", age=24)
    display.run()
