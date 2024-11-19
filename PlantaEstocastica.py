import re
from random import uniform, random
from turtle import Screen, Turtle
import colorsys

# DEFINICION DE VARIABLES
intercambios = {    # REGLAS PARA REMPLAZAR EL CARACTER F
    'prob1': 'F[+F]F[-F]F',
    'prob2': 'F[+F]F',
    'prob3': 'F[-F]F'
}

probabilidades = {  # POSIBILIDADES ASOCIADAS A LAS REGLAS DE REMPLAZO
    'prob1': 0.333,
    'prob2': 0.33,
    'prob3': 0.34
}

def aleatorio():
    return random()

''' Lee el contenido del archivo inicial.txt '''
def leerArchivo():
    try:
        with open('inicial.txt', 'r') as f:
            return f.read()
    except FileNotFoundError:
        with open('inicial.txt', 'w') as f: 
            f.write('F') # Si no existe lo crea con el contenido f
        return 'F'

''' Guarda el archivo generado en final.txt '''
def guardarArchivo(txt):
    with open('final.txt', 'w') as f:
        f.write(txt)

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

# MANIPULACION DE LA CADENA

def intercambiarVariables(valor, txt, i):
    if valor < probabilidades['prob1']:     # Usa valor aleatorio para decidir la regla de remplazo.
        txt = re.sub('F', intercambios['prob1'], txt)
    elif valor < (probabilidades['prob1'] + probabilidades['prob2']):
        txt = re.sub('F', intercambios['prob2'], txt)
    else:
        txt = re.sub('F', intercambios['prob3'], txt)

    with open('log.txt', 'a') as f:
        f.write(f'Iteración {i} | random: {valor:.2f} | {txt} \n')
    return txt


def iterar(iteraciones, txt):
    for i in range(iteraciones):
        txt = intercambiarVariables(aleatorio(), txt, i) # Repite el proceso de remplazo el número de iteraciones dada.
    return txt

# GENERA COLOR RGB
def color_rainbow(paso, total_pasos):
    paso = paso / total_pasos  # Normalizar el paso
    r, g, b = colorsys.hsv_to_rgb(paso, 1.0, 1.0)  # Convertir HSV a RGB
    return r, g, b


def dibujo(cadena):
    stack = []
    total_pasos = len(cadena)
    paso = 0

    for char in cadena:
        paso += 1
        color = color_rainbow(paso, total_pasos)
        t.pencolor(color)

        if char == 'F':
            t.forward(uniform(0.7, 1.2) * 15) # Avanza la tortuga.
        elif char == '+':
            t.right(uniform(0, 30))   # Gira a la derecha un ángulo aleatorio.
        elif char == '-':
            t.left(uniform(0, 30))  # Gira a la izquierda un ángulo aleatorio.
        elif char == '[':
            angulo = t.heading()    
            posicion = t.position()
            stack.append((posicion, angulo))    # Guarda ángulo y posición
        elif char == ']':
            posicion, angulo = stack.pop()  # Restaura la última posición y angulo guardados.
            t.setheading(angulo)
            t.goto(posicion)

# CONFIGURACIÓN DE PANTALLA
def conf_turtle(s, t):
    s.setup(width=1.0, height=1.0)
    t.speed(0)
    t.screen.title("NYAN NYAN NYAN NYAN")
    t.setheading(90)  # Hacemos que mire para arriba
    t.pensize(2)
    t.penup()
    t.goto(0, -300)
    t.pendown()
    s.register_shape("gato.gif")
    s.bgpic("espacio.gif")
    t.shape("gato.gif")


def log(txt):
    # Borra contenido de log.txt
    with open('log.txt', 'w') as f:
        pass

    if not txt:
        print('Error: No se puede leer el archivo.')


if __name__ == '__main__':

    txt = leerArchivo()

    log(txt)
    cadenaFinal = iterar(ingresarIteraciones(), txt)  # Ejecuta iteraciones para generar la cadena fractal.
    guardarArchivo(cadenaFinal)

    s = Screen()
    t = Turtle()
    conf_turtle(s, t) # Configura el entorno grafico.
    dibujo(cadenaFinal) # Dibuja el resultado.
    t.screen.mainloop()
