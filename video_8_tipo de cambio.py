# -*- coding: utf-8- -*-
def foreing_exchange_calculator(cantidad):
    usd_to_cop_rate = 2745.23

    return usd_to_cop_rate * cantidad


# si lo ubico abajo sale este error
'''File "video_8.py", line 12, in <module>
    resultado = foreing_exchange_calculator(cantidad)
NameError: name 'foreing_exchange_calculator' is not defined'''


def run():
    print('CALCULADORA DE DIVISAS')
    print('Convierte Dolares a pesos Colombianos')
    print('')  # se usa print vasio para dar espacios


cantidad = float(input('Dolares que quieres convertir:'))
# fuera de la funcion si esta dentro sale error
resultado = foreing_exchange_calculator(cantidad)


print('${} Dolares son ${} pesos Colombianos'.format(cantidad, resultado))
print('')


if __name__ == '__main__':
    run()
    print('Gracias por usas DIVISAS Edwin')
