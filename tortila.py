import turtle
def my_turtle():
    """

    :return:
    """
    step1 = int(input('Укажите длину стороны треугольника (10-100): '))
    step2 = int(input('Укажите длину стороны шестиугольника (20-150): '))


    turtle.shape('turtle')
    turtle.shapesize(2)
    turtle.color('green', 'yellow')

    for counter1 in range(6):
        turtle.begin_fill()
        for counter2 in range(3):
            turtle.forward(step1)
            turtle.left(360 / 3)
        turtle.end_fill()
        turtle.forward(step2)
        turtle.right(60)
if __name__ == '__main__':
    my_turtle()