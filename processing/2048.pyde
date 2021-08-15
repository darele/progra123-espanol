'''
Codigo de colores:
vacio = 8E8E8E

'''

colores = {0: "#8E8E8E", 2: "#FBFED4",
           4: "#D6E701", 8: "#E89F0C",
           16: "#E75106", 32: "#F56C6C",
           128: "#C5D61B", 64: "#E43B30",
           256: "#CBC611", 512: "#DBD50F",
           1024: "#EEE943", 2048: "#F0EA29"}

class cuadro:
    def __init__(self, px, py, val):
        self.x = px
        self.y = py
        self.col = 255
        self.val = val
        self.col = colores[self.val]
        self.par = False

mat = []
band = False

def setup():
    global mat
    global f
    f = createFont("ArialBlack", 20, True)
    size(550, 725)
    background(255)
    stroke(0)
    strokeWeight(10)
    fill(150)
    rect(25, 200, 500, 500)
    x, y = [25, 200];
    for i in range(4):
        mat.append([])
        x = 25
        for j in range(4):
            if (i == 0 or i == 3 or j == 0 or j == 3): a = cuadro(x, y, 2)
            else: a = cuadro(x, y, 0)
            mat[i].append(a)
            x += 125
        y += 125
    
def display():
    #delay(500)
    global f
    textFont(f)
    for i in range(4):
        for j in range(4):
            a = mat[i][j]
            a.col = colores[a.val]
            fill(a.col)
            rect(a.x, a.y, 125, 125)
            fill(0)
            if (a.val > 0):
                text(str(a.val), a.x + 75, a.y + 75)

def draw():     
    display()
    
def keyPressed():
    global mat
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
    for i in mat:
        for j in i:
            j.par = False