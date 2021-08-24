'''

size(400,400) #tamano del canvas
background(192,64,0) #color de fondo en rgb
stroke(255) #color dela linea en valor entero, tambien se puede hexadecimal
line(15,25,70,90) #Formato de linea, punto de inicio y punto final

'''

'''
# hacer una linea desde un punto fijo a donde esta el raton
def setup(): #corre solo una vez automaticamente
    size(400,400)#Esta siempre es la primera linea del setup
    stroke(255)
    
def draw(): #corre repetidamente
    background(192,64,0);#Esta linea hace que solo se vea una linea siempre
    line(150, 25,mouseX,mouseY)

#ninguna de las dos funciones se necesita llamar
#porque se llaman solas
'''

'''
def setup(): #corre solo una vez automaticamente
    size(400,400)#Esta siempre es la primera linea del setup
    stroke(255)
    background(192,64,0)
    
def draw(): #corre repetidamente
    line(150, 25,mouseX,mouseY)
    
def mousePressed():
    background(192,64,0) #ahora la pantalla se limpia de todas las demas 
    #lineas cada vez que tocamos click
'''


#una elipse a la mitad del canvas
size(400,400)
#esta forma solo funciona para este size
ellipse(200,200, 50,50)
#esta otra forma funciona para cualquier size
ellipse(width/2, height/2, 80, 80)
'''
