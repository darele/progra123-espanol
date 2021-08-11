def setup():
    fullScreen()
    dibujar()
    background(255)
    
def dibujar():
    stroke(0)
    strokeWeight(5)
    
def borrar():
    stroke(255)
    strokeWeight(100)
    
def draw():
    if (mousePressed):
        line(pmouseX, pmouseY, mouseX, mouseY)

'''
def mousePressed():
    if (mouseButton == LEFT):
        dibujar()
    elif (mouseButton == RIGHT):
        borrar()
'''    

def keyPressed():
    if (key == 'l' or key == 'L'):
        dibujar()
    elif (key == 'b' or key == 'B'):
        borrar()