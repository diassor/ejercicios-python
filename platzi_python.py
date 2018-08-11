'''import turtle
window = turtle.Screen()
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange', 'black']
t = turtle.Pen()
t.speed(0)
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)
turtle.mainloop()


def main():
    window = turtle.Screen()
    colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange', 'black']
    t = turtle.Pen()
    t.speed(0)
    turtle.mainloop()


for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

if __name__ == '__main__':
    main()




def edwin():
    ventana = turtle.Screen()
    dave = turtle.Turtle()
    make_square(dave)
    turtle.mainloop()


def make_square(dave):  # define la funcion de como se debe usar
    length = int(59)  # (input('Tamano del cuadrado: '))

    for i in range(4):
        make_line_and_turn(dave, length)


def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)


if __name__ == '__main__':  # primero ejecuta lo que esta en el bukle
    edwin()



def edwin():
    window = turtle.Screen()
    ale = turtle.Turtle()
    make_square(ale)
    turtle.mainloop()


def make_square(ale):
    turn = 0
    tamano = input('Insert lenght: ')
    length = int(tamano)
    while turn < 3:
        turn = input('Insert number of sides of your figure: ')
        turn = int(turn)
        if turn < 3:
            print('The minimum number of sides is 3')
    angle = 360/turn

    for i in range(turn):
        ale.forward(length)
        ale.left(angle)


if __name__ == '__main__':
    edwin()
'''


def say_hello(age):
    if (age >= 18) and (age <= 40):
        print('Hi mister')
    elif (age >= 41) and (age <= 50):
        print('Hi Milf')
    elif (age >= 51) and (age <= 100):
        print('Hi older')
    else:
        print('Hi boy')
    return


say_hello(int(input('Ingrese su edad: ')))
