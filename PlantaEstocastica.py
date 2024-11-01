import re
import random

intercambios = {
    'prob1': 'F[+F]F[-F]F',
    'prob2': 'F[+F]F',
    'prob3': 'F[-F]F'
}

probabilidades = {
    'prob1': 0.34,
    'prob2': 0.33,
    'prob3': 0.33
}

def aleatorio():
    return random.random()

def leerArchivo():
    with open('inicial.txt', 'r') as f:
        txt = f.read()
        f.close()   
        return txt

def guardarArchivo(txt):
    with open('final.txt', 'w') as f:
        f.write(txt)
        f.close()
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



def iterar(iteraciones, txt):
    for i in range(0, iteraciones):
        
        valor = aleatorio()
        
        with open('log.txt', 'a') as f:
            
            if valor < probabilidades['prob1']:
                txt = re.sub('F', intercambios['prob1'], txt)
            elif valor < (probabilidades['prob1'] + probabilidades['prob2']):
                txt = re.sub('F', intercambios['prob2'], txt)
            else:
                txt = re.sub('F', intercambios['prob3'], txt)
            
            f.write('iteracion {i} | random: {valor:.2f} | {txt} \n'.format(i=iteraciones, valor=aleatorio(), txt=txt))
    
    f.close()
    return txt

if __name__ == '__main__':
    
    txt = leerArchivo()

    with open('log.txt', 'w') as f:
        pass

    if not txt:
        print('Error: No se puede leer el archivo.')

    guardarArchivo(iterar(ingresarIteraciones(), txt))

    