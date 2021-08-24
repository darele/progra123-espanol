class celda:
    def __init__(self, x1,y1):
        self.minx = x1
        self.miny = y1
        self.col = 0
        self.vivos = 0
    
    def flipcol(self):
        if (self.col == 0): self.col = 255
        else: self.col = 0
    
    def getcol(self):
        return self.col
    
    def getcor(self):
        return [self.minx, self.miny]
    
    def getvivos(self):
        return self.vivos

l = []
tamcelda = 40
band = False
mensaje = "Presiona Enter para comenzar/parar simulacion\nClick para encender/apagar celdas"

def setup():
    global tamcelda
    '''
    se crea la fuente para poder ver la
    cantidad de vecinos vivos de cada celda
    '''
    global f
    f = createFont("Ubuntu Bold", 15, True)
    fullScreen()
    background(0)
    stroke(122,245,112)
    i = 0
    j = 0
    r = 0
    #se guarda cada celda en una matriz
    while (i < height):
        j = 0
        l.append([])
        while (j < width):
            nuevacelda = celda(j, i)
            l[r].append(nuevacelda)
            j += tamcelda
        i += tamcelda
        r += 1

'''
Para una celda cualquiera, esta funcion cuenta
la cantidad de vecinos vivos
'''
def vecinosvivos(i, j):
    global l
    r = len(l)
    c = len(l[0])
    cont = 0
    if (j > 0):
        if (i > 0 and l[i - 1][j - 1].getcol() == 255): cont += 1
        if (i < r - 1 and l[i + 1][j - 1].getcol() == 255): cont += 1
        if (l[i][j - 1].getcol() == 255): cont += 1
    if (j < c - 1):
        if (i > 0 and l[i - 1][j + 1].getcol() == 255): cont += 1
        if (i < r - 1 and l[i + 1][j + 1].getcol() == 255): cont += 1
        if (l[i][j + 1].getcol() == 255): cont += 1
    if (i > 0 and l[i - 1][j].getcol() == 255): cont += 1
    if (i < r - 1 and l[i + 1][j].getcol() == 255): cont += 1
    return cont 

def draw():
    global f, mensaje
    textFont(f)
    delay(100)
    global tamcelda
    if (band):
        for i in range(len(l)):
            for j in range(len(l[0])):
                l[i][j].vivos = vecinosvivos(i, j)
        '''
        Hasta que ya hemos contado la cantidad de 
        vecinos vivos de cada celda es que hacemos el
        cambio en el dato, porque sino no funciona
        '''
        for i in l:
            for j in i:
                if (j.getcol() == 255):
                    if (j.vivos < 2 or j.vivos > 3):
                        j.flipcol()
                else:
                    if (j.vivos == 3):
                        j.flipcol()
                        
    '''Impresion de matriz'''
    for j in l:
        for i in j:
            a = i.getcor()
            fill(i.getcol())
            rect(a[0], a[1], a[0] + tamcelda, a[1] + tamcelda)
            '''
            descomentando estas lineas veriamos
            la cantidad de vecinos vivos de cada celda
            '''
            #fill(0)
            #text(str(i.vivos), a[0] + 15, a[1] + 15)
    fill(255)
    textAlign(CENTER)
    textSize(30)
    text(mensaje, width/2, height/2)    
        
def mousePressed():
    if (band == False):
        parar = False
        for j in l:
            for i in j:
                a = i.getcor()
                if (mouseX >= a[0] and mouseX <= a[0] + tamcelda and mouseY >= a[1] and mouseY <= a[1] + tamcelda):
                    i.flipcol()
                    parar = True
                    break
            if (parar): break
            
def keyPressed():
    global band, mensaje
    '''
    cambiar entre hacer modificacion
    o que comience el juego cont ENTER
    '''
    if (key == RETURN or key == ENTER):
        if (band) : 
            band = False
            mensaje = "Presiona Enter para comenzar/parar simulacion\nClick para encender/apagar celdas"
        else : 
            band = True
            mensaje = ""
