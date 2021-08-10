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
    size(1600,900)
    #fullScreen()
    
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
    #noFill()
    
    #a un punto lo define 
    #la coordenada donde se ubica
    #en el formato (x, y)
    #de acuerdo al sistema de
    #coordenadas de processing
    point(150, 200)
    
    for i in l:
        point(i, 500)
