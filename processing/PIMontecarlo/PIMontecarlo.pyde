import random

dardos = 1000000
ce = []
ancho = 750
contcuadro = 0.0
contcirc = 0.0

def setup():
    global f, ce
    f = createFont("Ubuntu Bold", 30, True)
    background("#C6C62A")
    size(760, 800)
    ce = [width / 2, 380]
    fill("#B26C10")
    strokeWeight(5)
    rectMode(CENTER)
    rect(ce[0], ce[1], ancho, ancho)
    ellipse(ce[0], ce[1], ancho, ancho)
    
def draw():
    global dardos, f, ce, contcuadro, contcirc
    if (dardos == 0) :
        noLoop()
        return
    textFont(f)
    for i in range(1000):
        if (dardos == 0):
            break
        fill("#15E3E8")
        strokeWeight(1)
        dardos -= 1
        x, y = numran()
        ellipse(x, y, 5, 5)
        temp = dist(x, y)
        fill("#C6C62A")
        rectMode(CORNER)
        rect(0, height - 30, width, 30)
        fill(0)
        r = temp[0] * temp[0] + temp[1] * temp[1]
        contcuadro += 1
        radio = ancho / 2
        radio *= radio
        if (r <= radio) :
            contcirc += 1
        text(str((4 * contcirc) / contcuadro) + "        " + str(contcuadro), 3, height - 5)
    
def numran():
    x = random.randint((width - ancho) / 2, (width - ancho) / 2 + ancho)
    y = random.randint(5, 5 + ancho)
    return [x, y]

def dist(x, y):
    global ce
    return [x - ce[0], y - ce[1]]
