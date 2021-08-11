mx = 0
my = 0
l = []
cont = 0

def setup():
    #size(700,1000)
    fullScreen()
    stroke(255)
    strokeWeight(5)
    background(68,217,124)
    
def draw():
    global mx, my, cont
    background(68,217,124)
    if (keyPressed):
        cont = 0
    if (mousePressed):
        if cont:
            l.append([mx, my, mouseX, mouseY])
            mx = mouseX
            my = mouseY
        else:
            mx = mouseX
            my = mouseY
            cont += 1
    for i in l:
        line(i[0], i[1], i[2], i[3])
    if cont:
        line(mx, my, mouseX, mouseY)
        
