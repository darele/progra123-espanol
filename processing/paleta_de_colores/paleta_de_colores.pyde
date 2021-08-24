ratonlevantao = True

def setup():
    global f
    f = createFont("Arial", 20, True)
    fullScreen()
    stroke(0)
    strokeWeight(5)
    background(255)
    
#Paleta de colores

def pal():
    x = 50
    a = [256, 256, 256]
    b = [-1, -1, -1]
    i = 2
    band = True
    x = 100
    while (x < width):
        stroke(a[0], a[1], a[2])
        line(x, 50, x, 100)
        a[i] += 5 * b[i]
        if (a[i] >= 256 or a[i] <= 41):
            b[i] *= -1
            i -= 1
            if (i < 0):
                i = 2
        x += 5
        if (a == [240, 41, 41]):
            band = False
    
def draw():
    global f
    global i, j, k
    pal()
    '''k += 5
    if (k >= 257):
        j += 5
        k = 0
    if (j >= 257):
        i += 5
        j = 0
    if (i >= 257):
        i = 0
    textFont(f)
    fill(255)
    rect(500, 100, 400, 100)
    fill(0)
    text(str(i) + ", " + str(j) + ", " + str(k), 520, 150)
    fill(i, j, k)
    ellipse(500, 500, 50, 50)
    '''
    global ratonlevantao
    if (ratonlevantao == False):
        stroke(255)
        fill(255)
        ellipse(pmouseX, pmouseY, 52, 52)
        ratonlevantao = True
    if (mousePressed):
        if (key == 'l' or key == 'L') : 
            stroke(0)
            line(pmouseX, pmouseY, mouseX, mouseY)
        elif (key == 'b' or key == 'B'):
            stroke(0)
            fill(150)
            ellipse(mouseX, mouseY, 50, 50)
            ratonlevantao = False
