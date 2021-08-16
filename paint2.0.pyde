ratonlevantao = True
ex = 0
ey = 0

def setup():
    fullScreen()
    dibujar()
    background(255)
    
def dibujar():
    stroke(0)
    strokeWeight(5)
    
def draw():
    global ex, ey, ratonlevantao
    if (ratonlevantao == False):
        stroke(255)
        fill(255)
        ellipse(ex, ey, 52, 52)
        ratonlevantao = True
    if (mousePressed):
        if (key == 'l' or key == 'L'):
            dibujar() 
            line(pmouseX, pmouseY, mouseX, mouseY)
        elif (key == 'b' or key == 'B'):
            strokeWeight(5)
            stroke(0)
            fill(150)
            ellipse(mouseX, mouseY, 50, 50)
            ex = mouseX
            ey = mouseY
            ratonlevantao = False
    
    
    
    
    
    