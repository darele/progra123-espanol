import random
import Clases as clases
import Variables_globales as vars
        
c = clases.snake()
v = []
bocado = clases.punto(0,0)

def setup():
    global f
    f = createFont("Ubuntu", 20, True)
    #fullScreen()
    size(vars.ancho * 30, vars.ancho * 30)
    background("#2BAA47")
    textAlign(CENTER)
    c.add(2*vars.ancho,0)
    c.add(vars.ancho, 0)
    c.add(0, 0)
    vacios()
    comida()
    
def vacios():
    global v
    for i in range(0, height - 1, vars.ancho):
        for j in range(0, width - 1, vars.ancho):
            if (get(j + vars.ancho / 2, i + vars.ancho / 2) == [0,0,0]) : 
                continue
            v.append([j, i])
            
def comida():
    global v, bocado
    x = random.randint(0, len(v) - 1)
    a = clases.punto(v[x][0], v[x][1])
    bocado = a
        
def draw():
    global f, bocado
    textFont(f)
    background("#2BAA47")
    fill(255)
    stroke(0)
    rect(bocado.x, bocado.y, vars.ancho, vars.ancho)
    t = millis()
    c.imprimir()
    if (c.l[0].x == bocado.x and c.l[0].y == bocado.y):
        c.agrandar()
        vacios()
        comida()
        vars.cvelocidad(vars.velocidad - 1)
    for j in range(1, len(c.l)):
        i = c.l[j]
        if (c.l[0].x == i.x and c.l[0].y == i.y):
            vars.cmensaje("Game Over")
            fill("#2DF5FA")
            textSize(30)
            text(vars.mensaje, width/2, height/2)
            noLoop()
            break
    if (t - vars.ant >= vars.velocidad):
        vars.cant(t)
        if (c.cempty() == False):
            vars.cdir(c.cpop())
        c.mover()
    
def keyPressed():
    if (vars.dir == -1):
        vars.cdir(1)
        velocidad = 800
        vars.cmensaje("")
    if (keyCode == UP):
        c.cpush(0)
    elif (keyCode == DOWN):
        c.cpush(2)
    elif (keyCode == RIGHT):
        c.cpush(1)
    elif (keyCode == LEFT):
        c.cpush(3)
    if (key == ' '):
        comida()
    
