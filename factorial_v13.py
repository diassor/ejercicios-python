# -*- coding: utf-8 -*-


'''def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number-1)


if __name__ == '__main__':
    number = int(input('Write any number: '))

    result = factorial(number)
    print(result)'''
'''if (type(n)) != (type(1)):
    print('Solo numeros enteros')
    return -1
elif n < 0:
    print('solo numeros positivos y enteros')
    return -1'''


def fact(n):
    if (n != 1) and (n < 0):
        print('Only whole numbers and postive')
    elif n == 0:
        return 1
    else:
        return n * fact(n-1)


n = float(input('Write any number: '))
result = fact(n)
print(result)


if __name__ == '__main__':
    fact(n)
