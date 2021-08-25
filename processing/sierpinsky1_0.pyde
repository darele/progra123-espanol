import math

t = []
m = 1
nivel = 1
lim = 10000

def setup():
    global t, f
    f = createFont("Ubuntu Bold", 30, True)
    fullScreen()
    lado = float(height) + 144
    alto = (math.sqrt(3.0)/2.0)*lado
    #textFont(f)
    #text(str(lado) + " "  + str(height) + " " + str(alto), width/2, height/2)
    t.append([width/2, 0, width/2 - lado/2, alto, width/2 + lado/2, alto])
    
def draw():
    display()
    
def display():
    global t, m
    background("#20C9C8")
    stroke(0)
    strokeWeight(5)
    noFill()
    for j in range(m):
        i = t[j]
        a = [i[0], i[1]]
        b = [i[2], i[3]]
        c = [i[4], i[5]]
        triangle(a[0], a[1], b[0], b[1], c[0], c[1])
       
def siguiente():
    global t, m, nivel, lim
    if (m + 3 * nivel > lim):
        return
    for j in range(len(t) - 1, len(t) - 1 - nivel, -1):
        i = t[j]
        a = [i[0], i[1]]
        b = [i[2], i[3]]
        c = [i[4], i[5]]
        d = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]
        e = [(a[0] + c[0]) / 2, (a[1] + c[1]) / 2]
        f = [(c[0] + b[0]) / 2, (c[1] + b[1]) / 2]
        t.append([d[0], d[1], e[0], e[1], a[0], a[1]])
        t.append([d[0], d[1], f[0], f[1], b[0], b[1]])
        t.append([f[0], f[1], e[0], e[1], c[0], c[1]])
        m += 3
    nivel *= 3
          
def keyPressed():
    global t, m, nivel
    if (keyCode == RIGHT):
        if (m  == len(t)):
            siguiente()
        else:
            nivel *= 3
            m += nivel
    elif (keyCode == LEFT):
        if (m > 1):
            m -= nivel
            nivel /= 3
