import re
from random import *
from turtle import *

'''intercambios = {
    'prob1': '1F1',
    'prob2': '2F2',
    'prob3': '3F3'
}'''

intercambios = {
    'prob1': 'F[+F]F[-F]F',
    'prob2': 'F[+F]F',
    'prob3': 'F[-F]F'
}

probabilidades = {
    'prob1': 0.333,
    'prob2': 0.33,
    'prob3': 0.34
}

def aleatorio():
    return random()

def leerArchivo():
    try:
        with open('inicial.txt', 'r') as f:
            txt = f.read()
            f.close()
            return txt
    except FileNotFoundError:
        with open('inicial.txt', 'w') as f:
            f.write('F')
            f.close()
        return 'F'

def guardarArchivo(txt):
    try:
        with open('final.txt', 'w') as f:
            f.write(txt)
        return True
    except FileNotFoundError:
        with open('final.txt', 'w') as f:
            f.write(txt)
        return True
    
def ingresarIteraciones():
    while True:
        iteraciones = input('Ingresa el numero de iteraciones: ')
        try:
            iteraciones = int(iteraciones)
            if iteraciones < 0:
                print('El numero de iteraciones debe ser un numero positivo.')
            else:
                return iteraciones
        except ValueError:
            print('El numero de iteraciones debe ser un numero entero')

def intercambiarVariables(valor, txt, i):
    try:
        with open('log.txt', 'a') as f:
            pass
    except FileNotFoundError:
        with open('log.txt', 'w') as f:
            f.write('')
            f.close()
    
    if valor < probabilidades['prob1']:
        txt = re.sub('F', intercambios['prob1'], txt)
    elif valor < (probabilidades['prob1'] + probabilidades['prob2']):
        txt = re.sub('F', intercambios['prob2'], txt)
    else:
        txt = re.sub('F', intercambios['prob3'], txt)
                
    with open('log.txt', 'a') as f:
        f.write('iteracion {i} | random: {valor:.2f} | {txt} \n'.format(i=i, valor=valor, txt=txt))
    f.close()
    return txt


def iterar(iteraciones, txt):
    for i in range(0, iteraciones): 
       txt = intercambiarVariables(aleatorio(),txt, i)
    return txt







if __name__ == '__main__':  
    
    
    txt = leerArchivo()

    with open('log.txt', 'w') as f:
        pass

    if not txt:
        print('Error: No se puede leer el archivo.')

    cadenaFinal = iterar(ingresarIteraciones(), txt)

    guardarArchivo(cadenaFinal)

    print(cadenaFinal[2])

    t = Turtle()
    t.speed(0)

    posicion = (0,0)
    angle = 0
    t.screen.title("hermosa planta estoica")
    t.setheading(90)
    
    
    for i in cadenaFinal:

        if i == 'F':
            t.forward(uniform(0.7, 1.2)*10)
        elif i == '+':
            t.right(uniform(0, 30))
        elif i == '-':
            t.left(uniform(0, 30))
        elif i == '[':
            angle = t.heading()
            posicion = t.position()
        elif i == ']':
            t.setheading(angle)
            t.goto(posicion)


    t.screen.mainloop()

    #hay que hacerlo recursivo, cuando encontramos un ] volvemos a la iteracion anterior


    