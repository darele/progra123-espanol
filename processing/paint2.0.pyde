ratonlevantao = True

def setup():
    fullScreen()
    stroke(0)
    strokeWeight(5)
    background(255)
    
def draw():
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
    
    
    
    
    
    