# -*- coding: utf-8 -*-


# Esta serie limita la memoria no ingrese un numero mayor a 50
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input('Any number < 50 : '))

for n in range(1, n):
    print(n, ":", fibonacci(n))


if __name__ == '__main__':
    fibonacci(n)

# Esta serie utiliza la memoria cache escribe el numero 1000
# Memoization idea:Cache values
fibonacci_cache = {}


def fibonacci_2(m):
    # if we have cached the value, then return it
    if m in fibonacci_cache:
        return fibonacci_cache[m]
    if m == 1:
        value = 1
    elif m == 2:
        value = 1
    elif m > 2:
        value = fibonacci_2(m-1) + fibonacci_2(m-2)

    fibonacci_cache[m] = value
    return value


m = int(input('Write any number > 500 and < 1000: '))


for m in range(1, m):
    print(m, ":", fibonacci_2(m))


if __name__ == '__main__':
    fibonacci_2(m)


# Esta forma llama a la funcion lru_cache
from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci_3(c):
    if c == 1:
        return 1
    elif c == 2:
        return 1
    elif c > 2:
        return fibonacci_3(c-1) + fibonacci_3(c-2)


c = int(input('Write any numbre > 1000: '))
for c in range(1, c):
    print(c, ":", fibonacci_3(c))


if __name__ == '__main__':
    fibonacci_3(c)


# Esta serie viene con restricciones de type correcto
@lru_cache(maxsize=1000)
def fibonacci_4(r):
    # Check that the input is a positive integer
    if type(r) != int:
        raise TypeError('r no debe ser flotante')
    if r < 1:
        raise ValueError('r debe ser positivo')
    if r == 1:
        return 1
    elif r == 2:
        return 1
    elif r > 2:
        return fibonacci_4(r-1) + fibonacci_4(r-2)


r = int(input('Write any numbre : '))
for r in range(1, r):
    print(r, ":", fibonacci_4(r))


if __name__ == '__main__':
    fibonacci_4(r)
