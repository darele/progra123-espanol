import random

colores = {0: "#8E8E8E", 2: "#FBFED4",
           4: "#D6E701", 8: "#E89F0C",
           16: "#E75106", 32: "#F56C6C",
           128: "#C5D61B", 64: "#E43B30",
           256: "#CBC611", 512: "#DBD50F",
           1024: "#EEE943", 2048: "#F0EA29"}









#Definicion de clase

class cuadro:
    def __init__(self, px, py, val):
        self.x = px
        self.y = py
        self.desx = 0
        self.desy = 0
        self.col = 255
        self.val = val
        self.par = False







#Variables Globales

mat = []
puntaje = cuadro(220, 150, 0)
libres = []








#Funcion para generar numeros aleatorios

def numero():
    x = random.randint(1, 100000)
    if (x <= 90000): return 2
    else : return 4
    
    
    
    
    
    
    
    
def nuevo():
    global mat, libres
    x = random.randint(0, len(libres) - 1);
    mat[libres[x][0]][libres[x][1]].val = numero()
    libres.pop(x)









#Setup

def setup():
    global mat, puntaje, libres
    global f, f2
    f2 = createFont("Arial", 75, True)
    f = createFont("ArialBlack", 40, True)
    size(550, 825)
    background(255)
    stroke(0)
    strokeWeight(10)
    fill(150)
    x, y = [25, 300];
    for i in range(4):
        mat.append([])
        x = 25
        for j in range(4):
            libres.append([i, j])
            a = cuadro(x, y, 0)
            mat[i].append(a)
            x += 125
        y += 125
    nuevo()
    nuevo()
    libres = []
    for i in range(4):
        for j in range(4):
            if (i == 0 or i == 3 or j == 0 or j == 3):
                if (mat[i][j].val == 0):
                    libres.append([i, j])
        
            
                
            
#tablero

def tablero():
    x = 25
    y = 300
    for i in range(4):
        x = 25
        for j in range(4):
            fill(colores[0])
            rect(x, y, 125, 125)
            x += 125
        y += 125
            
                







#Display  
  
def display():
    background(255)
    tablero()
    global f, f2
    global puntaje
    textFont(f2)
    textAlign(CENTER)
    fill(0)
    text("Puntaje", 275, 100)
    textAlign(CENTER, CENTER)
    textFont(f)
    puntaje.col = colores[puntaje.val]
    fill(puntaje.col)
    rect(puntaje.x, puntaje.y, 125, 125)
    fill(0)
    text(str(puntaje.val), puntaje.x + 62, puntaje.y + 62)
    for i in range(4):
        for j in range(4):
            a = mat[i][j]
            if (a.val == 0): continue
            if (a.val > puntaje.val):
                puntaje.val = a.val
            a.col = colores[a.val]
            fill(a.col)
            rect(a.x, a.y, 125, 125)
            fill(0)
            if (a.val > 0):
                text(str(a.val), a.x + 62, a.y + 62)






#Draw

def draw():
    global mat, puntaje
    if (puntaje == 2048):
        noLoop()
    display()
    
    
    
    
    
    
    
    









#KeyPressed

def keyPressed():
    global mat, puntaje
    global libres
    libres = []
    cmat = [[j.val for j in i] for i in mat]
    if (keyCode == UP):
        for i in range(1, 4):
            for j in range(4):
                ci = i
                while (i > 0 and mat[i - 1][j].val == 0):
                    mat[i - 1][j].val = mat[i][j].val
                    mat[i][j].val = 0
                    i -= 1
                if (i > 0 and mat[i - 1][j].val == mat[i][j].val and mat[i - 1][j].par == False):
                    mat[i - 1][j].val *= 2
                    mat[i][j].val = 0
                    mat[i - 1][j].par = True
                i = ci
    if (keyCode == DOWN):
        for i in range(2, -1, -1):
            for j in range(4):
                ci = i
                while (i < 3 and mat[i + 1][j].val == 0):
                    mat[i + 1][j].val = mat[i][j].val
                    mat[i][j].val = 0
                    i += 1
                if (i < 3 and mat[i + 1][j].val == mat[i][j].val and mat[i + 1][j].par == False):
                    mat[i + 1][j].val *= 2
                    mat[i][j].val = 0
                    mat[i + 1][j].par = True
                i = ci
    if (keyCode == LEFT):
        for i in range(4):
            for j in range(1, 4):
                cj = j
                while (j > 0 and mat[i][j - 1].val == 0):
                    mat[i][j - 1].val = mat[i][j].val
                    mat[i][j].val = 0
                    j -= 1
                if (j > 0 and mat[i][j - 1].val == mat[i][j].val and mat[i][j - 1].par == False):
                    mat[i][j - 1].val *= 2
                    mat[i][j].val = 0
                    mat[i][j - 1].par = True
                j = cj
    if (keyCode == RIGHT):
        for i in range(4):
            for j in range(2, -1, -1):
                cj = j
                while (j < 3 and mat[i][j + 1].val == 0):
                    mat[i][j + 1].val = mat[i][j].val
                    mat[i][j].val = 0
                    j += 1
                if (j < 3 and mat[i][j + 1].val == mat[i][j].val and mat[i][j + 1].par == False):
                    mat[i][j + 1].val *= 2
                    mat[i][j].val = 0
                    mat[i][j + 1].par = True
                j = cj
    for i in range(len(mat)):
        for k in range(len(mat[0])):
            j = mat[i][k]
            j.par = False
            puntaje.val = max(puntaje.val, j.val)
            if (i == 0 or i == 3 or k == 0 or k == 3):
                if (j.val == 0):
                    libres.append([i, k])
    
    mueve = False
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if (mat[i][j].val != cmat[i][j]):
                mueve = True
    if (mueve):
        nuevo()
