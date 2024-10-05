import turtle


def get_depth():
    while True:
        depth = input(
            "Enter the depth of the fractal (number between 0 an 6): ")
        if depth.isdigit() and int(depth) <= 6:
            depth = int(depth)
            if depth >= 0:
                return depth
            else:
                print("Please enter a number!")
        else:
            print("Input must be a number between 0 and 6!")


def koch_curve(t: turtle, depth: int, size: int):
    if depth == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, depth - 1, size / 3)
            t.left(angle)


def draw_koch_curve(depth: int, size: int = 600):

    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3 + 20)
    t.pendown()

    for _ in range(3):
        koch_curve(t, int(depth), size)
        t.right(120)

    window.mainloop()


draw_koch_curve(get_depth())
