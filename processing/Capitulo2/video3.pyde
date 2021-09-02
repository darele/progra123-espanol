l = []

a, b = [1, 1]
c = a + b
l.append(a)
l.append(b)

for i in range(18):
    c = a + b
    l.append(c)
    a = b
    b = c
    
print(l)

def setup():
    #Define el tamaño del sketch
    size(1600,900)

    #Para poner el sketch a pantalla completa
    #se puede usar la siguiente función
    #fullScreen()

    #Con esta función definimos el color del sketch
    #se puede con RGB, hexadecimal o escala de grises 0-255
    background(97,213,229)

    #esta funcion define el 
    #color del lineado
    #le pasamos 0-255 o rgb
    stroke(0)

    #esta define el grosor
    #del lineado le pasamos
    #enteros
    strokeWeight(10)

    #define el color de la figura
    #le pasamos 0-255 o rgb
    fill(255)
    
    #solo se llama
    #sirve para hacer cualquier figura
    #transparente
    #noFill()
    
    #a un punto lo define 
    #la coordenada donde se ubica
    #en el formato (x, y)
    #de acuerdo al sistema de
    #coordenadas de processing
    point(150, 200)

    #Puntos puestos segun la sucesion de Fibonacci    
    for i in l:
        point(i, 500)
