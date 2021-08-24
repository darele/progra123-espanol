import Variables_globales as vars

ancho = vars.ancho
dir = vars.dir

class punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class snake():
    def __init__(self):
        self.l = []
        self.cola = [-1 for i in range(100)]
        self.ini = 0
        self.fin = 0
    
    #Funciones de Cola
    def cempty(self):
        return self.ini == self.fin
    def cpush(self, val):
        if(val == 0):
            if (self.cola[self.fin - 1] == 2): return
        if (val == 1):
            if (self.cola[self.fin - 1] == 3): return
        if (val == 2):
            if (self.cola[self.fin - 1] == 0): return
        if (val == 3):
            if (self.cola[self.fin - 1] == 1): return
        self.cola[self.fin] = val
        self.fin += 1
        if (self.fin == 100):
            self.fin = 0
    def cpop(self):
        temp = self.cola[self.ini]
        self.ini += 1
        if (self.ini == 100):
            self.ini = 0
        return temp
    
    #Funciones de Serpiente
    def add(self, x, y):
        a = punto(x, y)
        self.l.append(a)
    def agrandar(self):
        a = self.l[len(self.l) - 1]
        b = self.l[len(self.l) - 2]
        if (b.x < a.x):
            c = punto((a.x + vars.ancho) % width, a.y)
            self.l.append(c)
        elif (b.x > a.x):
            c = punto((a.x - vars.ancho + width) % width, a.y)
            self.l.append(c)
        elif (b.y < a.y):
            c = punto(a.x, (a.y + vars.ancho) % height)
            self.l.append(c)
        else:
            c = punto(a.x, (a.y + vars.ancho + height) % height)
            self.l.append(c)
            
    #Funciones de impresion en pantalla
    def imprimir(self):
        fill(0)
        stroke(255)
        for i in self.l:
            rect(i.x,i.y, vars.ancho, vars.ancho)
            
    #Funciones de movimiento de serpiente
    def acomodar(self):
        for i in range(len(self.l) - 1, 0, -1):
            self.l[i].x, self.l[i].y = self.l[i - 1].x, self.l[i - 1].y
    
    def mover(self):
        if (vars.dir == 0):
            self.acomodar()
            i = self.l[0]
            i.y -= ancho
            if (i.y < 0):
                i.y = height - ancho
        elif(vars.dir == 2):
            self.acomodar()
            i = self.l[0]
            i.y += ancho
            if (i.y >= height):
                i.y = 0
        elif (vars.dir == 1):
            self.acomodar()
            i = self.l[0]
            i.x += ancho
            if (i.x >= width):
                i.x = 0
        elif(vars.dir == 3):
            self.acomodar()
            i = self.l[0]
            i.x -= ancho
            if (i.x < 0):
                i.x = width - ancho
